import { forwardRef, type HTMLAttributes } from "react";

type CardPadding = "none" | "sm" | "md" | "lg";

type CardTag = "div" | "article" | "section";

export interface CardProps extends HTMLAttributes<HTMLDivElement> {
  /**
   * Padding scale inside the card.
   * - `none`: no padding (useful for full-bleed content).
   * - `sm` / `md` / `lg`: increasing padding.
   *
   * @default "md"
   */
  padding?: CardPadding;

  /**
   * When true the card responds to hover: a subtle lift plus a
   * brighter, violet-tinted border. Intended for clickable cards.
   *
   * @default false
   */
  hoverable?: boolean;

  /**
   * Renders as a `<button>` so keyboard/AT users can activate it.
   * Only allowed when `onClick` is provided.
   */
  as?: CardTag;

  /**
   * When true, adds a subtle hover lift (translateY(-2px)) and a
   * violet border-active glow transition. Pure CSS — no motion
   * library involved. Distinct from `hoverable`, which also sets
   * `cursor: pointer` for fully clickable cards.
   *
   * @default false
   */
  interactive?: boolean;
}

const paddingClasses: Record<CardPadding, string> = {
  none: "",
  sm: "p-4",
  md: "p-6",
  lg: "p-8",
};

/**
 * Glass panel surface — the base container of the design system.
 *
 * Uses the `--bg-panel` / `--border-subtle` tokens with backdrop blur.
 * Pass `hoverable` for interactive (clickable) cards.
 */
export const Card = forwardRef<HTMLDivElement, CardProps>(function Card(
  {
    padding = "md",
    hoverable = false,
    interactive = false,
    as = "div",
    className = "",
    ...rest
  },
  ref,
) {
  const Tag = as;

  return (
    <Tag
      ref={ref}
      className={`
        rounded-2xl
        border
        border-[color:var(--border-subtle)]
        bg-[color:var(--bg-panel)]
        backdrop-blur-lg
        ${paddingClasses[padding]}
        ${
          hoverable
            ? "cursor-pointer transition-all duration-200 hover:-translate-y-0.5 hover:border-[color:var(--border-active)] hover:shadow-glow"
            : ""
        }
        ${
          interactive
            ? "transition-all duration-200 hover:-translate-y-0.5 hover:border-[color:var(--border-active)] hover:shadow-glow"
            : ""
        }
        ${className}
      `}
      {...rest}
    />
  );
});

export default Card;
