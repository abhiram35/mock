import {
  Bar,
  BarChart,
  CartesianGrid,
  Legend,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

import {
  AXIS_TICK,
  GRID_STROKE,
  STATUS,
  TOOLTIP_ITEM_STYLE,
  TOOLTIP_LABEL_STYLE,
  TOOLTIP_STYLE,
  useChartAnimation,
} from "./chartTheme";

export interface AdminDifficultyChartProps {
  /**
   * Counts of sessions per final difficulty — derived from
   * `AdminInterviewResponse.final_difficulty` of
   * `GET /admin/interviews` (always exactly one row).
   */
  data: Array<{
    bucket: string;
    easy: number;
    medium: number;
    hard: number;
  }>;
}

const DIFFICULTY_COLORS: Record<string, string> = {
  easy: STATUS.success,
  medium: STATUS.warning,
  hard: STATUS.error,
};

/**
 * Difficulty distribution of interview sessions (stacked bars,
 * one segment per final difficulty level).
 */
export default function AdminDifficultyChart({
  data,
}: AdminDifficultyChartProps) {
  const isAnimate = useChartAnimation();

  return (
    <div className="h-[240px] w-full">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data} margin={{ top: 10, right: 12, bottom: 0, left: -22 }}>
          <CartesianGrid stroke={GRID_STROKE} vertical={false} />

          <XAxis
            dataKey="bucket"
            tick={AXIS_TICK}
            stroke={GRID_STROKE}
            tickLine={false}
          />

          <YAxis
            allowDecimals={false}
            tick={AXIS_TICK}
            stroke={GRID_STROKE}
            tickLine={false}
          />

          <Tooltip
            contentStyle={TOOLTIP_STYLE}
            labelStyle={TOOLTIP_LABEL_STYLE}
            itemStyle={TOOLTIP_ITEM_STYLE}
            cursor={{ fill: "rgba(139, 92, 246, 0.08)" }}
          />

          <Legend
            wrapperStyle={{
              color: "var(--text-secondary)",
              fontSize: 11,
              fontFamily: "'JetBrains Mono', monospace",
            }}
          />

          <Bar
            dataKey="easy"
            stackId="difficulty"
            fill={DIFFICULTY_COLORS.easy}
            maxBarSize={44}
            radius={[0, 0, 0, 0]}
            isAnimationActive={isAnimate}
          />

          <Bar
            dataKey="medium"
            stackId="difficulty"
            fill={DIFFICULTY_COLORS.medium}
            maxBarSize={44}
            isAnimationActive={isAnimate}
          />

          <Bar
            dataKey="hard"
            stackId="difficulty"
            fill={DIFFICULTY_COLORS.hard}
            maxBarSize={44}
            radius={[6, 6, 0, 0]}
            isAnimationActive={isAnimate}
          />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
