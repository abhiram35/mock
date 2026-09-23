import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  BookOpen,
  LayoutDashboard,
  Moon,
  Search,
  Sun,
  User,
  Zap,
} from "lucide-react";

import { Kbd } from "../primitives";
import { applyTheme, getStoredTheme } from "../../lib/theme";
import { practiceClient } from "../../lib/practice/client";

interface Command {
  id: string;
  label: string;
  hint?: string;
  group: string;
  icon: React.ReactNode;
  run: () => void;
}

/**
 * Global ⌘K palette: navigation, quick actions, and live track
 * jumps loaded from the practice data layer.
 */
export default function CommandPalette({
  isOpen,
  onClose,
}: {
  isOpen: boolean;
  onClose: () => void;
}) {
  const navigate = useNavigate();

  const [query, setQuery] = useState("");

  const [activeIndex, setActiveIndex] = useState(0);

  const [tracks, setTracks] = useState<
    Array<{ id: string; name: string; problemCount: number }>
  >([]);

  const inputRef = useRef<HTMLInputElement>(null);

  const listRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!isOpen) {
      setQuery("");
      setActiveIndex(0);
      return;
    }

    inputRef.current?.focus();

    let cancelled = false;

    practiceClient
      .listTracks()
      .then((items) => {
        if (!cancelled) {
          setTracks(
            items.map((track) => ({
              id: track.id,
              name: track.name,
              problemCount: track.problemCount,
            })),
          );
        }
      })
      .catch(() => {
        /* Palette still works for static commands. */
      });

    return () => {
      cancelled = true;
    };
  }, [isOpen]);

  const commands = useMemo<Command[]>(() => {
    const base: Command[] = [
      {
        id: "nav-dashboard",
        label: "Dashboard",
        group: "Go to",
        icon: <LayoutDashboard size={15} />,
        run: () => navigate("/app/dashboard"),
      },
      {
        id: "nav-practice",
        label: "Practice tracks",
        group: "Go to",
        icon: <BookOpen size={15} />,
        run: () => navigate("/app/practice"),
      },
      {
        id: "nav-profile",
        label: "Profile",
        group: "Go to",
        icon: <User size={15} />,
        run: () => navigate("/app/profile"),
      },
      {
        id: "act-interview",
        label: "Start an interview",
        hint: "AI topic interview",
        group: "Actions",
        icon: <Zap size={15} />,
        run: () => navigate("/interviews/new"),
      },
    ];

    if (getStoredTheme() === "dark") {
      base.push({
        id: "theme-light",
        label: "Switch to light theme",
        group: "Preferences",
        icon: <Sun size={15} />,
        run: () => applyTheme("light"),
      });
    } else {
      base.push({
        id: "theme-dark",
        label: "Switch to dark theme",
        group: "Preferences",
        icon: <Moon size={15} />,
        run: () => applyTheme("dark"),
      });
    }

    tracks.forEach((track) => {
      base.push({
        id: `track-${track.id}`,
        label: track.name,
        hint: `${track.problemCount} problems`,
        group: "Practice tracks",
        icon: <BookOpen size={15} />,
        run: () => navigate(`/app/practice/${track.id}`),
      });
    });

    return base;
  }, [navigate, tracks]);

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();

    if (!q) {
      return commands;
    }

    return commands.filter(
      (command) =>
        command.label.toLowerCase().includes(q) ||
        command.group.toLowerCase().includes(q),
    );
  }, [commands, query]);

  useEffect(() => {
    setActiveIndex(0);
  }, [query]);

  useEffect(() => {
    if (!isOpen) {
      return;
    }

    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        onClose();
        return;
      }

      if (event.key === "ArrowDown") {
        event.preventDefault();
        setActiveIndex((index) => Math.min(index + 1, filtered.length - 1));
      }

      if (event.key === "ArrowUp") {
        event.preventDefault();
        setActiveIndex((index) => Math.max(index - 1, 0));
      }

      if (event.key === "Enter" && filtered[activeIndex]) {
        event.preventDefault();
        filtered[activeIndex].run();
        onClose();
      }
    };

    document.addEventListener("keydown", onKeyDown);

    return () => document.removeEventListener("keydown", onKeyDown);
  }, [isOpen, filtered, activeIndex, onClose]);

  useEffect(() => {
    listRef.current
      ?.querySelectorAll("[data-command]")
      [activeIndex]?.scrollIntoView({ block: "nearest" });
  }, [activeIndex]);

  if (!isOpen) {
    return null;
  }

  let lastGroup = "";

  return (
    <div
      className="fixed inset-0 z-[70] flex items-start justify-center pt-[12vh]"
      role="presentation"
    >
      <div
        aria-hidden="true"
        className="absolute inset-0 bg-[rgba(20,18,15,0.45)]"
        onClick={onClose}
      />

      <div
        role="dialog"
        aria-modal="true"
        aria-label="Command palette"
        className="
          relative z-10 w-full max-w-lg overflow-hidden rounded-xl
          border border-line bg-paper-raised shadow-lg2
        "
      >
        <div className="flex items-center gap-2.5 border-b border-line px-4">
          <Search size={15} aria-hidden="true" className="text-ink-3" />

          <input
            ref={inputRef}
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Jump to a track, action, or setting…"
            aria-label="Command palette search"
            className="h-12 w-full bg-transparent text-sm text-ink outline-none placeholder:text-ink-3"
          />

          <Kbd>esc</Kbd>
        </div>

        <div
          ref={listRef}
          className="max-h-[46vh] overflow-y-auto p-2"
        >
          {filtered.length === 0 && (
            <p className="px-3 py-8 text-center text-sm text-ink-3">
              Nothing matches “{query}”.
            </p>
          )}

          {filtered.map((command, index) => {
            const showGroup = command.group !== lastGroup;

            lastGroup = command.group;

            return (
              <div key={command.id}>
                {showGroup && (
                  <p className="px-3 pb-1 pt-3 text-[10px] font-semibold uppercase tracking-[0.12em] text-ink-3">
                    {command.group}
                  </p>
                )}

                <button
                  data-command={command.id}
                  onMouseEnter={() => setActiveIndex(index)}
                  onClick={() => {
                    command.run();
                    onClose();
                  }}
                  className={`
                    flex w-full items-center gap-2.5 rounded-lg px-3 py-2
                    text-left text-sm transition-colors
                    ${
                      index === activeIndex
                        ? "bg-accent-soft text-accent"
                        : "text-ink-2"
                    }
                  `}
                >
                  <span aria-hidden="true">{command.icon}</span>

                  <span className="flex-1 truncate">{command.label}</span>

                  {command.hint && (
                    <span className="text-[11px] text-ink-3">
                      {command.hint}
                    </span>
                  )}
                </button>
              </div>
            );
          })}
        </div>

        <div className="flex items-center gap-3 border-t border-line px-4 py-2 text-[11px] text-ink-3">
          <span className="flex items-center gap-1">
            <Kbd>↑</Kbd>
            <Kbd>↓</Kbd> navigate
          </span>

          <span className="flex items-center gap-1">
            <Kbd>↵</Kbd> select
          </span>
        </div>
      </div>
    </div>
  );
}
