import {
  forwardRef,
  type ButtonHTMLAttributes,
  type ReactNode,
} from "react";

type ButtonVariant = "primary" | "secondary" | "ghost";

type ButtonSize = "sm" | "md" | "lg";

export interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement> {
  /**
   * Visual style of the button.
   * - `primary`: violet gradient fill with a glow shadow on hover.
   * - `secondary`: bordered glass surface; border brightens on hover.
   * - `ghost`: transparent until hovered.
   *
   * @default "primary"
   */
  variant?: ButtonVariant;

  /**
   * Controls padding and font size.
   *
   * @default "md"
   */
  size?: ButtonSize;

  /**
   * Shows an inline spinner and disables the button.
   * The children remain visible so the label can read
   * e.g. "Evaluating answer...".
   *
   * @default false
   */
  isLoading?: boolean;

  /**
   * Stretch the button to the full width of its container.
   *
   * @default false
   */
  fullWidth?: boolean;

  /** Optional leading element (icon, glyph) shown before the label. */
  leadingIcon?: ReactNode;
}

const variantClasses: Record<ButtonVariant, string> = {
  primary:
    "border border-[color:var(--border-active)] bg-[linear-gradient(135deg,var(--accent-violet),var(--accent-purple))] text-white hover:brightness-110 hover:shadow-glow",
  secondary:
    "border border-[color:var(--border-subtle)] bg-white/[0.045] text-[color:var(--text-primary)] hover:border-[color:var(--border-active)] hover:bg-white/[0.07]",
  ghost:
    "border border-transparent bg-transparent text-[color:var(--text-secondary)] hover:bg-white/[0.05] hover:text-[color:var(--text-primary)]",
};

const sizeClasses: Record<ButtonSize, string> = {
  sm: "rounded-lg px-3 py-2 text-xs",
  md: "rounded-xl px-4 py-2.5 text-sm",
  lg: "rounded-xl px-6 py-3.5 text-sm",
};

/**
 * Shared button used across the app.
 *
 * Built exclusively on the design tokens defined in
 * `tailwind.config.js` and `src/index.css` — no ad-hoc colors.
 */
export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  function Button(
    {
      variant = "primary",
      size = "md",
      isLoading = false,
      fullWidth = false,
      leadingIcon,
      className = "",
      children,
      disabled,
      type = "button",
      ...rest
    },
    ref,
  ) {
    const isDisabled = disabled || isLoading;

    return (
      <button
        ref={ref}
        type={type}
        aria-busy={isLoading || undefined}
        disabled={isDisabled}
        className={`
          inline-flex
          items-center
          justify-center
          gap-2
          font-semibold
          transition-all
          duration-200
          disabled:cursor-not-allowed
          disabled:opacity-50
          ${variantClasses[variant]}
          ${sizeClasses[size]}
          ${fullWidth ? "w-full" : ""}
          ${className}
        `}
        {...rest}
      >
        {isLoading && (
          <span
            aria-hidden="true"
            className="
              h-4
              w-4
              animate-spin
              rounded-full
              border-2
              border-transparent
              border-t-current
            "
          />
        )}

        {!isLoading && leadingIcon}

        {children}
      </button>
    );
  },
);

export default Button;
