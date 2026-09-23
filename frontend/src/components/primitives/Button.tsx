import { forwardRef, type ButtonHTMLAttributes, type ReactNode } from "react";

type ButtonVariant =
  | "primary"
  | "secondary"
  | "ghost"
  | "danger";

type ButtonSize = "xs" | "sm" | "md" | "lg";

export interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement> {
  /** Visual weight. `primary` is the single loud action on a screen. */
  variant?: ButtonVariant;

  /** @default "md" */
  size?: ButtonSize;

  /** Spinner + disabled + aria-busy. Label stays visible. */
  isLoading?: boolean;

  /** Stretch to container width. */
  fullWidth?: boolean;

  /** Leading icon slot (Lucide). */
  icon?: ReactNode;
}

const variants: Record<ButtonVariant, string> = {
  primary:
    "bg-accent text-[color:var(--accent-ink)] hover:bg-[color:var(--accent-hover)] active:translate-y-px shadow-xs",
  secondary:
    "bg-paper-raised text-ink border border-line-strong hover:border-[color:var(--ink-3)] hover:bg-paper-sunken/60 active:translate-y-px shadow-xs",
  ghost:
    "bg-transparent text-ink-2 hover:text-ink hover:bg-accent-soft border border-transparent",
  danger:
    "bg-[color:var(--bad)] text-white hover:brightness-110 active:translate-y-px shadow-xs",
};

const sizes: Record<ButtonSize, string> = {
  xs: "h-7 gap-1.5 rounded-md px-2.5 text-xs",
  sm: "h-8 gap-1.5 rounded-lg px-3 text-[13px]",
  md: "h-10 gap-2 rounded-lg px-4 text-sm",
  lg: "h-12 gap-2 rounded-xl px-6 text-[15px]",
};

/**
 * The one button. Four variants, four sizes, loading state.
 * Focus ring comes from the global :focus-visible token rule.
 */
export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  function Button(
    {
      variant = "primary",
      size = "md",
      isLoading = false,
      fullWidth = false,
      icon,
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
          inline-flex select-none items-center justify-center
          font-sans font-medium tracking-[-0.01em]
          transition-colors duration-150
          disabled:cursor-not-allowed disabled:opacity-45
          ${variants[variant]}
          ${sizes[size]}
          ${fullWidth ? "w-full" : ""}
          ${className}
        `}
        {...rest}
      >
        {isLoading ? (
          <span
            aria-hidden="true"
            className="
              h-3.5 w-3.5 animate-spin rounded-full
              border-[1.5px] border-transparent
              border-t-current border-r-current
            "
          />
        ) : (
          icon
        )}

        {children}
      </button>
    );
  },
);

export default Button;
