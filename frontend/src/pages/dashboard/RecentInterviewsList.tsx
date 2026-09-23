import { motion } from "framer-motion";

import type { Interview } from "../../lib/api";

import { Badge, Card } from "../../components/ui";
import {
  onceInView,
  useStaggerContainer,
  useStaggerItem,
} from "../../components/motion/transitions";

import {
  formatDateTime,
  getDifficultyLabel,
  getScoreClass,
  getStatusClass,
  getStatusLabel,
  getStatusTone,
} from "./utils";

export interface RecentInterviewsListProps {
  /** All interviews, newest first (already sorted by the page). */
  interviews: Interview[];

  /** Resolved topic names by topic id. */
  topicNames: Map<number, string>;

  /** Navigates to the full result report for a session. */
  onViewResult: (sessionId: number) => void;

  /** Starts a new interview (used by the empty state CTA). */
  onStartFirstInterview: () => void;
}

/**
 * Interview history section: list of session cards with status,
 * difficulty progression and score — plus the empty state.
 */
export default function RecentInterviewsList({
  interviews,
  topicNames,
  onViewResult,
  onStartFirstInterview,
}: RecentInterviewsListProps) {
  const container = useStaggerContainer();

  const item = useStaggerItem();

  return (
    <Card as="section" padding="none" className="dashboard-section backdrop-blur-none">
      <div className="dashboard-section-header">
        <div>
          <div className="dashboard-eyebrow">INTERVIEW HISTORY</div>

          <h2>Your interviews</h2>

          <p>Review every interview in chronological order.</p>
        </div>

        <span className="dashboard-count">
          {interviews.length}{" "}
          {interviews.length === 1 ? "interview" : "interviews"}
        </span>
      </div>

      {interviews.length === 0 ? (
        <div className="dashboard-empty">
          <div className="dashboard-empty-icon">+</div>

          <h3>No interviews yet</h3>

          <p>
            Start your first mock interview to begin building your
            performance history.
          </p>

          <button
            className="dashboard-primary-button"
            onClick={onStartFirstInterview}
          >
            Start Your First Interview
            <span>→</span>
          </button>
        </div>
      ) : (
        <motion.div
          className="dashboard-interview-list"
          variants={container}
          initial="hidden"
          whileInView="show"
          viewport={onceInView}
        >
          {interviews.map((interview, index) => {
            const topicName =
              topicNames.get(interview.topic_id) ||
              `Topic #${interview.topic_id}`;

            const score = interview.overall_score;

            return (
              <motion.div variants={item} key={interview.id}>
              <Card
                as="article"
                padding="none"
                className="dashboard-interview-card backdrop-blur-none"
              >
                <div className="dashboard-interview-number">
                  #{interviews.length - index}
                </div>

                <div className="dashboard-interview-main">
                  <div className="dashboard-interview-top">
                    <div>
                      <h3>{topicName} Interview</h3>

                      <p>{formatDateTime(interview.created_at)}</p>
                    </div>

                    <Badge
                      tone={getStatusTone(interview.status)}
                      uppercase
                      className={getStatusClass(interview.status)}
                    >
                      {getStatusLabel(interview.status)}
                    </Badge>
                  </div>

                  <div className="dashboard-interview-meta">
                    <div>
                      <span>STARTING</span>

                      <strong>
                        {getDifficultyLabel(interview.starting_difficulty)}
                      </strong>
                    </div>

                    <div>
                      <span>FINAL</span>

                      <strong>
                        {getDifficultyLabel(interview.current_difficulty)}
                      </strong>
                    </div>

                    <div>
                      <span>QUESTIONS</span>

                      <strong>{interview.total_questions}</strong>
                    </div>

                    <div>
                      <span>PROGRESS</span>

                      <strong>
                        {interview.current_question_number}/
                        {interview.total_questions}
                      </strong>
                    </div>
                  </div>
                </div>

                <div className="dashboard-interview-score">
                  <span>SCORE</span>

                  <strong className={getScoreClass(score)}>
                    {score !== null ? score.toFixed(0) : "—"}
                  </strong>

                  {interview.status === "completed" && (
                    <button
                      className="dashboard-view-button"
                      onClick={() => onViewResult(interview.id)}
                    >
                      View Full Report
                      <span>→</span>
                    </button>
                  )}
                </div>
              </Card>
              </motion.div>
            );
          })}
        </motion.div>
      )}
    </Card>
  );
}
