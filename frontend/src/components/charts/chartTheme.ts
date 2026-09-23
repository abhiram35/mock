import { useReducedMotion } from "framer-motion";

/**
 * Shared recharts theming built on the design tokens:
 * series colors are signal.{violet,cyan,mint}, text uses the
 * --text-secondary / --text-muted vars, and surfaces are the
 * midnight glass panels.
 */

export const SIGNAL = {
  violet: "#8B5CF6",
  purple: "#A855F7",
  cyan: "#22D3EE",
  mint: "#2DD4BF",
} as const;

/** Semantic status hues (matches --success/--warning/--error). */
export const STATUS = {
  success: "#34d399",
  warning: "#fbbf24",
  error: "#fb7185",
} as const;

export const GRID_STROKE = "rgba(255, 255, 255, 0.06)";

export const AXIS_TICK = {
  fill: "var(--text-secondary)",
  fontSize: 11,
  fontFamily: "'JetBrains Mono', monospace",
} as const;

export const TOOLTIP_STYLE = {
  background: "rgba(17, 24, 39, 0.95)",
  border: "1px solid var(--border-subtle)",
  borderRadius: 12,
  color: "var(--text-primary)",
  fontSize: 12,
  boxShadow: "0 12px 30px rgba(0, 0, 0, 0.35)",
} as const;

export const TOOLTIP_LABEL_STYLE = {
  color: "var(--text-secondary)",
  marginBottom: 4,
} as const;

export const TOOLTIP_ITEM_STYLE = {
  color: "var(--text-primary)",
} as const;

/**
 * Recharts animation toggle that respects `prefers-reduced-motion`.
 */
export function useChartAnimation(): boolean {
  const reduceMotion = useReducedMotion();

  return !reduceMotion;
}
