import { motion } from "framer-motion";

import { StatCard } from "../../components/ui";

import { onceInView, useStaggerContainer, useStaggerItem } from "../../components/motion/transitions";

export interface StatsOverviewProps {
  /** Total number of interview sessions for the user. */
  totalInterviews: number;

  /** Sessions with status "completed". */
  completedCount: number;

  /** Mean overall score across completed sessions, or null. */
  averageScore: number | null;

  /** Highest overall score, or null. */
  bestScore: number | null;
}

/**
 * The four summary stat tiles at the top of the dashboard.
 * Rendered with the shared `StatCard` kit component.
 */
export default function StatsOverview({
  totalInterviews,
  completedCount,
  averageScore,
  bestScore,
}: StatsOverviewProps) {
  const container = useStaggerContainer();

  const item = useStaggerItem();

  return (
    <motion.section
      className="dashboard-overview"
      variants={container}
      initial="hidden"
      whileInView="show"
      viewport={onceInView}
    >
      <motion.div variants={item}>
        <StatCard
          label="TOTAL INTERVIEWS"
          value={totalInterviews}
          description="All interview sessions"
        />
      </motion.div>

      <motion.div variants={item}>
        <StatCard
          label="COMPLETED"
          value={completedCount}
          description="Successfully completed"
        />
      </motion.div>

      <motion.div variants={item}>
        <StatCard
          label="AVERAGE SCORE"
          value={averageScore !== null ? `${averageScore.toFixed(0)}` : "—"}
          description="Across completed interviews"
        />
      </motion.div>

      <motion.div variants={item}>
        <StatCard
          label="BEST SCORE"
          value={bestScore !== null ? `${bestScore.toFixed(0)}` : "—"}
          description="Your highest performance"
        />
      </motion.div>
    </motion.section>
  );
}
