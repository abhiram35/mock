import { forwardRef, type HTMLAttributes } from "react";

type CardPadding = "none" | "sm" | "md" | "lg";

type CardTag = "div" | "article" | "section";

export interface CardProps extends HTMLAttributes<HTMLDivElement> {
  /** @default "md" */
  padding?: CardPadding;

  /** Elevation level; `flat` uses border only. */
  elevation?: "flat" | "xs" | "sm" | "md";

  /** Adds hover elevation + border shift for clickable cards. */
  interactive?: boolean;

  /** Semantic tag to render. @default "div" */
  as?: CardTag;
}

const paddings: Record<CardPadding, string> = {
  none: "",
  sm: "p-4",
  md: "p-6",
  lg: "p-8",
};

const elevations: Record<
  NonNullable<CardProps["elevation"]>,
  string
> = {
  flat: "",
  xs: "shadow-xs",
  sm: "shadow-sm2",
  md: "shadow-md2",
};

/**
 * The workhorse surface: paper-raised, hairline border, quiet
 * layered shadow. `interactive` for clickable cards.
 */
export const Card = forwardRef<HTMLDivElement, CardProps>(function Card(
  {
    padding = "md",
    elevation = "xs",
    interactive = false,
    as: Tag = "div",
    className = "",
    ...rest
  },
  ref,
) {
  return (
    <Tag
      ref={ref}
      className={`
        rounded-xl border border-line bg-paper-raised
        transition-all duration-200
        ${paddings[padding]}
        ${elevations[elevation]}
        ${
          interactive
            ? "cursor-pointer hover:-translate-y-0.5 hover:border-line-strong hover:shadow-sm2"
            : ""
        }
        ${className}
      `}
      {...rest}
    />
  );
});

export default Card;
