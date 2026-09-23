import type { HTMLAttributes } from "react";

type SkeletonVariant = "text" | "card" | "avatar";

export interface SkeletonProps extends HTMLAttributes<HTMLDivElement> {
  /**
   * Shape to render:
   * - `text`: inline line, pass `className="w-3/4"` etc. for width.
   * - `card`: full-width rounded block.
   * - `avatar`: circle.
   *
   * @default "text"
   */
  variant?: SkeletonVariant;

  /** Height of a `text` line. */
  size?: "sm" | "md" | "lg";
}

const variantClasses: Record<SkeletonVariant, string> = {
  text: "h-3 rounded-md",
  card: "h-24 w-full rounded-2xl",
  avatar: "h-10 w-10 rounded-full",
};

const sizeClasses: Record<NonNullable<SkeletonProps["size"]>, string> = {
  sm: "h-2",
  md: "h-3",
  lg: "h-4",
};

/**
 * Pulsing loading placeholder.
 *
 * Reuses the `animate-pulse-slow` keyframe defined in
 * `tailwind.config.js` (opacity/scale pulse) — the same motion
 * language as the rest of the app.
 */
export function Skeleton({
  variant = "text",
  size = "md",
  className = "",
  ...rest
}: SkeletonProps) {
  const isText = variant === "text";

  return (
    <div
      aria-hidden="true"
      className={`
        animate-pulse-slow
        bg-white/[0.06]
        ${variantClasses[variant]}
        ${isText ? sizeClasses[size] : ""}
        ${className}
      `}
      {...rest}
    />
  );
}

/**
 * Convenience composition: a text block skeleton
 * (title line + two body lines).
 */
export function SkeletonText({ className = "" }: { className?: string }) {
  return (
    <div className={`space-y-2 ${className}`}>
      <Skeleton className="w-2/3" size="lg" />
      <Skeleton className="w-full" />
      <Skeleton className="w-5/6" />
    </div>
  );
}

/**
 * Convenience composition: a stat-card shaped skeleton
 * (small label line + big value line + caption line).
 */
export function SkeletonStatCard() {
  return (
    <div
      className="
        rounded-2xl
        border
        border-[color:var(--border-subtle)]
        bg-[color:var(--bg-panel)]
        p-6
      "
    >
      <Skeleton className="w-24" size="sm" />
      <Skeleton className="mt-4 h-8 w-16" />
      <Skeleton className="mt-3 w-32" size="sm" />
    </div>
  );
}

export default Skeleton;
