import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../../api/axios";
import { isAxiosError } from "axios";
import { logout } from "../../api/auth";

import { SkeletonStatCard } from "../../components/ui/Skeleton";
import AdminInterviewsPerDayChart from "../../components/charts/AdminInterviewsPerDayChart";
import AdminDifficultyChart from "../../components/charts/AdminDifficultyChart";

interface DashboardStats {
  total_users: number;
  total_interviews: number;
  completed_interviews: number;
  in_progress_interviews: number;
  abandoned_interviews: number;
  average_interview_score: number | null;
}

/** Subset of `AdminInterviewResponse` (GET /admin/interviews). */
interface AdminInterview {
  session_id: number;
  topic_name: string;
  final_difficulty: "easy" | "medium" | "hard";
  status: "in_progress" | "completed" | "abandoned";
  overall_score: number | null;
  created_at: string;
}

function dayLabel(date: Date): string {
  return date.toLocaleDateString(undefined, {
    day: "numeric",
    month: "short",
  });
}

/** Last `days` days (ascending) with per-day interview counts. */
function buildInterviewsPerDay(
  interviews: AdminInterview[],
  days: number,
): Array<{ day: string; interviews: number }> {
  const buckets: Array<{ key: string; label: string; count: number }> = [];

  const today = new Date();

  for (let offset = days - 1; offset >= 0; offset -= 1) {
    const day = new Date(today);
    day.setDate(today.getDate() - offset);

    const key = day.toISOString().slice(0, 10);

    buckets.push({ key, label: dayLabel(day), count: 0 });
  }

  const byKey = new Map(buckets.map((bucket) => [bucket.key, bucket]));

  interviews.forEach((interview) => {
    const key = new Date(interview.created_at).toISOString().slice(0, 10);

    const bucket = byKey.get(key);

    if (bucket) {
      bucket.count += 1;
    }
  });

  return buckets.map((bucket) => ({
    day: bucket.label,
    interviews: bucket.count,
  }));
}

/** Session counts per final difficulty level. */
function buildDifficultyDistribution(interviews: AdminInterview[]) {
  const counts = { easy: 0, medium: 0, hard: 0 };

  interviews.forEach((interview) => {
    counts[interview.final_difficulty] += 1;
  });

  return [{ bucket: "Sessions", ...counts }];
}

