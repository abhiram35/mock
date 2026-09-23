import type { Interview, Topic } from "../../lib/api";

import ScoreTrendChart from "./ScoreTrendChart";
import TopicStrengthChart from "./TopicStrengthChart";

import {
  buildScoreTrendData,
  buildTopicStrengthData,
} from "../../pages/dashboard/metrics";

export interface DashboardAnalyticsProps {
  /** All interviews for the user (any status). */
  interviews: Interview[];

  /** Topics from `getTopics()` for name resolution. */
  topics: Topic[];
}

/**
 * Dashboard analytics section: score trend + topic strength,
 * styled with the existing dashboard glass-section classes.
 *
 * Data is derived from real API fields only:
 * - `Interview.overall_score` / `Interview.created_at` / `Interview.topic_id`
 * - `Topic.name` from `getTopics()`
 */
export default function DashboardAnalytics({
  interviews,
  topics,
}: DashboardAnalyticsProps) {
  const scoreTrendData = buildScoreTrendData(interviews);

  const topicStrengthData = buildTopicStrengthData(interviews, topics);

  return (
    <div className="grid gap-5 lg:grid-cols-2">
      <section className="dashboard-section">
        <div className="dashboard-section-header">
          <div>
            <div className="dashboard-eyebrow">ANALYTICS</div>

            <h2>Score trend</h2>

            <p>Your overall score across completed interviews.</p>
          </div>
        </div>

        {scoreTrendData.length > 0 ? (
          <ScoreTrendChart data={scoreTrendData} />
        ) : (
          <p className="text-sm text-[color:var(--text-muted)]">
            Complete an interview to see your score trend.
          </p>
        )}
      </section>

      <section className="dashboard-section">
        <div className="dashboard-section-header">
          <div>
            <div className="dashboard-eyebrow">ANALYTICS</div>

            <h2>Topic strength</h2>

            <p>Average score by topic across completed interviews.</p>
          </div>
        </div>

        {topicStrengthData.length > 0 ? (
          <TopicStrengthChart data={topicStrengthData} />
        ) : (
          <p className="text-sm text-[color:var(--text-muted)]">
            Complete interviews in different topics to compare your
            strengths.
          </p>
        )}
      </section>
    </div>
  );
}
