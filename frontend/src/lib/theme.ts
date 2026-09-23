export type ThemeChoice = "light" | "dark" | "system";

const STORAGE_KEY = "app.theme";

function systemPrefersDark(): boolean {
  return (
    window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches
  );
}

function resolve(choice: ThemeChoice): "light" | "dark" {
  if (choice === "system") {
    return systemPrefersDark() ? "dark" : "light";
  }

  return choice;
}

export function getStoredTheme(): ThemeChoice {
  const stored = localStorage.getItem(STORAGE_KEY);

  if (stored === "light" || stored === "dark" || stored === "system") {
    return stored;
  }

  return "system";
}

/** Applies `data-theme` to <html> and persists the choice. */
export function applyTheme(choice: ThemeChoice): "light" | "dark" {
  const resolved = resolve(choice);

  document.documentElement.setAttribute("data-theme", resolved);

  localStorage.setItem(STORAGE_KEY, choice);

  return resolved;
}

/**
 * Initializes theme on boot and follows the OS setting while the
 * user's choice is "system". Returns a cleanup function.
 */
export function initTheme(): () => void {
  applyTheme(getStoredTheme());

  const media = window.matchMedia("(prefers-color-scheme: dark)");

  const onChange = () => {
    if (getStoredTheme() === "system") {
      applyTheme("system");
    }
  };

  media.addEventListener("change", onChange);

  return () => media.removeEventListener("change", onChange);
}

export function cycleTheme(current: ThemeChoice): ThemeChoice {
  const next: ThemeChoice =
    current === "light" ? "dark" : current === "dark" ? "system" : "light";

  applyTheme(next);

  return next;
}
