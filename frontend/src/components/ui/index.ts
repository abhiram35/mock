/**
 * Shared UI kit.
 *
 * Every component is built exclusively on the design tokens
 * defined in `tailwind.config.js` and `src/index.css`:
 * - colors: midnight.{950,900,800,700}, signal.{violet,purple,cyan,mint}
 * - shadows: glow, glow-cyan
 * - animations: pulse-slow, float-slow, grid-move
 * - CSS vars: --bg-panel, --border-subtle, --border-active,
 *   --text-primary/secondary/muted, --success/--warning/--error
 */

export { Button, default as ButtonDefault } from "./Button";
export type { ButtonProps } from "./Button";

export { Card, default as CardDefault } from "./Card";
export type { CardProps } from "./Card";

export { Badge, default as BadgeDefault } from "./Badge";
export type { BadgeProps } from "./Badge";

export { StatCard, default as StatCardDefault } from "./StatCard";
export type { StatCardProps } from "./StatCard";

export {
  Skeleton,
  SkeletonText,
  SkeletonStatCard,
  default as SkeletonDefault,
} from "./Skeleton";
export type { SkeletonProps } from "./Skeleton";

export { Modal, default as ModalDefault } from "./Modal";
export type { ModalProps } from "./Modal";

export { EmptyState, default as EmptyStateDefault } from "./EmptyState";
export type { EmptyStateProps } from "./EmptyState";
