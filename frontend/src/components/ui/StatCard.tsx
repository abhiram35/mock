import type { ReactNode } from "react";

import Card from "./Card";

export interface StatCardProps {
  /**
   * Small mono label above the value, e.g. "TOTAL INTERVIEWS".
   */
  label: string;

  /** The headline number — string or number. */
  value: ReactNode;

  /** Optional one-line context below the value. */
  description?: string;

  /**
   * Optional icon or glyph rendered in a rounded slot.
   * Accepts any node (emoji, SVG, number badge).
   */
  icon?: ReactNode;

  /**
   * Optional trend delta, e.g. "+4" or "-2".
   * Positive deltas render green (--success), negative red (--error),
   * and neutral is the muted gray.
   */
  trend?: {
    value: string;
    direction: "up" | "down" | "neutral";
  };

  /** Extra classes merged onto the underlying Card shell. */
  className?: string;
}

/**
 * Summary stat tile built on the glass `Card`.
 *
 * Layout: optional icon · mono label · big value · description · trend.
 * The label/value/description utilities intentionally mirror the
 * dashboard's `.dashboard-stat-*` styles so the kit and the page
 * render identical output.
 */
export function StatCard({
  label,
  value,
  description,
  icon,
  trend,
  className = "",
}: StatCardProps) {
  return (
    <Card padding="md" className={className}>
      <div className="flex items-start justify-between gap-3">
        <span
          className="
            block
            font-mono
            text-[9px]
            uppercase
            tracking-[0.15em]
            text-[color:var(--text-muted)]
          "
        >
          {label}
        </span>

        {icon && (
          <span
            aria-hidden="true"
            className="
              flex
              h-8
              w-8
              shrink-0
              items-center
              justify-center
              rounded-lg
              bg-white/[0.05]
              text-sm
              text-[color:var(--accent-violet)]
            "
          >
            {icon}
          </span>
        )}
      </div>

      <div className="mt-4 flex items-baseline gap-2">
        <strong
          className="
            block
            font-display
            text-[38px]
            leading-none
            text-[color:var(--text-primary)]
          "
        >
          {value}
        </strong>

        {trend && (
          <span
            className={`
              font-mono
              text-xs
              ${
                trend.direction === "up"
                  ? "text-[color:var(--success)]"
                  : trend.direction === "down"
                    ? "text-[color:var(--error)]"
                    : "text-[color:var(--text-muted)]"
              }
            `}
          >
            {trend.direction === "up" ? "↑" : trend.direction === "down" ? "↓" : "•"}{" "}
            {trend.value}
          </span>
        )}
      </div>

      {description && (
        <span
          className="
            mt-2.5
            block
            text-xs
            text-[color:var(--text-muted)]
          "
        >
          {description}
        </span>
      )}
    </Card>
  );
}

export default StatCard;
