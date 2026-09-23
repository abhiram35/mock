import type { Interview } from "../../lib/api";

import { formatDate } from "./utils";

export interface PerformanceTrendProps {
  /** Completed, scored interviews in chronological order. */
  performanceInterviews: Interview[];

  /** Score delta vs the previous interview, or null. */
  improvement: number | null;
}

/**
 * "Performance over time" section — the per-interview score bar
 * chart with the improvement indicator.
 */
export default function PerformanceTrend({
  performanceInterviews,
  improvement,
}: PerformanceTrendProps) {
  return (
    <section className="dashboard-section">
      <div className="dashboard-section-header">
        <div>
          <div className="dashboard-eyebrow">PROGRESS</div>

          <h2>Performance over time</h2>

          <p>Your interview scores across completed sessions.</p>
        </div>

        {improvement !== null && (
          <div
            className={
              improvement >= 0
                ? "dashboard-improvement dashboard-improvement-positive"
                : "dashboard-improvement dashboard-improvement-negative"
            }
          >
            {improvement >= 0 ? "↑" : "↓"} {Math.abs(improvement).toFixed(0)}{" "}
            points vs previous
          </div>
        )}
      </div>

      <div className="dashboard-chart">
        {performanceInterviews.map((interview, index) => {
          const score = interview.overall_score ?? 0;

          return (
            <div className="dashboard-chart-item" key={interview.id}>
              <div className="dashboard-chart-value">{score.toFixed(0)}</div>

              <div className="dashboard-chart-track">
                <div
                  className="dashboard-chart-bar"
                  style={{
                    height: `${Math.max(score, 5)}%`,
                  }}
                />
              </div>

              <div className="dashboard-chart-label">#{index + 1}</div>

              <div className="dashboard-chart-date">
                {formatDate(interview.created_at)}
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}
