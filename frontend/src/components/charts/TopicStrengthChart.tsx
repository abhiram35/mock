import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

import {
  AXIS_TICK,
  GRID_STROKE,
  SIGNAL,
  TOOLTIP_ITEM_STYLE,
  TOOLTIP_LABEL_STYLE,
  TOOLTIP_STYLE,
  useChartAnimation,
} from "./chartTheme";

export interface TopicStrengthChartProps {
  /**
   * One row per topic: average overall_score of completed
   * interviews in that topic, plus the count they're averaged over.
   * Topic names come from `getTopics()`; scores from
   * `Interview.overall_score` grouped by `Interview.topic_id`.
   */
  data: Array<{
    topic: string;
    averageScore: number;
    interviews: number;
  }>;
}

const SERIES_COLORS = [SIGNAL.violet, SIGNAL.cyan, SIGNAL.mint, SIGNAL.purple];

/**
 * Average score by topic — the "topic strength breakdown".
 * Bars cycle through the signal palette.
 */
export default function TopicStrengthChart({
  data,
}: TopicStrengthChartProps) {
  const isAnimate = useChartAnimation();

  return (
    <div className="h-[260px] w-full">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data} margin={{ top: 10, right: 12, bottom: 0, left: -18 }}>
          <CartesianGrid stroke={GRID_STROKE} vertical={false} />

          <XAxis
            dataKey="topic"
            tick={AXIS_TICK}
            stroke={GRID_STROKE}
            tickLine={false}
            interval={0}
            angle={data.length > 3 ? -12 : 0}
            height={data.length > 3 ? 40 : 30}
          />

          <YAxis
            domain={[0, 100]}
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

          <Bar
            dataKey="averageScore"
            name="Avg score"
            radius={[6, 6, 0, 0]}
            maxBarSize={44}
            isAnimationActive={isAnimate}
          >
            {data.map((entry, index) => (
              <Cell
                key={entry.topic}
                fill={SERIES_COLORS[index % SERIES_COLORS.length]}
              />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
