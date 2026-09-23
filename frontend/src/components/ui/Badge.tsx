import type { HTMLAttributes } from "react";

type BadgeTone = "neutral" | "success" | "warning" | "error";

export interface BadgeProps extends HTMLAttributes<HTMLSpanElement> {
  /**
   * Semantic color of the pill.
   * - `success`: green — completed / passing states.
   * - `warning`: amber — in-progress / medium states.
   * - `error`: red — abandoned / failing states.
   * - `neutral`: default muted pill for informational labels.
   *
   * @default "neutral"
   */
  tone?: BadgeTone;

  /** When true, text renders uppercase with extra letter-spacing. */
  uppercase?: boolean;

  /** Prefix the label with a small status dot. */
  dot?: boolean;
}

/*
 * Backgrounds/borders are the semantic tokens (--success/--warning/--error)
 * rendered at low alpha via hex literals — opacity modifiers cannot be
 * applied to `var()` colors, and these mirror the alpha values already
 * used by the status styles in `index.css`.
 */
const toneClasses: Record<BadgeTone, string> = {
  neutral:
    "text-[color:var(--text-secondary)] bg-white/[0.05] border-[color:var(--border-subtle)]",
  success:
    "text-[color:var(--success)] bg-[#34d39914] border-[#34d39940]",
  warning:
    "text-[color:var(--warning)] bg-[#fbbf2414] border-[#fbbf2440]",
  error: "text-[color:var(--error)] bg-[#fb718514] border-[#fb718540]",
};

/**
 * Pill-shaped label for statuses and difficulty levels.
 *
 * Colors map to the semantic tokens `--success` / `--warning` /
 * `--error` defined in `index.css`.
 */
export function Badge({
  tone = "neutral",
  uppercase = false,
  dot = false,
  className = "",
  children,
  ...rest
}: BadgeProps) {
  return (
    <span
      className={`
        inline-flex
        items-center
        gap-1.5
        rounded-full
        border
        px-2.5
        py-1
        text-[10px]
        font-medium
        tracking-wide
        ${uppercase ? "uppercase tracking-[0.08em]" : ""}
        ${toneClasses[tone]}
        ${className}
      `}
      {...rest}
    >
      {dot && <span aria-hidden="true" className="h-1.5 w-1.5 rounded-full bg-current" />}

      {children}
    </span>
  );
}

export default Badge;
