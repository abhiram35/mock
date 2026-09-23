import type { HTMLAttributes, ReactNode } from "react";

type BadgeTone = "neutral" | "ok" | "warn" | "bad" | "info" | "accent";

export interface BadgeProps extends HTMLAttributes<HTMLSpanElement> {
  /** Semantic tone; fills use the token soft values. */
  tone?: BadgeTone;

  /** Small leading dot for status badges. */
  dot?: boolean;

  /** Leading icon slot (Lucide). */
  icon?: ReactNode;
}

const tones: Record<BadgeTone, string> = {
  neutral: "bg-paper-sunken text-ink-2 border-line",
  ok: "bg-[color:var(--ok-soft)] text-[color:var(--ok)] border-transparent",
  warn: "bg-[color:var(--warn-soft)] text-[color:var(--warn)] border-transparent",
  bad: "bg-[color:var(--bad-soft)] text-[color:var(--bad)] border-transparent",
  info: "bg-[color:var(--info-soft)] text-[color:var(--info)] border-transparent",
  accent: "bg-accent-soft text-accent border-transparent",
};

/**
 * Status/difficulty pill. Always pair with a visible text label —
 * color alone never carries meaning (a11y rule).
 */
export function Badge({
  tone = "neutral",
  dot = false,
  icon,
  className = "",
  children,
  ...rest
}: BadgeProps) {
  return (
    <span
      className={`
        inline-flex items-center gap-1.5 rounded-full border
        px-2.5 py-0.5 text-[11px] font-medium leading-5
        ${tones[tone]}
        ${className}
      `}
      {...rest}
    >
      {dot && (
        <span
          aria-hidden="true"
          className="h-1.5 w-1.5 rounded-full bg-current"
        />
      )}

      {icon}

      {children}
    </span>
  );
}

export default Badge;
