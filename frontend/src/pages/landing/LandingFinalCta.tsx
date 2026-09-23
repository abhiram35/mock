import { useNavigate } from "react-router-dom";

/**
 * Landing final CTA: the gradient panel with the account button.
 */
export default function LandingFinalCta() {
  const navigate = useNavigate();

  return (
    <section className="mx-auto max-w-7xl px-6 py-28 lg:px-8">
      <div className="relative overflow-hidden rounded-3xl border border-violet-300/10 bg-gradient-to-br from-violet-500/[0.09] via-white/[0.025] to-cyan-500/[0.05] p-10 text-center sm:p-16">
        <div className="pointer-events-none absolute left-1/2 top-1/2 h-64 w-64 -translate-x-1/2 -translate-y-1/2 rounded-full bg-violet-500/10 blur-[100px]" />

        <div className="relative">
          <div className="text-[10px] font-semibold uppercase tracking-[0.25em] text-violet-300">
            Your next interview starts here
          </div>

          <h2 className="mx-auto mt-5 max-w-2xl text-3xl font-semibold tracking-tight sm:text-5xl">
            Turn interview anxiety into interview confidence.
          </h2>

          <p className="mx-auto mt-5 max-w-xl text-sm leading-7 text-slate-400">
            Practice technical questions, understand your weaknesses, and
            walk into your next interview better prepared.
          </p>

          <button
            type="button"
            onClick={() => navigate("/register")}
            className="group mt-8 inline-flex items-center gap-3 rounded-xl bg-white px-7 py-3.5 text-sm font-bold text-[#0b0c16] transition hover:-translate-y-0.5 hover:bg-violet-100 active:translate-y-0"
          >
            Create your account
            <span className="transition-transform group-hover:translate-x-1">
              →
            </span>
          </button>
        </div>
      </div>
    </section>
  );
}
