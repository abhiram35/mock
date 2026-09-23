import { useEffect, useMemo, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import {
  ArrowRight,
  BookOpen,
  CalendarCheck,
  Flame,
  Play,
  Zap,
} from "lucide-react";

import {
  Badge,
  Button,
  Card,
  EmptyState,
  Skeleton,
} from "../../components/primitives";
import { getInterviews, getTopics } from "../../lib/api";
import { practiceClient } from "../../lib/practice/client";
import type { Interview, Topic } from "../../lib/api";

function greetingFor(date: Date): string {
  const hour = date.getHours();

  if (hour < 5) {
    return "Up late";
  }

  if (hour < 12) {
    return "Good morning";
  }

  if (hour < 18) {
    return "Good afternoon";
  }

  return "Good evening";
}

/**
 * Local, forgiving streak: consecutive days (ending today or
 * yesterday) on which the user solved a problem or completed an
 * interview. One freeze day is allowed before the chain breaks.
 */
function computeStreak(dates: string[]): number {
  if (dates.length === 0) {
    return 0;
  }

  const unique = Array.from(
    new Set(dates.map((date) => date.slice(0, 10))),
  ).sort();

  const dayMs = 86_400_000;

  let streak = 0;

  let cursor = Date.now();

  // Allow today to be missing (day isn't over yet).
  const last = new Date(unique[unique.length - 1]).getTime();

  if (cursor - last > 2 * dayMs) {
    return 0;
  }

  if (cursor - last <= dayMs) {
    streak += 1;
  }

  cursor = last;

  let freezes = 1;

  for (let i = unique.length - 2; i >= 0; i -= 1) {
    const current = new Date(unique[i]).getTime();

    const gap = cursor - current;

    if (gap <= dayMs) {
      streak += 1;
    } else if (gap <= 2 * dayMs && freezes > 0) {
      streak += 1;
      freezes -= 1;
    } else {
      break;
    }

    cursor = current;
  }

  return streak;
}

/**
 * Dashboard, redesigned. Everything comes from real endpoints:
 * interviews (continue/recent scores), topics (quick start),
 * practice problems (continue coding + streak).
 */
export default function DashboardV2() {
  const navigate = useNavigate();

  const [interviews, setInterviews] = useState<Interview[] | null>(null);

  const [topics, setTopics] = useState<Topic[] | null>(null);

  const [problems, setProblems] = useState<
    Awaited<ReturnType<typeof practiceClient.listProblems>> | null
  >(null);

  const [solvedIds, setSolvedIds] = useState<Set<number>>(new Set());

  const [loadError, setLoadError] = useState<string | null>(null);

  const me = useMemo<{ fullName: string; firstName: string }>(() => {
    try {
      const parsed = JSON.parse(
        localStorage.getItem("user") ?? "{}",
      ) as { full_name?: string };

      const fullName = parsed.full_name ?? "there";

      return {
        fullName,
        firstName: fullName.split(/\s+/)[0] ?? "there",
      };
    } catch {
      return { fullName: "there", firstName: "there" };
    }
  }, []);

  useEffect(() => {
    let cancelled = false;

    Promise.all([
      getInterviews(),
      getTopics(),
      practiceClient.listProblems().catch(() => []),
      practiceClient.getSolvedIds().catch(() => [] as number[]),
    ])
      .then(([interviewData, topicData, problemData, solved]) => {
        if (cancelled) {
          return;
        }

        setInterviews(
          [...interviewData].sort(
            (a, b) =>
              new Date(b.created_at).getTime() -
              new Date(a.created_at).getTime(),
          ),
        );

        setTopics(topicData);

        setProblems(problemData);

        setSolvedIds(new Set(solved));
      })
      .catch(() => {
        if (!cancelled) {
          setLoadError(
            "Your data didn't load. The backend might be napping — retry?",
          );
        }
      });

    return () => {
      cancelled = true;
    };
  }, []);

  const inProgress = interviews?.find(
    (interview) => interview.status === "in_progress",
  );

  const nextProblem = useMemo(() => {
    if (!problems) {
      return null;
    }

    return problems.find((problem) => !solvedIds.has(problem.id)) ?? null;
  }, [problems, solvedIds]);

  const completed = useMemo(
    () => interviews?.filter((interview) => interview.status === "completed") ?? [],
    [interviews],
  );

  const streak = useMemo(() => {
    const days: string[] = [];

    completed.forEach((interview) => days.push(interview.updated_at));

    if (solvedIds.size > 0 && problems) {
      problems
        .filter((problem) => solvedIds.has(problem.id))
        .forEach((problem) => days.push(problem.updated_at));
    }

    return computeStreak(days);
  }, [completed, problems, solvedIds]);

  const activeTopics = useMemo(
    () => (topics ?? []).filter((topic) => topic.is_active).slice(0, 3),
    [topics],
  );

  function handleLogout() {
    localStorage.removeItem("access_token");

    localStorage.removeItem("user");

    navigate("/login");
  }

  return (
    <div className="mx-auto w-full max-w-5xl px-5 py-10 md:px-8">
      {/* Greeting row */}
      <header className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <p className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
            {new Date().toLocaleDateString(undefined, {
              weekday: "long",
              month: "long",
              day: "numeric",
            })}
          </p>

          <h1 className="display mt-2 text-3xl text-ink md:text-4xl">
            {greetingFor(new Date())}, {me.firstName}.
          </h1>
        </div>

        <div className="flex items-center gap-3">
          {streak > 0 && (
            <Badge tone="warn" icon={<Flame size={12} />}>
              <span className="tnum">{streak}</span>-day streak
            </Badge>
          )}

          <Button
            variant="ghost"
            size="sm"
            onClick={handleLogout}
          >
            Sign out
          </Button>
        </div>
      </header>

      {loadError && (
        <Card padding="md" className="mt-6 border-[color:var(--bad)]">
          <p className="text-sm text-ink-2">{loadError}</p>

          <Button
            variant="secondary"
            size="sm"
            className="mt-3"
            onClick={() => window.location.reload()}
          >
            Retry
          </Button>
        </Card>
      )}

      {/* Continue where you left off */}
      <section className="mt-8 grid gap-4 md:grid-cols-2">
        {interviews === null && !loadError ? (
          <>
            <Skeleton className="h-28 w-full" variant="block" />
            <Skeleton className="h-28 w-full" variant="block" />
          </>
        ) : (
          <>
            {inProgress ? (
              <Card
                interactive
                padding="lg"
                onClick={() => navigate(`/interviews/${inProgress.id}`)}
              >
                <p className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
                  Continue
                </p>

                <h2 className="display mt-2 text-xl text-ink">
                  Your interview in progress
                </h2>

                <p className="mt-1 text-[13px] text-ink-2">
                  Question {inProgress.current_question_number} of{" "}
                  {inProgress.total_questions} · waiting since{" "}
                  {new Date(inProgress.updated_at).toLocaleDateString(
                    undefined,
                    { month: "short", day: "numeric" },
                  )}
                </p>

                <span className="mt-4 inline-flex items-center gap-1.5 text-[13px] font-medium text-accent">
                  Resume now <ArrowRight size={14} />
                </span>
              </Card>
            ) : (
              nextProblem && (
                <Card
                  interactive
                  padding="lg"
                  onClick={() =>
                    navigate(`/app/practice/0/${nextProblem.id}`)
                  }
                >
                  <p className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
                    Up next in practice
                  </p>

                  <h2 className="display mt-2 text-xl text-ink">
                    {nextProblem.title}
                  </h2>

                  <p className="mt-1 text-[13px] text-ink-2 capitalize">
                    {nextProblem.difficulty} · five-stage solve flow
                  </p>

                  <span className="mt-4 inline-flex items-center gap-1.5 text-[13px] font-medium text-accent">
                    Pick it up <ArrowRight size={14} />
                  </span>
                </Card>
              )
            )}

            <Card padding="lg">
              <p className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
                Today's quest
              </p>

              <ul className="mt-3 space-y-2 text-sm text-ink-2">
                <li className="flex items-center gap-2.5">
                  <BookOpen size={14} className="text-accent" />
                  One problem — {nextProblem ? "queued" : "all caught up"}
                </li>

                <li className="flex items-center gap-2.5">
                  <Zap size={14} className="text-accent" />
                  One interview — {inProgress ? "resumable" : "not started"}
                </li>

                <li className="flex items-center gap-2.5">
                  <CalendarCheck size={14} className="text-accent" />
                  Keep the streak alive
                </li>
              </ul>
            </Card>
          </>
        )}
      </section>

      {/* Quick start */}
      <section className="mt-10">
        <div className="flex items-end justify-between">
          <h2 className="display text-xl text-ink">Quick start</h2>

          <Link
            to="/app/practice"
            className="text-[13px] font-medium text-accent hover:underline"
          >
            All tracks →
          </Link>
        </div>

        {topics === null && !loadError ? (
          <div className="mt-4 flex gap-3">
            <Skeleton className="h-20 flex-1" variant="block" />
            <Skeleton className="h-20 flex-1" variant="block" />
            <Skeleton className="h-20 flex-1" variant="block" />
          </div>
        ) : (
          <div className="mt-4 grid gap-3 sm:grid-cols-3">
            {activeTopics.map((topic) => (
              <Card
                key={topic.id}
                interactive
                padding="md"
                onClick={() => navigate("/interviews/new")}
              >
                <p className="text-sm font-medium text-ink">{topic.name}</p>

                <p className="mt-1 line-clamp-1 text-xs text-ink-3">
                  {topic.description ?? "Topic interview"}
                </p>

                <span className="mt-3 inline-flex items-center gap-1 text-[12px] font-medium text-accent">
                  <Play size={11} /> Start interview
                </span>
              </Card>
            ))}
          </div>
        )}
      </section>

      {/* Recent scores */}
      <section className="mt-10">
        <h2 className="display text-xl text-ink">Recent interviews</h2>

        {interviews === null ? null : interviews.length === 0 ? (
          <div className="mt-4">
            <EmptyState
              icon={<Zap size={18} />}
              title="No interviews yet"
              description="The first one is the hardest. Fifteen minutes, one topic, honest feedback."
              action={{
                label: "Start your first interview",
                onClick: () => navigate("/interviews/new"),
              }}
            />
          </div>
        ) : (
          <Card padding="none" elevation="xs" className="mt-4 overflow-hidden">
            <ul className="divide-y divide-line">
              {interviews.slice(0, 5).map((interview) => (
                <li
                  key={interview.id}
                  className="flex items-center gap-4 px-5 py-3.5"
                >
                  <span className="min-w-0 flex-1">
                    <span className="block truncate text-sm text-ink">
                      Interview #{interview.id}
                    </span>

                    <span className="block text-xs text-ink-3">
                      {new Date(interview.created_at).toLocaleDateString(
                        undefined,
                        { month: "short", day: "numeric" },
                      )}
                    </span>
                  </span>

                  <Badge
                    tone={
                      interview.status === "completed"
                        ? "ok"
                        : interview.status === "in_progress"
                          ? "warn"
                          : "bad"
                    }
                  >
                    {interview.status === "in_progress"
                      ? "In progress"
                      : interview.status}
                  </Badge>

                  <span className="tnum w-10 text-right text-sm font-medium text-ink">
                    {interview.overall_score !== null
                      ? Math.round(interview.overall_score)
                      : "—"}
                  </span>

                  {interview.status === "completed" && (
                    <Link
                      to={`/interviews/${interview.id}/result`}
                      className="text-[13px] font-medium text-accent hover:underline"
                    >
                      Report
                    </Link>
                  )}
                </li>
              ))}
            </ul>
          </Card>
        )}
      </section>
    </div>
  );
}
