import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  getInterviews,
  getTopics,
  type Interview,
  type Topic,
} from "../lib/api";

import Button from "../components/ui/Button";
import Skeleton from "../components/ui/Skeleton";

import DashboardAnalytics from "../components/charts/DashboardAnalytics";

import DashboardHeader from "./dashboard/DashboardHeader";
import PerformanceTrend from "./dashboard/PerformanceTrend";
import RecentInterviewsList from "./dashboard/RecentInterviewsList";
import StatsOverview from "./dashboard/StatsOverview";
import { computeDashboardMetrics } from "./dashboard/metrics";

export default function Dashboard() {
  const navigate = useNavigate();

  const [interviews, setInterviews] = useState<Interview[]>([]);

  const [topics, setTopics] = useState<Topic[]>([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadDashboard() {
      try {
        setLoading(true);
        setError(null);

        const [interviewData, topicData] = await Promise.all([
          getInterviews(),
          getTopics(),
        ]);

        const sortedInterviews = [...interviewData].sort(
          (a, b) =>
            new Date(b.created_at).getTime() - new Date(a.created_at).getTime(),
        );

        setInterviews(sortedInterviews);
        setTopics(topicData);
      } catch (err) {
        setError(
          err instanceof Error ? err.message : "Failed to load dashboard.",
        );
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  const topicNames = useMemo(() => {
    const map = new Map<number, string>();

    topics.forEach((topic) => {
      map.set(topic.id, topic.name);
    });

    return map;
  }, [topics]);

  const metrics = useMemo(
    () => computeDashboardMetrics(interviews),
    [interviews],
  );

  if (loading) {
    return (
      <div className="dashboard-page">
        <div className="dashboard-container">
          {/* Header skeleton */}
          <div className="dashboard-header">
            <div>
              <Skeleton className="w-36" size="sm" />

              <Skeleton className="mt-4 h-10 w-80 max-w-full" size="lg" />

              <Skeleton className="mt-4 w-96 max-w-full" />
            </div>

            <Skeleton className="h-12 w-48 rounded-xl" variant="card" />
          </div>

          {/* Stat card skeletons (matches .dashboard-overview grid) */}
          <div className="dashboard-overview">
            {[0, 1, 2, 3].map((index) => (
              <div
                className="dashboard-stat-card"
                key={index}
                aria-hidden="true"
              >
                <Skeleton className="w-28" size="sm" />

                <Skeleton className="mt-4 h-9 w-16" size="lg" />

                <Skeleton className="mt-3 w-36" size="sm" />
              </div>
            ))}
          </div>

          {/* History section skeleton (matches .dashboard-section) */}
          <div className="dashboard-section" aria-hidden="true">
            <Skeleton className="w-48" size="lg" />

            <div className="mt-8 flex flex-col gap-3">
              {[0, 1, 2].map((index) => (
                <Skeleton key={index} variant="card" className="h-24" />
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="dashboard-page">
        <div className="dashboard-container">
          <div className="dashboard-error">
            <h2>Unable to load dashboard</h2>

            <p>{error}</p>

            <Button
              variant="secondary"
              onClick={() => window.location.reload()}
            >
              Try Again
            </Button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="dashboard-page">
      <div className="dashboard-container">
        <DashboardHeader onStartInterview={() => navigate("/interviews/new")} />

        <StatsOverview
          totalInterviews={interviews.length}
          completedCount={metrics.completedInterviews.length}
          averageScore={metrics.averageScore}
          bestScore={metrics.bestScore}
        />

        <DashboardAnalytics interviews={interviews} topics={topics} />

        {metrics.performanceInterviews.length > 0 && (
          <PerformanceTrend
            performanceInterviews={metrics.performanceInterviews}
            improvement={metrics.improvement}
          />
        )}

        <RecentInterviewsList
          interviews={interviews}
          topicNames={topicNames}
          onViewResult={(sessionId) => navigate(`/interviews/${sessionId}/result`)}
          onStartFirstInterview={() => navigate("/interviews/new")}
        />
      </div>
    </div>
  );
}
