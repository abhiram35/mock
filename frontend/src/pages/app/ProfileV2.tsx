import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  Avatar,
  Badge,
  Button,
  Card,
  Skeleton,
} from "../../components/primitives";
import { getInterviews, type Interview } from "../../lib/api";

export default function ProfileV2() {
  const navigate = useNavigate();

  const [interviews, setInterviews] = useState<Interview[] | null>(null);

  const [error, setError] = useState<string | null>(null);

  const me = useMemo(() => {
    try {
      return JSON.parse(
        localStorage.getItem("user") ?? "{}",
      ) as {
        full_name?: string;
        email?: string;
        role?: string;
      };
    } catch {
      return {};
    }
  }, []);

  useEffect(() => {
    let cancelled = false;

    getInterviews()
      .then((data) => {
        if (!cancelled) {
          setInterviews(data);
        }
      })
      .catch(() => {
        if (!cancelled) {
          setError("Interview history didn't load. Retry when ready.");
        }
      });

    return () => {
      cancelled = true;
    };
  }, []);

  const completed = interviews?.filter(
    (interview) => interview.status === "completed",
  );

  const scores = (completed ?? [])
    .map((interview) => interview.overall_score)
    .filter((score): score is number => score !== null);

  const average =
    scores.length > 0
      ? scores.reduce((sum, score) => sum + score, 0) / scores.length
      : null;

  const best = scores.length > 0 ? Math.max(...scores) : null;

  function handleLogout() {
    localStorage.removeItem("access_token");

    localStorage.removeItem("user");

    navigate("/login");
  }

  return (
    <div className="mx-auto w-full max-w-3xl px-5 py-10 md:px-8">
      <header className="flex items-center gap-4">
        <Avatar
          name={me.full_name ?? "You"}
          className="h-14 w-14 text-lg"
        />

        <div className="min-w-0">
          <h1 className="display truncate text-2xl text-ink">
            {me.full_name ?? "You"}
          </h1>

          <p className="truncate text-sm text-ink-2">{me.email ?? ""}</p>
        </div>

        {me.role === "admin" && (
          <Badge tone="accent" className="ml-auto">
            Admin
          </Badge>
        )}
      </header>

      {error && (
        <Card padding="md" className="mt-8 border-[color:var(--bad)]">
          <p className="text-sm text-ink-2">{error}</p>

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

      <div className="mt-8 grid gap-4 sm:grid-cols-3">
        {interviews === null && !error ? (
          <>
            <Skeleton className="h-24 w-full" variant="block" />
            <Skeleton className="h-24 w-full" variant="block" />
            <Skeleton className="h-24 w-full" variant="block" />
          </>
        ) : (
          <>
            <Card padding="md">
              <p className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
                Interviews
              </p>

              <p className="display tnum mt-2 text-3xl text-ink">
                {interviews?.length ?? 0}
              </p>
            </Card>

            <Card padding="md">
              <p className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
                Average
              </p>

              <p className="display tnum mt-2 text-3xl text-ink">
                {average !== null ? Math.round(average) : "—"}
              </p>
            </Card>

            <Card padding="md">
              <p className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
                Best
              </p>

              <p className="display tnum mt-2 text-3xl text-ink">
                {best !== null ? Math.round(best) : "—"}
              </p>
            </Card>
          </>
        )}
      </div>

      <div className="mt-10 flex items-center justify-between border-t border-line pt-6">
        <p className="text-[13px] text-ink-3">
          Signed in as {me.email ?? "…"}
        </p>

        <Button variant="secondary" size="sm" onClick={handleLogout}>
          Sign out
        </Button>
      </div>
    </div>
  );
}
