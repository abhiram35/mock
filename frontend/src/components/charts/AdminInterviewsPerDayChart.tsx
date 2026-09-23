import {
  Area,
  AreaChart,
  CartesianGrid,
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

export interface AdminInterviewsPerDayChartProps {
  /**
   * One row per day (ascending): interviews started that day,
   * derived from `AdminInterviewResponse.created_at` of
   * `GET /admin/interviews`.
   */
  data: Array<{
    day: string;
    interviews: number;
  }>;
}

/**
 * Platform-wide interviews started per day.
 * Series: signal.cyan.
 */
export default function AdminInterviewsPerDayChart({
  data,
}: AdminInterviewsPerDayChartProps) {
  const isAnimate = useChartAnimation();

  return (
    <div className="h-[240px] w-full">
      <ResponsiveContainer width="100%" height="100%">
        <AreaChart data={data} margin={{ top: 10, right: 12, bottom: 0, left: -22 }}>
          <defs>
            <linearGradient id="adminInterviewsFill" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor={SIGNAL.cyan} stopOpacity={0.35} />
              <stop offset="100%" stopColor={SIGNAL.cyan} stopOpacity={0.02} />
            </linearGradient>
          </defs>

          <CartesianGrid stroke={GRID_STROKE} vertical={false} />

          <XAxis
            dataKey="day"
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
            cursor={{ stroke: SIGNAL.cyan, strokeOpacity: 0.3 }}
          />

          <Area
            type="monotone"
            dataKey="interviews"
            name="Interviews"
            stroke={SIGNAL.cyan}
            strokeWidth={2}
            fill="url(#adminInterviewsFill)"
            isAnimationActive={isAnimate}
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}