export default function AdminDashboard() {
  const navigate = useNavigate();

  const [stats, setStats] = useState<DashboardStats | null>(null);

  const [interviews, setInterviews] = useState<AdminInterview[]>([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadDashboard() {
      try {
        setLoading(true);
        setError(null);

        const [statsResponse, interviewsResponse] = await Promise.all([
          api.get<DashboardStats>("/admin/dashboard"),
          api.get<AdminInterview[]>("/admin/interviews"),
        ]);

        setStats(statsResponse.data);
        setInterviews(interviewsResponse.data);
      } catch (err) {
        setError(
          isAxiosError(err)
            ? err.response?.data?.detail ?? "Failed to load admin dashboard."
            : "Failed to load admin dashboard.",
        );
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  function handleLogout() {
    logout();
    navigate("/login");
  }

  const interviewsPerDay = useMemo(
    () => buildInterviewsPerDay(interviews, 14),
    [interviews],
  );

  const difficultyDistribution = useMemo(
    () => buildDifficultyDistribution(interviews),
    [interviews],
  );

  const cards = [
    {
      title: "Total Users",
      value: stats?.total_users ?? 0,
    },
    {
      title: "Total Interviews",
      value: stats?.total_interviews ?? 0,
    },
    {
      title: "Completed",
      value: stats?.completed_interviews ?? 0,
    },
    {
      title: "In Progress",
      value: stats?.in_progress_interviews ?? 0,
    },
    {
      title: "Abandoned",
      value: stats?.abandoned_interviews ?? 0,
    },
    {
      title: "Average Score",
      value:
        stats?.average_interview_score !== null &&
        stats?.average_interview_score !== undefined
          ? `${stats.average_interview_score}/100`
          : "—",
    },
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <nav className="border-b border-slate-800">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-5">
          <div>
            <h1 className="font-bold">AI Mock Interview</h1>

            <p className="text-xs text-slate-500">Administrator</p>
          </div>

          <button
            onClick={handleLogout}
            className="text-sm text-slate-400 hover:text-white"
          >
            Logout
          </button>
        </div>
      </nav>

      <main className="mx-auto max-w-7xl px-6 py-10">
        <h2 className="text-4xl font-bold">Admin Dashboard</h2>

        <p className="mt-2 text-slate-400">
          Overview of the interview platform.
        </p>

        {error && (
          <div
            role="alert"
            className="mt-8 rounded-2xl border border-rose-400/20 bg-rose-400/[0.05] px-5 py-4"
          >
            <p className="text-sm text-rose-200">{error}</p>

            <button
              type="button"
              onClick={() => window.location.reload()}
              className="mt-3 rounded-lg border border-rose-400/30 px-4 py-2 text-xs font-semibold text-rose-100 transition hover:bg-rose-400/10"
            >
              Try Again
            </button>
          </div>
        )}

        {loading ? (
          <div className="mt-10 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {cards.map((card) => (
              <SkeletonStatCard key={card.title} />
            ))}
          </div>
        ) : (
          !error && (
            <>
              <div className="mt-10 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
                {cards.map((card) => (
                  <div
                    key={card.title}
                    className="rounded-2xl border border-slate-800 bg-slate-900 p-6"
                  >
                    <p className="text-sm text-slate-400">{card.title}</p>

                    <p className="mt-3 text-3xl font-bold">{card.value}</p>
                  </div>
                ))}
              </div>

              {/* ===============================================
                  PLATFORM ANALYTICS
              ================================================ */}

              <section className="mt-12">
                <h3 className="text-lg font-semibold">Interview activity</h3>

                <p className="mt-1 text-sm text-slate-400">
                  Sessions started per day over the last two weeks.
                </p>

                <div className="mt-5 rounded-2xl border border-slate-800 bg-slate-900 p-5">
                  <AdminInterviewsPerDayChart data={interviewsPerDay} />
                </div>
              </section>

              <section className="mt-10">
                <h3 className="text-lg font-semibold">
                  Difficulty distribution
                </h3>

                <p className="mt-1 text-sm text-slate-400">
                  Final difficulty reached by interview sessions.
                </p>

                <div className="mt-5 rounded-2xl border border-slate-800 bg-slate-900 p-5">
                  <AdminDifficultyChart data={difficultyDistribution} />
                </div>
              </section>
            </>
          )
        )}

        <div className="mt-10 grid gap-5 md:grid-cols-2 lg:grid-cols-4">
          <button
            onClick={() => navigate("/admin/users")}
            className="rounded-xl border border-slate-800 bg-slate-900 p-5 text-left hover:border-blue-500"
          >
            <h3 className="font-semibold">Users</h3>
            <p className="mt-1 text-sm text-slate-400">
              Manage application users.
            </p>
          </button>

          <button
            onClick={() => navigate("/admin/topics")}
            className="rounded-xl border border-slate-800 bg-slate-900 p-5 text-left hover:border-blue-500"
          >
            <h3 className="font-semibold">Topics</h3>
            <p className="mt-1 text-sm text-slate-400">
              Manage interview topics.
            </p>
          </button>

          <button
            onClick={() => navigate("/admin/questions")}
            className="rounded-xl border border-slate-800 bg-slate-900 p-5 text-left hover:border-blue-500"
          >
            <h3 className="font-semibold">Questions</h3>
            <p className="mt-1 text-sm text-slate-400">
              Manage interview questions.
            </p>
          </button>

          <button
            onClick={() => navigate("/admin/interviews")}
            className="rounded-xl border border-slate-800 bg-slate-900 p-5 text-left hover:border-blue-500"
          >
            <h3 className="font-semibold">Interviews</h3>
            <p className="mt-1 text-sm text-slate-400">
              Review candidate interviews.
            </p>
          </button>
        </div>
      </main>
    </div>
  );
}
