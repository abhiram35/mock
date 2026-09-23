import {
  forwardRef,
  useId,
  type InputHTMLAttributes,
  type ReactNode,
  type SelectHTMLAttributes,
  type TextareaHTMLAttributes,
} from "react";

const fieldBase =
  "w-full rounded-lg border bg-paper-raised text-ink text-sm " +
  "placeholder:text-ink-3 transition-colors duration-150 " +
  "disabled:cursor-not-allowed disabled:opacity-50";

const fieldTone = (invalid: boolean) =>
  invalid
    ? "border-[color:var(--bad)] focus:border-[color:var(--bad)]"
    : "border-line-strong focus:border-accent";

function FieldFrame({
  id,
  label,
  hint,
  error,
  children,
}: {
  id: string;
  label?: string;
  hint?: string;
  error?: string;
  children: ReactNode;
}) {
  return (
    <div className="flex flex-col gap-1.5">
      {label && (
        <label
          htmlFor={id}
          className="text-[13px] font-medium text-ink-2"
        >
          {label}
        </label>
      )}

      {children}

      {error ? (
        <p className="text-xs text-[color:var(--bad)]">{error}</p>
      ) : hint ? (
        <p className="text-xs text-ink-3">{hint}</p>
      ) : null}
    </div>
  );
}

export interface InputProps
  extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  hint?: string;
  error?: string;
  /** Leading icon slot (Lucide). */
  icon?: ReactNode;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  function Input({ label, hint, error, icon, className = "", id, ...rest }, ref) {
    const autoId = useId();

    const inputId = id ?? autoId;

    return (
      <FieldFrame
        id={inputId}
        label={label}
        hint={hint}
        error={error}
      >
        <div className="relative">
          {icon && (
            <span className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-ink-3">
              {icon}
            </span>
          )}

          <input
            ref={ref}
            id={inputId}
            aria-invalid={error ? true : undefined}
            className={`
              ${fieldBase} ${fieldTone(Boolean(error))} h-10 px-3
              ${icon ? "pl-9" : ""}
              ${className}
            `}
            {...rest}
          />
        </div>
      </FieldFrame>
    );
  },
);

export interface TextareaProps
  extends TextareaHTMLAttributes<HTMLTextAreaElement> {
  label?: string;
  hint?: string;
  error?: string;
}

export const Textarea = forwardRef<HTMLTextAreaElement, TextareaProps>(
  function Textarea({ label, hint, error, className = "", id, ...rest }, ref) {
    const autoId = useId();

    const inputId = id ?? autoId;

    return (
      <FieldFrame id={inputId} label={label} hint={hint} error={error}>
        <textarea
          ref={ref}
          id={inputId}
          aria-invalid={error ? true : undefined}
          className={`${fieldBase} ${fieldTone(Boolean(error))} min-h-[110px] px-3 py-2.5 leading-6 ${className}`}
          {...rest}
        />
      </FieldFrame>
    );
  },
);

export interface SelectProps
  extends SelectHTMLAttributes<HTMLSelectElement> {
  label?: string;
  hint?: string;
  error?: string;
}

export const Select = forwardRef<HTMLSelectElement, SelectProps>(
  function Select({ label, hint, error, className = "", id, children, ...rest }, ref) {
    const autoId = useId();

    const inputId = id ?? autoId;

    return (
      <FieldFrame id={inputId} label={label} hint={hint} error={error}>
        <div className="relative">
          <select
            ref={ref}
            id={inputId}
            aria-invalid={error ? true : undefined}
            className={`${fieldBase} ${fieldTone(Boolean(error))} h-10 appearance-none pl-3 pr-9 ${className}`}
            {...rest}
          >
            {children}
          </select>

          <span
            aria-hidden="true"
            className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-ink-3"
          >
            ▾
            {" "}
          </span>
        </div>
      </FieldFrame>
    );
  },
);
