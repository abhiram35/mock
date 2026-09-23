import { useId } from "react";

export interface TabItem {
  id: string;
  label: string;
}

export interface TabsProps {
  items: TabItem[];
  value: string;
  onChange: (id: string) => void;

  /** Accessible name for the tab group. */
  label: string;
}

/**
 * Segmented control with a sliding ink pill for the active tab.
 */
export function Tabs({ items, value, onChange, label }: TabsProps) {
  const groupId = useId();

  return (
    <div
      role="tablist"
      aria-label={label}
      className="inline-flex items-center gap-1 rounded-lg border border-line bg-paper-sunken/60 p-1"
    >
      {items.map((item) => {
        const isSelected = item.id === value;

        return (
          <button
            key={`${groupId}-${item.id}`}
            role="tab"
            aria-selected={isSelected}
            onClick={() => onChange(item.id)}
            className={`
              rounded-md px-3 py-1.5 text-[13px] font-medium
              transition-colors duration-150
              ${
                isSelected
                  ? "bg-paper-raised text-ink shadow-xs"
                  : "text-ink-2 hover:text-ink"
              }
            `}
          >
            {item.label}
          </button>
        );
      })}
    </div>
  );
}
