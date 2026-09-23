import type { Interview, Topic } from "../../lib/api";

import { formatDate } from "./utils";

export interface DashboardMetrics {
  /** Completed sessions only. */
  completedInterviews: Interview[];

  /** Mean overall score across completed sessions, or null. */
  averageScore: number | null;

  /** Highest overall score, or null. */
  bestScore: number | null;

  /** Score delta between the two most recent scored interviews, or null. */
  improvement: number | null;

  /** Completed + scored interviews, oldest first (for the trend chart). */
  performanceInterviews: Interview[];
}

/**
 * Pure derived-metrics computation for the dashboard.
 * Separated from the component so it can be unit tested.
 */
export function computeDashboardMetrics(
  interviews: Interview[],
): DashboardMetrics {
  const completedInterviews = interviews.filter(
    (interview) => interview.status === "completed",
  );

  const scores = completedInterviews
    .map((interview) => interview.overall_score)
    .filter((score): score is number => score !== null);

  const averageScore =
    scores.length > 0
      ? scores.reduce((sum, score) => sum + score, 0) / scores.length
      : null;

  const bestScore = scores.length > 0 ? Math.max(...scores) : null;

  const latestScore = scores.length > 0 ? scores[0] : null;

  const previousScore = scores.length > 1 ? scores[1] : null;

  const improvement =
    latestScore !== null && previousScore !== null
      ? latestScore - previousScore
      : null;

  const performanceInterviews = [...completedInterviews]
    .reverse()
    .filter((interview) => interview.overall_score !== null);

  return {
    completedInterviews,
    averageScore,
    bestScore,
    improvement,
    performanceInterviews,
  };
}

export interface ScoreTrendPoint {
  /** Short date label from `Interview.created_at`. */
  label: string;

  /** `Interview.overall_score`. */
  score: number;

  /** `Interview.id` — used for tooltip keys. */
  sessionId: number;
}

/**
 * Score-over-time series (oldest first) for the trend line chart.
 * Only completed sessions with a non-null `overall_score`.
 */
export function buildScoreTrendData(
  interviews: Interview[],
): ScoreTrendPoint[] {
  return [...interviews]
    .filter(
      (interview) =>
        interview.status === "completed" &&
        interview.overall_score !== null,
    )
    .sort(
      (a, b) =>
        new Date(a.created_at).getTime() - new Date(b.created_at).getTime(),
    )
    .map((interview) => ({
      label: formatDate(interview.created_at),
      score: interview.overall_score as number,
      sessionId: interview.id,
    }));
}

export interface TopicStrengthPoint {
  /** `Topic.name`. */
  topic: string;

  /** Mean `overall_score` of completed interviews in the topic. */
  averageScore: number;

  /** Number of completed interviews the average covers. */
  interviews: number;
}

/**
 * Average score per topic for the topic-strength chart.
 * Groups completed, scored interviews by `topic_id` and resolves
 * names via the `getTopics()` response.
 */
export function buildTopicStrengthData(
  interviews: Interview[],
  topics: Topic[],
): TopicStrengthPoint[] {
  const scoresByTopic = new Map<number, number[]>();

  interviews
    .filter(
      (interview) =>
        interview.status === "completed" &&
        interview.overall_score !== null,
    )
    .forEach((interview) => {
      const scores = scoresByTopic.get(interview.topic_id) ?? [];

      scores.push(interview.overall_score as number);

      scoresByTopic.set(interview.topic_id, scores);
    });

  return topics
    .map((topic) => {
      const scores = scoresByTopic.get(topic.id);

      if (!scores || scores.length === 0) {
        return null;
      }

      const sum = scores.reduce((total, score) => total + score, 0);

      return {
        topic: topic.name,
        averageScore: sum / scores.length,
        interviews: scores.length,
      };
    })
    .filter((point): point is TopicStrengthPoint => point !== null);
}
