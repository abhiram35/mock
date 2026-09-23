import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { ArrowRight, Lock, Search } from "lucide-react";

import { Badge, Card, EmptyState, Kbd, Skeleton } from "../../components/primitives";
import { practiceClient } from "../../lib/practice/client";
import type { PracticeTrack } from "../../lib/practice/types";

function TrackCardSkeleton() {
  return (
    <Card padding="lg">
      <div className="flex items-center gap-2">
        <Skeleton className="h-2.5 w-2.5" variant="block" />
        <Skeleton className="h-3 w-24" />
      </div>

      <Skeleton className="mt-4 h-6 w-40" variant="block" />

      <Skeleton className="mt-2 h-4 w-56" />

      <Skeleton className="mt-6 h-2 w-full" />
    </Card>
  );
}

/**
 * Practice index: every track with its own accent mark and a real
 * problem count. Non-executable tracks are clearly labeled.
 */
export default function PracticeHome() {
  const [tracks, setTracks] = useState<PracticeTrack[] | null>(null);

  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    practiceClient
      .listTracks()
      .then(setTracks)
      .catch(() =>
        setError(
          "The practice library couldn't load. Check that the backend is running.",
        ),
      );
  }, []);

  return (
    <div className="mx-auto w-full max-w-5xl px-5 py-10 md:px-8">
      {/* Context header — one obvious identity per track, no identical cards */}
      <header className="max-w-2xl">
        <p className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
          Practice
        </p>

        <h1 className="display mt-2 text-3xl text-ink md:text-4xl">
          Learn the pattern, then solve.
        </h1>

        <p className="mt-3 text-[15px] leading-7 text-ink-2">
          Every problem walks five stages — understand, plan, code, verify,
          reflect — so you practice the method, not just the answer.
        </p>
      </header>

      {error && (
        <div className="mt-8 rounded-xl border border-line bg-paper-raised px-5 py-4">
          <p className="text-sm text-ink-2">{error}</p>
        </div>
      )}

      {!tracks && !error && (
        <div className="mt-10 grid gap-4 md:grid-cols-2">
          <TrackCardSkeleton />

          <TrackCardSkeleton />

          <TrackCardSkeleton />
        </div>
      )}

      {tracks && tracks.length === 0 && (
        <div className="mt-10">
          <EmptyState
            icon={<Search size={18} />}
            title="No problem tracks yet"
            description="Problems appear here once coding questions are seeded for a topic."
          />
        </div>
      )}

      {tracks && tracks.length > 0 && (
        <ul className="mt-10 grid gap-4 md:grid-cols-2">
          {tracks.map((track) => (
            <li key={track.id}>
              <Card
                as="article"
                interactive
                elevation="xs"
                padding="lg"
                className="h-full"
              >
                <Link
                  to={`/app/practice/${track.id}`}
                  className="flex h-full flex-col"
                >
                  <div className="flex items-center gap-2.5">
                    <span
                      aria-hidden="true"
                      className="subject-mark"
                      style={{ ["--mark" as string]: track.color }}
                    />

                    <span className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
                      {track.problemCount}{" "}
                      {track.problemCount === 1 ? "problem" : "problems"}
                    </span>

                    {!track.executable && (
                      <Badge tone="warn" icon={<Lock size={11} />}>
                        Soon
                      </Badge>
                    )}

                    <ArrowRight
                      size={15}
                      aria-hidden="true"
                      className="ml-auto text-ink-3 transition-transform duration-200 group-hover:translate-x-0.5"
                    />
                  </div>

                  <h2 className="display mt-4 text-2xl text-ink">
                    {track.name}
                  </h2>

                  <p className="mt-1.5 text-sm leading-6 text-ink-2">
                    {track.tagline}
                  </p>

                  <div className="mt-auto pt-5">
                    {track.executable ? (
                      <span className="text-[13px] font-medium text-accent">
                        Start solving
                      </span>
                    ) : (
                      <span className="text-[13px] text-ink-3">
                        Browsing only — runner coming soon
                      </span>
                    )}
                  </div>
                </Link>
              </Card>
            </li>
          ))}
        </ul>
      )}

      <p className="mt-8 flex items-center gap-2 text-xs text-ink-3">
        Tip: press <Kbd>⌘K</Kbd> to jump straight to any track.
      </p>
    </div>
  );
}
