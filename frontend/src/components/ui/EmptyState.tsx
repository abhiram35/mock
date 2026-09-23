import type { ReactNode } from "react";

import Button from "./Button";
import Card from "./Card";

export interface EmptyStateProps {
  /**
   * Icon / illustration slot rendered inside a rounded tile.
   * Accepts any node — a glyph, SVG, or custom illustration.
   */
  icon?: ReactNode;

  /** Short headline, e.g. "No interviews yet". */
  title: string;

  /** One or two sentences explaining the state. */
  description?: string;

  /**
   * Primary action for the state, e.g. "Start Your First Interview".
   * Rendered as a full `Button` so all its props are available.
   */
  action?: {
    label: string;
    onClick: () => void;
  };
}

/**
 * Placeholder for empty collections ("no interviews yet",
 * "no practice problems", etc.).
 *
 * Card-backed, centered, with an optional call-to-action.
 */
export function EmptyState({ icon, title, description, action }: EmptyStateProps) {
  return (
    <Card padding="lg" className="text-center">
      <div className="flex flex-col items-center">
        {icon && (
          <span
            aria-hidden="true"
            className="
              flex
              h-12
              w-12
              items-center
              justify-center
              rounded-xl
              bg-[rgba(139,92,246,0.08)]
              text-xl
              text-[color:var(--accent-violet)]
            "
          >
            {icon}
          </span>
        )}

        <h3
          className="
            mt-4
            font-display
            text-lg
            font-semibold
            text-[color:var(--text-primary)]
          "
        >
          {title}
        </h3>

        {description && (
          <p
            className="
              mt-2
              max-w-md
              text-sm
              leading-6
              text-[color:var(--text-secondary)]
            "
          >
            {description}
          </p>
        )}

        {action && (
          <div className="mt-6">
            <Button onClick={action.onClick}>{action.label}</Button>
          </div>
        )}
      </div>
    </Card>
  );
}

export default EmptyState;
