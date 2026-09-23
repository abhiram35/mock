import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import {
  ArrowLeft,
  CircleDashed,
  CircleCheck,
  CircleX,
  Lock,
} from "lucide-react";

import {
  Badge,
  Card,
  EmptyState,
  Progress,
  Skeleton,
} from "../../components/primitives";
import { practiceClient } from "../../lib/practice/client";
import type { PracticeTrack } from "../../lib/practice/types";
import type { CodingQuestion } from "../../lib/api";

const DIFFICULTY_TONE = {
  easy: "ok",
  medium: "warn",
  hard: "bad",
} as const;

function RowSkeleton() {
  return (
    <div className="flex items-center gap-4 px-5 py-4">
      <Skeleton className="h-4 w-4" variant="block" />

      <div className="flex-1">
        <Skeleton className="h-4 w-52" />
      </div>

      <Skeleton className="h-5 w-16" />
    </div>
  );
}

/**
 * One track: its problems, your status on each, difficulty at a
 * glance. Solved state comes from the submissions endpoint.
 */
export default function TrackPage() {
  const { trackId } = useParams<{ trackId: string }>();

  const [track, setTrack] = useState<PracticeTrack | null>(null);

  const [problems, setProblems] = useState<CodingQuestion[] | null>(null);

  const [solvedIds, setSolvedIds] = useState<Set<number>>(new Set());

  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;

    async function load() {
      try {
        setError(null);

        const [tracks, problemsData] = await Promise.all([
          practiceClient.listTracks(),
          practiceClient.listProblems(trackId),
        ]);

        if (cancelled) {
          return;
        }

        setTrack(
          tracks.find((candidate) => candidate.id === trackId) ?? null,
        );

        setProblems(problemsData);

        const solved = await practiceClient
          .getSolvedIds()
          .catch(() => [] as number[]);

        if (!cancelled) {
          setSolvedIds(new Set(solved));
        }
      } catch {
        if (!cancelled) {
          setError(
            "Couldn't load this track. The backend may be down — try again in a moment.",
          );
        }
      }
    }

    void load();

    return () => {
      cancelled = true;
    };
  }, [trackId]);

  const solvedCount = problems
    ? problems.filter((problem) => solvedIds.has(problem.id)).length
    : 0;

  return (
    <div className="mx-auto w-full max-w-5xl px-5 py-10 md:px-8">
      {/* Breadcrumb + title */}
      <Link
        to="/app/practice"
        className="inline-flex items-center gap-1.5 text-[13px] text-ink-3 transition-colors hover:text-ink"
      >
        <ArrowLeft size={14} /> All tracks
      </Link>

      {track ? (
        <header className="mt-5 max-w-2xl">
          <div className="flex items-center gap-2.5">
            <span
              aria-hidden="true"
              className="subject-mark"
              style={{ ["--mark" as string]: track.color }}
            />

            <span className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
              Track
            </span>

            {!track.executable && (
              <Badge tone="warn" icon={<Lock size={11} />}>
                Runner coming soon
              </Badge>
            )}
          </div>

          <h1 className="display mt-3 text-3xl text-ink md:text-4xl">
            {track.name}
          </h1>

          <p className="mt-2 text-[15px] text-ink-2">{track.tagline}</p>

          <div className="mt-5 max-w-xs">
            <div className="mb-1.5 flex items-center justify-between text-xs text-ink-2">
              <span className="tnum">
                {solvedCount}/{problems?.length ?? 0} solved
              </span>

              <span className="tnum">
                {problems?.length
                  ? Math.round((solvedCount / problems.length) * 100)
                  : 0}
                %
              </span>
            </div>

            <Progress
              value={solvedCount}
              max={problems?.length || 1}
              label={`${track.name} progress`}
            />
          </div>
        </header>
      ) : (
        problems === null &&
        !error && (
          <div className="mt-5">
            <Skeleton className="h-9 w-56" variant="block" />
          </div>
        )
      )}

      {error && (
        <div className="mt-8 rounded-xl border border-line bg-paper-raised px-5 py-4">
          <p className="text-sm text-ink-2">{error}</p>
        </div>
      )}

      {/* Problem list */}
      <Card elevation="xs" padding="none" className="mt-8 overflow-hidden">
        {problems === null && !error && (
          <div className="divide-y divide-line">
            <RowSkeleton />
            <RowSkeleton />
            <RowSkeleton />
            <RowSkeleton />
          </div>
        )}

        {problems && problems.length === 0 && (
          <div className="p-6">
            <EmptyState
              title="No problems here yet"
              description="This track is waiting for its first problem."
            />
          </div>
        )}

        {problems && problems.length > 0 && (
          <ul className="divide-y divide-line">
            {problems.map((problem) => {
              const isSolved = solvedIds.has(problem.id);

              return (
                <li key={problem.id}>
                  <Link
                    to={`/app/practice/${trackId}/${problem.id}`}
                    className="group flex items-center gap-4 px-5 py-4 transition-colors hover:bg-paper-sunken/50"
                  >
                    {/* Status: shape + color + label */}
                    {isSolved ? (
                      <CircleCheck
                        size={17}
                        aria-hidden="true"
                        className="shrink-0 text-[color:var(--ok)]"
                      />
                    ) : (
                      <CircleDashed
                        size={17}
                        aria-hidden="true"
                        className="shrink-0 text-ink-3"
                      />
                    )}

                    <span className="min-w-0 flex-1">
                      <span className="block truncate text-sm font-medium text-ink transition-colors group-hover:text-accent">
                        {problem.title}
                      </span>

                      <span className="sr-only">
                        {isSolved ? "Solved" : "Not solved yet"}
                      </span>
                    </span>

                    <Badge tone={DIFFICULTY_TONE[problem.difficulty]}>
                      {problem.difficulty}
                    </Badge>

                    <span
                      className={`
                        hidden w-24 text-right text-[13px] font-medium sm:block
                        ${isSolved ? "text-[color:var(--ok)]" : "text-ink-3"}
                      `}
                    >
                      {isSolved ? "Solved" : "Solve"}
                    </span>
                  </Link>
                </li>
              );
            })}
          </ul>
        )}
      </Card>

      {/* Honest note for non-executable tracks */}
      {track && !track.executable && (
        <p className="mt-4 flex items-center gap-1.5 text-xs text-ink-3">
          <CircleX size={13} aria-hidden="true" />
          Code execution for this language isn't available yet — you can
          read and plan, but not run.
        </p>
      )}
    </div>
  );
}
