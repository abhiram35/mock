import { useNavigate } from "react-router-dom";

/**
 * Landing navbar: logo, anchor navigation and auth actions.
 */
export default function LandingNavbar() {
  const navigate = useNavigate();

  return (
    <header className="landing-nav relative z-10">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6 lg:px-8">
        {/* Logo */}
        <button
          type="button"
          onClick={() => navigate("/")}
          className="group flex items-center gap-3"
          aria-label="Go to home"
        >
          <div className="landing-logo-mark relative flex h-9 w-9 items-center justify-center rounded-xl">
            <span className="h-1.5 w-1.5 rounded-full bg-violet-100 shadow-[0_0_14px_rgba(196,181,253,1)]" />
            <span className="absolute h-4 w-1 rounded-full bg-violet-300/80" />
            <span className="absolute h-2.5 w-1 rounded-full bg-cyan-300/80 -translate-x-2" />
            <span className="absolute h-3 w-1 rounded-full bg-violet-300/80 translate-x-2" />
          </div>

          <div className="text-left">
            <div className="text-sm font-semibold tracking-wide">
              AI Mock Interview
            </div>

            <div className="text-[9px] uppercase tracking-[0.25em] text-slate-500">
              Interview Lab
            </div>
          </div>
        </button>

        {/* Navigation */}
        <nav className="hidden items-center gap-8 md:flex">
          <a
            href="#how-it-works"
            className="landing-nav-link text-sm text-slate-400 transition hover:text-white"
          >
            How it works
          </a>

          <a
            href="#features"
            className="landing-nav-link text-sm text-slate-400 transition hover:text-white"
          >
            Features
          </a>
        </nav>

        {/* Auth */}
        <div className="flex items-center gap-3">
          <button
            type="button"
            onClick={() => navigate("/login")}
            className="rounded-lg px-4 py-2 text-sm font-medium text-slate-300 transition hover:bg-white/[0.05] hover:text-white"
          >
            Sign in
          </button>

          <button
            type="button"
            onClick={() => navigate("/register")}
            className="rounded-lg border border-violet-300/40 bg-violet-400/15 px-4 py-2 text-sm font-semibold text-violet-100 transition hover:border-violet-200/70 hover:bg-violet-400/25"
          >
            Get started
          </button>
        </div>
      </div>
    </header>
  );
}
