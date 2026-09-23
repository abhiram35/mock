import { useCallback, useEffect, useRef, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { ArrowLeft, Check, CircleAlert } from "lucide-react";

import { Badge, Button, Card, Skeleton } from "../../components/primitives";
import { useToast } from "../../components/primitives/Toast";
import { practiceClient } from "../../lib/practice/client";
import {
  clearSolveProgress,
  loadSolveProgress,
  saveSolveProgress,
} from "../../lib/practice/client";
import {
  EMPTY_PLAN,
  SOLVE_STAGES,
  type RunNarration,
  type SolveProgress,
  type SolveStageId,
} from "../../lib/practice/types";
import type { CodeExecutionResponse, CodingQuestion } from "../../lib/api";

import UnderstandStage from "./solve/UnderstandStage";
import PlanStage from "./solve/PlanStage";
import CodeStage from "./solve/CodeStage";
import VerifyStage from "./solve/VerifyStage";
import ReflectStage from "./solve/ReflectStage";

const stageOrder: SolveStageId[] = [
  "understand",
  "plan",
  "code",
  "verify",
  "reflect",
];

function freshProgress(startAt: SolveStageId = "understand"): SolveProgress {
  return {
    stage: startAt,
    plan: { ...EMPTY_PLAN },
    reflection: "",
    completedAt: {},
  };
}

const RUN_ERROR_COPY: Record<string, string> = {
  docker:
    "The code sandbox isn't reachable right now. It usually means Docker isn't running on the server — try again shortly.",
  rate:
    "That's the rate limit talking. Give it a few seconds, then run again.",
  timeout:
    "Your code ran past the time limit. Check for an infinite loop or a much-slower-than-planned approach.",
  memory:
    "Your code used more memory than allowed. Look for unbounded data structures.",
};

function classifyRunError(message: string): string {
  const lower = message.toLowerCase();

  if (lower.includes("docker")) {
    return RUN_ERROR_COPY.docker;
  }

  if (lower.includes("rate") || lower.includes("429") || lower.includes("too many")) {
    return RUN_ERROR_COPY.rate;
  }

  if (lower.includes("time") || lower.includes("timeout")) {
    return RUN_ERROR_COPY.timeout;
  }

  if (lower.includes("memory")) {
    return RUN_ERROR_COPY.memory;
  }

  return message;
}

/**
 * The 5-stage solve flow: Understand → Plan → Code → Verify →
 * Reflect. Stage progress persists locally per problem; code runs
 * and submissions go through the real execution endpoints.
 */
export default function SolvePage() {
  const { trackId, questionId } = useParams<{
    trackId: string;
    questionId: string;
  }>();

  const navigate = useNavigate();

  const { toast } = useToast();

  const [problem, setProblem] = useState<CodingQuestion | null>(null);

  const [trackName, setTrackName] = useState("Track");

  const [loadError, setLoadError] = useState<string | null>(null);

  const [progress, setProgress] = useState<SolveProgress>(() =>
    freshProgress(),
  );

  const [code, setCode] = useState("");

  const [runResult, setRunResult] = useState<CodeExecutionResponse | null>(
    null,
  );

  const [isRunning, setIsRunning] = useState(false);

  const [runError, setRunError] = useState<string | null>(null);

  const [narration, setNarration] = useState<RunNarration | null>(null);

  const [submitted, setSubmitted] = useState(false);

  const narrationTimer = useRef<number | null>(null);

  /* ---------------- Load problem + prior progress ---------------- */

  useEffect(() => {
    let cancelled = false;

    const numericId = Number(questionId);

    if (!Number.isInteger(numericId) || numericId <= 0) {
      setLoadError("That problem link doesn't look right.");
      return;
    }

    practiceClient
      .listTracks()
      .then((tracks) => {
        if (cancelled) {
          return;
        }

        const match = tracks.find((track) => track.id === trackId);

        if (match) {
          setTrackName(match.name);
        }
      })
      .catch(() => {
        /* Breadcrumb falls back to "Track". */
      });

    practiceClient
      .getProblem(numericId)
      .then((data) => {
        if (cancelled) {
          return;
        }

        setProblem(data);

        setCode(data.starter_code || "");

        const saved = loadSolveProgress(numericId);

        if (saved) {
          setProgress(saved);
        }
      })
      .catch(() => {
        if (!cancelled) {
          setLoadError(
            "Couldn't load this problem. It may have been removed — the track list has what's available.",
          );
        }
      });

    return () => {
      cancelled = true;
    };
  }, [questionId, trackId]);

  /* ---------------- Persistence ---------------- */

  useEffect(() => {
    if (problem) {
      saveSolveProgress(problem.id, progress);
    }
  }, [problem, progress]);

  /* ---------------- Navigation ---------------- */

  const stageIndex = stageOrder.indexOf(progress.stage);

  const goToStage = useCallback(
    (stage: SolveStageId) => {
      setProgress((current) => {
        const next: SolveProgress = {
          ...current,
          stage,
          completedAt: {
            ...current.completedAt,
            [current.stage]: current.completedAt[current.stage] ?? Date.now(),
          },
        };

        return next;
      });
    },
    [],
  );

  const advance = useCallback(() => {
    const next = stageOrder[Math.min(stageIndex + 1, stageOrder.length - 1)];

    goToStage(next);
  }, [stageIndex, goToStage]);

  const goBack = useCallback(() => {
    const prev = stageOrder[Math.max(stageIndex - 1, 0)];

    goToStage(prev);
  }, [stageIndex, goToStage]);

  /* ---------------- Run & submit ---------------- */

  async function execute(kind: "run" | "submit") {
    if (!problem || isRunning) {
      return;
    }

    setIsRunning(true);

    setRunError(null);

    setRunResult(null);

    const phases: RunNarration["phase"][] =
      kind === "run"
        ? ["submitting", "compiling", "running", "comparing"]
        : ["submitting", "compiling", "running", "comparing"];

    let phaseIndex = 0;

    const tickNarration = () => {
      setNarration({
        phase: phases[Math.min(phaseIndex, phases.length - 1)],
        message:
          kind === "submit" && phaseIndex >= 2
            ? "Recording your submission…"
            : ["Sending to the sandbox…", "Setting up Python 3.12…", "Running your code…", "Comparing outputs…"][
                Math.min(phaseIndex, 3)
              ],
      });

      phaseIndex += 1;

      narrationTimer.current = window.setTimeout(tickNarration, 900);
    };

    tickNarration();

    try {
      const result =
        kind === "run"
          ? await practiceClient.run(problem.id, code)
          : await practiceClient.submit(problem.id, code);

      if (narrationTimer.current) {
        window.clearTimeout(narrationTimer.current);
      }

      setNarration({ phase: "done", message: "Done." });

      setRunResult(result);

      if (kind === "submit") {
        setSubmitted(true);
      }

      if (result.success) {
        goToStage("verify");
      } else {
        goToStage("verify");

        if (kind === "submit") {
          toast({
            tone: "warn",
            title: "Not all cases passed",
            description: "Hidden cases are trying to tell you something.",
          });
        }
      }
    } catch (err) {
      const message =
        err instanceof Error ? err.message : "Something went wrong.";

      setRunError(classifyRunError(message));
    } finally {
      if (narrationTimer.current) {
        window.clearTimeout(narrationTimer.current);
      }

      setIsRunning(false);

      window.setTimeout(() => setNarration(null), 400);
    }
  }

  const run = useCallback(() => void execute("run"), [problem, code, isRunning]);

  const submit = useCallback(
    () => void execute("submit"),
    [problem, code, isRunning],
  );

  /* ---------------- Render ---------------- */

  if (loadError) {
    return (
      <div className="mx-auto w-full max-w-5xl px-5 py-10 md:px-8">
        <Card padding="lg" className="border-[color:var(--bad)]">
          <div className="flex items-start gap-3">
            <CircleAlert className="mt-0.5 text-[color:var(--bad)]" size={18} />

            <div>
              <h1 className="display text-lg text-ink">
                Couldn't open the problem
              </h1>

              <p className="mt-1.5 text-sm leading-6 text-ink-2">{loadError}</p>

              <Button
                variant="secondary"
                size="sm"
                className="mt-4"
                onClick={() => navigate(`/app/practice/${trackId ?? ""}`)}
              >
                Back to the track
              </Button>
            </div>
          </div>
        </Card>
      </div>
    );
  }

  if (!problem) {
    return (
      <div className="mx-auto w-full max-w-5xl px-5 py-10 md:px-8">
        <Skeleton className="h-7 w-64" variant="block" />

        <div className="mt-8 flex gap-2">
          {[0, 1, 2, 3, 4].map((index) => (
            <Skeleton key={index} className="h-8 w-24" />
          ))}
        </div>

        <Skeleton className="mt-8 h-72 w-full" variant="block" />
      </div>
    );
  }

  const stageProps = {
    problem,
    progress,
    onNext: advance,
    onJump: goToStage,
  };

  return (
    <div className="mx-auto w-full max-w-6xl px-5 py-8 md:px-8">
      {/* Context header */}
      <div className="flex items-center gap-3">
        <Link
          to={`/app/practice/${trackId ?? ""}`}
          className="inline-flex items-center gap-1.5 text-[13px] text-ink-3 transition-colors hover:text-ink"
        >
          <ArrowLeft size={14} /> {trackName}
        </Link>

        <span className="text-ink-3">/</span>

        <span className="truncate text-[13px] font-medium text-ink">
          {problem.title}
        </span>

        <Badge
          tone={
            problem.difficulty === "easy"
              ? "ok"
              : problem.difficulty === "medium"
                ? "warn"
                : "bad"
          }
          className="ml-auto"
        >
          {problem.difficulty}
        </Badge>
      </div>

      {/* Stage rail */}
      <nav
        aria-label="Solve stages"
        className="mt-6 flex items-center gap-1 overflow-x-auto pb-1"
      >
        {SOLVE_STAGES.map((stage, index) => {
          const isActive = stage.id === progress.stage;

          const isDone = Boolean(progress.completedAt[stage.id]);

          return (
            <button
              key={stage.id}
              onClick={() => goToStage(stage.id)}
              aria-current={isActive ? "step" : undefined}
              className={`
                group flex items-center gap-2 rounded-lg px-3 py-1.5 text-[13px]
                transition-colors
                ${
                  isActive
                    ? "bg-accent-soft font-medium text-accent"
                    : isDone
                      ? "text-ink-2 hover:bg-paper-sunken"
                      : "text-ink-3 hover:bg-paper-sunken"
                }
              `}
            >
              <span
                aria-hidden="true"
                className={`
                  flex h-4.5 w-4.5 h-[18px] w-[18px] items-center justify-center
                  rounded-full border text-[10px]
                  ${
                    isDone
                      ? "border-transparent bg-accent text-[color:var(--accent-ink)]"
                      : isActive
                        ? "border-accent text-accent"
                        : "border-line-strong text-ink-3"
                  }
                `}
              >
                {isDone ? <Check size={10} /> : index + 1}
              </span>

              <span className="whitespace-nowrap">{stage.label}</span>

              {index < SOLVE_STAGES.length - 1 && (
                <span aria-hidden="true" className="ml-1 text-ink-3">
                  →
                </span>
              )}
            </button>
          );
        })}
      </nav>

      {/* Stage content */}
      <div className="mt-6">
        {progress.stage === "understand" && (
          <UnderstandStage {...stageProps} />
        )}

        {progress.stage === "plan" && (
          <PlanStage
            {...stageProps}
            onPlanChange={(plan) =>
              setProgress((current) => ({ ...current, plan }))
            }
            onBack={goBack}
          />
        )}

        {progress.stage === "code" && (
          <CodeStage
            {...stageProps}
            code={code}
            onCodeChange={setCode}
            onRun={run}
            onSubmit={submit}
            runResult={runResult}
            narration={narration}
            isRunning={isRunning}
            runError={runError}
            onProceedToVerify={() => goToStage("verify")}
            onBack={goBack}
          />
        )}

        {progress.stage === "verify" && (
          <VerifyStage
            {...stageProps}
            runResult={runResult}
            submitted={submitted}
            onBack={goBack}
            onNext={advance}
          />
        )}

        {progress.stage === "reflect" && (
          <ReflectStage
            {...stageProps}
            runResult={runResult}
            onReflectionChange={(reflection) =>
              setProgress((current) => ({ ...current, reflection }))
            }
            onBack={goBack}
            onRestart={() => {
              clearSolveProgress(problem.id);

              setProgress(freshProgress());

              setRunResult(null);

              setSubmitted(false);

              setCode(problem.starter_code || "");
            }}
          />
        )}
      </div>
    </div>
  );
}
