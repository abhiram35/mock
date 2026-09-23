/* eslint-disable react-refresh/only-export-components -- useToast is intentionally co-located with its provider */

import {
  createContext,
  useCallback,
  useContext,
  useMemo,
  useRef,
  useState,
  type ReactNode,
} from "react";

type ToastTone = "info" | "ok" | "warn" | "bad";

interface ToastItem {
  id: number;

  tone: ToastTone;

  title: string;

  description?: string;
}

interface ToastContextValue {
  toast: (toast: {
    tone?: ToastTone;
    title: string;
    description?: string;
  }) => void;
}

const ToastContext = createContext<ToastContextValue | null>(null);

const toneStyles: Record<ToastTone, string> = {
  info: "border-line",
  ok: "border-[color:var(--ok)]",
  warn: "border-[color:var(--warn)]",
  bad: "border-[color:var(--bad)]",
};

const toneDot: Record<ToastTone, string> = {
  info: "bg-[color:var(--info)]",
  ok: "bg-[color:var(--ok)]",
  warn: "bg-[color:var(--warn)]",
  bad: "bg-[color:var(--bad)]",
};

/**
 * App-level toast queue. Mount `<ToastProvider>` once, call
 * `const { toast } = useToast()` anywhere, then
 * `toast({ tone: "ok", title: "Saved" })`.
 */
export function ToastProvider({ children }: { children: ReactNode }) {
  const [toasts, setToasts] = useState<ToastItem[]>([]);

  const nextId = useRef(1);

  const toast = useCallback(
    ({
      tone = "info",
      title,
      description,
    }: {
      tone?: ToastTone;
      title: string;
      description?: string;
    }) => {
      const id = nextId.current++;

      setToasts((current) => [...current, { id, tone, title, description }]);

      window.setTimeout(() => {
        setToasts((current) => current.filter((item) => item.id !== id));
      }, 4200);
    },
    [],
  );

  const value = useMemo(() => ({ toast }), [toast]);

  return (
    <ToastContext.Provider value={value}>
      {children}

      <div
        aria-live="polite"
        className="
          pointer-events-none fixed bottom-5 right-5 z-[60]
          flex w-full max-w-sm flex-col gap-2
        "
      >
        {toasts.map((item) => (
          <div
            key={item.id}
            className={`
              pointer-events-auto flex items-start gap-3
              rounded-xl border bg-paper-raised px-4 py-3 shadow-lg2
              ${toneStyles[item.tone]}
            `}
          >
            <span
              aria-hidden="true"
              className={`mt-1.5 h-2 w-2 shrink-0 rounded-full ${toneDot[item.tone]}`}
            />

            <div className="min-w-0">
              <p className="text-sm font-medium text-ink">{item.title}</p>

              {item.description && (
                <p className="mt-0.5 text-xs leading-5 text-ink-2">
                  {item.description}
                </p>
              )}
            </div>

            <button
              type="button"
              aria-label="Dismiss notification"
              onClick={() =>
                setToasts((current) => current.filter((t) => t.id !== item.id))
              }
              className="ml-auto shrink-0 rounded p-0.5 text-ink-3 hover:text-ink"
            >
              ✕
            </button>
          </div>
        ))}
      </div>
    </ToastContext.Provider>
  );
}

export function useToast(): ToastContextValue {
  const context = useContext(ToastContext);

  if (!context) {
    throw new Error("useToast must be used within ToastProvider");
  }

  return context;
}
