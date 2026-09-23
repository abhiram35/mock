import { ArrowLeft, RotateCcw, Sparkles } from "lucide-react";

import {
  Badge,
  Button,
  Card,
  Textarea,
} from "../../../components/primitives";
import type { ReflectStageProps } from "./stageProps";

/**
 * REFLECT — planned vs achieved complexity, a written takeaway,
 * and an honest AI comparison state (needs Gemini keys; says so).
 */
export default function ReflectStage({
  progress,
  runResult,
  onReflectionChange,
  onBack,
  onRestart,
}: ReflectStageProps & {
  onBack: () => void;
  runResult: import("../../../lib/api").CodeExecutionResponse | null;
}) {
  const plan = progress.plan;

  const allPassed = runResult?.success === true;

  return (
    <div className="grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
      <Card padding="lg">
        <h2 className="display text-xl text-ink">What did you learn?</h2>

        <p className="mt-1.5 text-sm leading-6 text-ink-2">
          One honest sentence you'd want to reread in a week. This stays
          on your device.
        </p>

        <div className="mt-5">
          <Textarea
            label="Your note"
            value={progress.reflection}
            onChange={(event) => onReflectionChange(event.target.value)}
            placeholder="Next time I see a 'find the pair' problem, I'll reach for the hash map first…"
          />
        </div>

        <div className="mt-6 flex items-center justify-between">
          <Button
            variant="ghost"
            size="sm"
            icon={<ArrowLeft size={15} />}
            onClick={onBack}
          >
            Back to verify
          </Button>

          <Button
            variant="secondary"
            size="sm"
            icon={<RotateCcw size={14} />}
            onClick={onRestart}
          >
            Restart this problem
          </Button>
        </div>
      </Card>

      <div className="flex flex-col gap-6">
        <Card padding="lg">
          <h3 className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
            Plan vs reality
          </h3>

          <dl className="mt-3 flex flex-col gap-2.5 text-sm">
            <div className="flex items-center justify-between gap-3">
              <dt className="text-ink-2">Pattern you chose</dt>

              <dd>
                {plan.pattern ? (
                  <Badge tone="accent">{plan.pattern}</Badge>
                ) : (
                  <span className="text-ink-3">—</span>
                )}
              </dd>
            </div>

            <div className="flex items-center justify-between gap-3">
              <dt className="text-ink-2">Time / space you predicted</dt>

              <dd className="mono tnum text-[13px] text-ink">
                {plan.timeComplexity || "?"}
                {plan.spaceComplexity ? ` · ${plan.spaceComplexity}` : ""}
              </dd>
            </div>

            <div className="flex items-center justify-between gap-3">
              <dt className="text-ink-2">Tests</dt>

              <dd>
                {runResult ? (
                  <Badge tone={allPassed ? "ok" : "bad"}>
                    {allPassed
                      ? "all passing"
                      : `${runResult.passed_test_cases}/${runResult.total_test_cases}`}
                  </Badge>
                ) : (
                  <span className="text-ink-3">not run</span>
                )}
              </dd>
            </div>
          </dl>
        </Card>

        {/* Honest AI state */}
        <Card padding="lg" className="border-dashed">
          <div className="flex items-center gap-2">
            <Sparkles size={14} className="text-ink-3" />

            <h3 className="text-[13px] font-medium text-ink-2">
              Compare with the optimal
            </h3>
          </div>

          <p className="mt-2 text-sm leading-6 text-ink-2">
            When AI is enabled, your solution goes line-by-line against a
            reference answer — what you'd miss, what you'd over-engineer.
          </p>

          <Button
            variant="secondary"
            size="sm"
            className="mt-4"
            disabled
            title="AI features are unavailable — Gemini keys not configured"
          >
            Compare solutions
          </Button>
        </Card>
      </div>
    </div>
  );
}
