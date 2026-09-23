import {
  CartesianGrid,
  Line,
  LineChart,
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

export interface ScoreTrendChartProps {
  /**
   * One point per completed, scored interview — chronological
   * (oldest first). Score comes from `Interview.overall_score`,
   * the label from `Interview.created_at`.
   */
  data: Array<{
    label: string;
    score: number;
    sessionId: number;
  }>;
}

/**
 * Score over time across completed interviews.
 * Series: signal.violet. Grid/axes use the token styles.
 */
export default function ScoreTrendChart({ data }: ScoreTrendChartProps) {
  const isAnimate = useChartAnimation();

  return (
    <div className="h-[260px] w-full">
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data} margin={{ top: 10, right: 12, bottom: 0, left: -18 }}>
          <CartesianGrid stroke={GRID_STROKE} vertical={false} />

          <XAxis
            dataKey="label"
            tick={AXIS_TICK}
            stroke={GRID_STROKE}
            tickLine={false}
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
            cursor={{ stroke: SIGNAL.violet, strokeOpacity: 0.3 }}
          />

          <Line
            type="monotone"
            dataKey="score"
            name="Score"
            stroke={SIGNAL.violet}
            strokeWidth={2}
            dot={{ r: 3, fill: SIGNAL.violet, strokeWidth: 0 }}
            activeDot={{ r: 5 }}
            isAnimationActive={isAnimate}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
