import { useEffect, useRef } from "react";
import { createPortal } from "react-dom";

import Card from "./Card";

export interface ModalProps {
  /** Controls visibility. When false nothing renders. */
  isOpen: boolean;

  /** Fired by backdrop click, the X button, or the Escape key. */
  onClose: () => void;

  /** Accessible dialog name; also the visually hidden heading. */
  title: string;

  /** Panel content. */
  children: React.ReactNode;

  /** Max width of the panel. @default "md" */
  size?: "sm" | "md" | "lg";
}

const sizeClasses: Record<NonNullable<ModalProps["size"]>, string> = {
  sm: "max-w-sm",
  md: "max-w-md",
  lg: "max-w-lg",
};

/**
 * Centered dialog over a blurred backdrop.
 *
 * Closes on backdrop click and Escape. Portal-rendered, locks body
 * scroll while open, and focus is trapped inside the panel.
 */
export function Modal({
  isOpen,
  onClose,
  title,
  children,
  size = "md",
}: ModalProps) {
  const panelRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!isOpen) {
      return;
    }

    const previousOverflow = document.body.style.overflow;

    document.body.style.overflow = "hidden";

    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        event.stopPropagation();
        onClose();
        return;
      }

      if (event.key === "Tab" && panelRef.current) {
        const focusables = panelRef.current.querySelectorAll<HTMLElement>(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])',
        );

        if (focusables.length === 0) {
          return;
        }

        const first = focusables[0];
        const last = focusables[focusables.length - 1];

        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault();
          last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault();
          first.focus();
        }
      }
    };

    document.addEventListener("keydown", handleKeyDown);

    const timer = window.setTimeout(() => {
      panelRef.current
        ?.querySelector<HTMLElement>(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])',
        )
        ?.focus();
    }, 0);

    return () => {
      document.removeEventListener("keydown", handleKeyDown);
      document.body.style.overflow = previousOverflow;
      window.clearTimeout(timer);
    };
  }, [isOpen, onClose]);

  if (!isOpen) {
    return null;
  }

  return createPortal(
    <div
      className="
        fixed
        inset-0
        z-50
        flex
        items-center
        justify-center
        p-4
      "
      role="presentation"
    >
      {/* Backdrop */}
      <div
        className="
          absolute
          inset-0
          bg-black/60
          backdrop-blur-sm
        "
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Panel */}
      <Card
        ref={panelRef}
        role="dialog"
        aria-modal="true"
        aria-label={title}
        padding="lg"
        className={`
          relative
          z-10
          w-full
          shadow-glow
          ${sizeClasses[size]}
        `}
      >
        <h2
          className="
            font-display
            text-lg
            font-semibold
            text-[color:var(--text-primary)]
          "
        >
          {title}
        </h2>

        <button
          type="button"
          onClick={onClose}
          aria-label="Close dialog"
          className="
            absolute
            right-4
            top-4
            flex
            h-8
            w-8
            items-center
            justify-center
            rounded-lg
            text-[color:var(--text-muted)]
            transition-colors
            hover:bg-white/[0.06]
            hover:text-[color:var(--text-primary)]
          "
        >
          ✕
        </button>

        <div className="mt-4">{children}</div>
      </Card>
    </div>,
    document.body,
  );
}

export default Modal;
