import { useEffect, useState, type ReactNode } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import {
  BookOpen,
  LayoutDashboard,
  LogOut,
  Moon,
  PanelLeftClose,
  PanelLeftOpen,
  Search,
  Sun,
  User,
} from "lucide-react";

import { Avatar, Kbd, Tooltip } from "../primitives";
import {
  cycleTheme,
  getStoredTheme,
  type ThemeChoice,
} from "../../lib/theme";

export interface AppShellUser {
  fullName: string;
  email?: string;
}

interface AppShellProps {
  /** Called when the logout action is chosen. */
  onLogout: () => void;

  /** Opens the command palette (wired by the layout owner). */
  onOpenCommandPalette?: () => void;

  children: ReactNode;
}

const NAV_ITEMS = [
  { to: "/app/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { to: "/app/practice", label: "Practice", icon: BookOpen },
  { to: "/app/profile", label: "Profile", icon: User },
] as const;

function currentUser(): AppShellUser | null {
  try {
    const raw = localStorage.getItem("user");

    if (!raw) {
      return null;
    }

    const parsed = JSON.parse(raw) as {
      full_name?: string;
      email?: string;
    };

    return {
      fullName: parsed.full_name ?? "You",
      email: parsed.email,
    };
  } catch {
    return null;
  }
}

/**
 * The redesign shell: collapsible sidebar with an animated active
 * indicator, mobile bottom tabs, theme toggle. Wrapped routes render
 * inside the content pane.
 */
export default function AppShell({
  onLogout,
  onOpenCommandPalette,
  children,
}: AppShellProps) {
  const navigate = useNavigate();

  const [collapsed, setCollapsed] = useState(false);

  const [themeChoice, setThemeChoice] = useState<ThemeChoice>(() =>
    getStoredTheme(),
  );

  const [user, setUser] = useState(() => currentUser());

  useEffect(() => {
    const sync = () => setUser(currentUser());

    window.addEventListener("storage", sync);

    return () => window.removeEventListener("storage", sync);
  }, []);

  function handleThemeToggle() {
    setThemeChoice((current) => cycleTheme(current));
  }

  return (
    <div className="app-root flex min-h-screen">
      {/* =======================================================
          SIDEBAR (desktop)
      ======================================================== */}

      <aside
        className={`
          sticky top-0 hidden h-screen shrink-0 flex-col
          border-r border-line bg-paper md:flex
          transition-[width] duration-200
          ${collapsed ? "w-[68px]" : "w-[232px]"}
        `}
      >
        {/* Wordmark */}
        <div
          className={`flex h-14 items-center border-b border-line px-4 ${
            collapsed ? "justify-center px-0" : "justify-between"
          }`}
        >
          {!collapsed && (
            <button
              type="button"
              onClick={() => navigate("/app/dashboard")}
              className="display text-[15px] font-semibold text-ink"
            >
              Mock<span className="text-accent">.</span>
            </button>
          )}

          <Tooltip content={collapsed ? "Expand" : "Collapse"}>
            <button
              type="button"
              aria-label={collapsed ? "Expand sidebar" : "Collapse sidebar"}
              onClick={() => setCollapsed((value) => !value)}
              className={`
                rounded-md p-1.5 text-ink-3 transition-colors hover:bg-accent-soft hover:text-ink
                ${collapsed ? "mx-auto" : ""}
              `}
            >
              {collapsed ? (
                <PanelLeftOpen size={16} />
              ) : (
                <PanelLeftClose size={16} />
              )}
            </button>
          </Tooltip>
        </div>

        {/* Command palette trigger */}
        <div className={`px-3 pt-3 ${collapsed ? "px-2" : ""}`}>
          <button
            type="button"
            onClick={onOpenCommandPalette}
            className={`
              flex h-9 w-full items-center gap-2 rounded-lg border
              border-line bg-paper-raised px-2.5 text-[13px] text-ink-3
              transition-colors hover:border-line-strong hover:text-ink-2
              ${collapsed ? "justify-center" : ""}
            `}
          >
            <Search size={14} />

            {!collapsed && (
              <>
                <span className="flex-1 text-left">Jump to…</span>

                <Kbd>⌘K</Kbd>
              </>
            )}
          </button>
        </div>

        {/* Nav */}
        <nav className="flex-1 px-3 py-3">
          <ul className="flex flex-col gap-0.5">
            {NAV_ITEMS.map((item) => (
              <li key={item.to}>
                <NavLink to={item.to}>
                  {({ isActive }) => (
                    <span
                      className={`
                        group relative flex h-9 items-center gap-2.5 rounded-lg
                        px-2.5 text-[13px] font-medium transition-colors
                        ${
                          isActive
                            ? "bg-accent-soft text-accent"
                            : "text-ink-2 hover:bg-paper-sunken hover:text-ink"
                        }
                        ${collapsed ? "justify-center px-0" : ""}
                      `}
                    >
                      {/* Active indicator bar */}
                      <span
                        aria-hidden="true"
                        className={`
                          absolute left-0 top-1/2 h-4 w-[3px] -translate-y-1/2
                          rounded-full bg-accent transition-all duration-200
                          ${isActive ? "opacity-100" : "opacity-0"}
                          ${collapsed ? "-left-2" : ""}
                        `}
                      />

                      <item.icon size={16} aria-hidden="true" />

                      {!collapsed && item.label}
                    </span>
                  )}
                </NavLink>
              </li>
            ))}
          </ul>
        </nav>

        {/* Footer: theme + user */}
        <div className="border-t border-line p-3">
          <div
            className={`mb-2 flex ${collapsed ? "justify-center" : "justify-start"}`}
          >
            <Tooltip
              content={
                themeChoice === "light"
                  ? "Light (click: dark)"
                  : themeChoice === "dark"
                    ? "Dark (click: system)"
                    : "System (click: light)"
              }
            >
              <button
                type="button"
                aria-label="Toggle theme"
                onClick={handleThemeToggle}
                className="rounded-md p-1.5 text-ink-3 hover:bg-accent-soft hover:text-ink"
              >
                {themeChoice === "dark" ? (
                  <Moon size={16} />
                ) : (
                  <Sun size={16} />
                )}
              </button>
            </Tooltip>
          </div>

          <div
            className={`flex items-center gap-2.5 rounded-lg p-1.5 ${
              collapsed ? "justify-center" : ""
            }`}
          >
            <Avatar name={user?.fullName ?? "You"} />

            {!collapsed && (
              <>
                <span className="min-w-0 flex-1">
                  <span className="block truncate text-[13px] font-medium text-ink">
                    {user?.fullName ?? "You"}
                  </span>

                  <span className="block truncate text-[11px] text-ink-3">
                    {user?.email ?? "signed in"}
                  </span>
                </span>

                <Tooltip content="Sign out">
                  <button
                    type="button"
                    aria-label="Sign out"
                    onClick={onLogout}
                    className="rounded-md p-1.5 text-ink-3 hover:bg-[color:var(--bad-soft)] hover:text-[color:var(--bad)]"
                  >
                    <LogOut size={15} />
                  </button>
                </Tooltip>
              </>
            )}
          </div>
        </div>
      </aside>

      {/* =======================================================
          CONTENT
      ======================================================== */}

      <div className="flex min-w-0 flex-1 flex-col">
        {/* Mobile top bar */}
        <header className="sticky top-0 z-30 flex h-12 items-center justify-between border-b border-line bg-paper/90 px-4 backdrop-blur md:hidden">
          <span className="display text-[15px] font-semibold text-ink">
            Mock<span className="text-accent">.</span>
          </span>

          <div className="flex items-center gap-1">
            <button
              type="button"
              aria-label="Search (opens command palette)"
              onClick={onOpenCommandPalette}
              className="rounded-md p-1.5 text-ink-3 hover:bg-accent-soft hover:text-ink"
            >
              <Search size={16} />
            </button>

            <button
              type="button"
              aria-label="Toggle theme"
              onClick={handleThemeToggle}
              className="rounded-md p-1.5 text-ink-3 hover:bg-accent-soft hover:text-ink"
            >
              {themeChoice === "dark" ? <Moon size={16} /> : <Sun size={16} />}
            </button>

            <button
              type="button"
              aria-label="Sign out"
              onClick={onLogout}
              className="rounded-md p-1.5 text-ink-3 hover:bg-[color:var(--bad-soft)] hover:text-[color:var(--bad)]"
            >
              <LogOut size={16} />
            </button>
          </div>
        </header>

        <main className="min-w-0 flex-1">{children}</main>

        {/* Mobile bottom tabs */}
        <nav className="sticky bottom-0 z-30 flex h-14 items-stretch border-t border-line bg-paper/95 backdrop-blur md:hidden">
          {NAV_ITEMS.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className="flex flex-1 flex-col items-center justify-center gap-0.5"
            >
              {({ isActive }) => (
                <>
                  <item.icon
                    size={18}
                    aria-hidden="true"
                    className={isActive ? "text-accent" : "text-ink-3"}
                  />

                  <span
                    className={`
                      text-[10px] font-medium
                      ${isActive ? "text-accent" : "text-ink-3"}
                    `}
                  >
                    {item.label}
                  </span>
                </>
              )}
            </NavLink>
          ))}
        </nav>
      </div>
    </div>
  );
}
