import type { HTMLAttributes, ReactNode } from "react";

import Button from "./Button";

/* =========================================================
   SKELETON — content-shaped shimmer
   ========================================================= */

export interface SkeletonProps extends HTMLAttributes<HTMLDivElement> {
  variant?: "line" | "block" | "circle";
}

/** Content-shaped placeholder; size it with className. */
export function Skeleton({
  variant = "line",
  className = "",
  ...rest
}: SkeletonProps) {
  const shape =
    variant === "circle"
      ? "rounded-full"
      : variant === "block"
        ? "rounded-xl"
        : "rounded-md";

  return (
    <div
      aria-hidden="true"
      className={`
        animate-pulse bg-paper-sunken
        ${shape} ${className}
      `}
      {...rest}
    />
  );
}

/* =========================================================
   PROGRESS — thin editorial bar
   ========================================================= */

export function Progress({
  value,
  max = 100,
  label,
  className = "",
}: {
  value: number;
  max?: number;
  /** Accessible name, e.g. "Track progress". */
  label: string;
  className?: string;
}) {
  const pct = Math.max(0, Math.min(100, (value / max) * 100));

  return (
    <div
      role="progressbar"
      aria-label={label}
      aria-valuemin={0}
      aria-valuemax={max}
      aria-valuenow={Math.round(pct)}
      className={`h-1.5 w-full overflow-hidden rounded-full bg-paper-sunken ${className}`}
    >
      <div
        className="h-full rounded-full bg-accent transition-[width] duration-500"
        style={{ width: `${pct}%` }}
      />
    </div>
  );
}

/* =========================================================
   AVATAR — initials, quiet
   ========================================================= */

export function Avatar({
  name,
  className = "",
}: {
  name: string;
  className?: string;
}) {
  const initials = name
    .trim()
    .split(/\s+/)
    .map((part) => part.charAt(0))
    .slice(0, 2)
    .join("")
    .toUpperCase();

  return (
    <span
      aria-hidden="true"
      className={`
        flex h-8 w-8 shrink-0 items-center justify-center rounded-full
        bg-accent-soft font-sans text-xs font-semibold text-accent
        ${className}
      `}
    >
      {initials}
    </span>
  );
}

/* =========================================================
   TOOLTIP (CSS-only, hover/focus)
   ========================================================= */

export function Tooltip({
  content,
  children,
  side = "top",
}: {
  content: ReactNode;
  children: ReactNode;
  side?: "top" | "bottom";
}) {
  const position =
    side === "top"
      ? "bottom-[calc(100%+6px)] left-1/2 -translate-x-1/2"
      : "top-[calc(100%+6px)] left-1/2 -translate-x-1/2";

  return (
    <span className="group/tt relative inline-flex">
      {children}

      <span
        role="tooltip"
        className={`
          pointer-events-none absolute z-40 whitespace-nowrap
          rounded-md border border-line bg-paper-raised px-2 py-1
          text-xs text-ink-2 opacity-0 shadow-sm2
          transition-opacity duration-100
          group-hover/tt:opacity-100 group-focus-within/tt:opacity-100
          ${position}
        `}
      >
        {content}
      </span>
    </span>
  );
}

/* =========================================================
   KBD — keyboard hint
   ========================================================= */

export function Kbd({ children }: { children: ReactNode }) {
  return (
    <kbd
      className="
        inline-flex h-5 min-w-5 items-center justify-center rounded
        border border-line bg-paper-sunken px-1.5
        font-mono text-[10px] font-medium text-ink-2
      "
    >
      {children}
    </kbd>
  );
}

/* =========================================================
   EMPTY STATE — specific, with one next action
   ========================================================= */

export interface EmptyStateProps {
  icon?: ReactNode;
  title: string;
  description?: string;
  action?: { label: string; onClick: () => void };
}

export function EmptyState({
  icon,
  title,
  description,
  action,
}: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center rounded-xl border border-dashed border-line-strong px-8 py-14 text-center">
      {icon && (
        <span
          aria-hidden="true"
          className="mb-4 flex h-10 w-10 items-center justify-center rounded-lg bg-accent-soft text-accent"
        >
          {icon}
        </span>
      )}

      <h3 className="display text-lg text-ink">{title}</h3>

      {description && (
        <p className="mt-2 max-w-sm text-sm leading-6 text-ink-2">
          {description}
        </p>
      )}

      {action && (
        <div className="mt-5">
          <Button size="sm" onClick={action.onClick}>
            {action.label}
          </Button>
        </div>
      )}
    </div>
  );
}
