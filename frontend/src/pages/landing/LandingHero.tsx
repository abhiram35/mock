import { useNavigate } from "react-router-dom";

/**
 * Landing hero: headline, CTAs and the AI-interview visual card.
 */
export default function LandingHero() {
  const navigate = useNavigate();

  return (
    <section className="landing-hero mx-auto max-w-7xl px-6 pb-28 pt-24 lg:px-8 lg:pb-40 lg:pt-32">
      <div className="grid items-center gap-16 lg:grid-cols-[1.05fr_0.95fr]">
        {/* Hero copy */}
        <div className="max-w-2xl">
          {/* Eyebrow */}
          <div className="landing-reveal landing-reveal-1 mb-8 inline-flex items-center gap-2 rounded-full border border-violet-300/25 bg-violet-300/[0.09] px-4 py-2">
            <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-emerald-400" />

            <span className="text-[10px] font-semibold uppercase tracking-[0.22em] text-violet-200">
              AI-powered interview practice
            </span>
          </div>

          <h1 className="landing-reveal landing-reveal-2 max-w-4xl text-5xl font-semibold leading-[1.03] tracking-[-0.04em] text-white sm:text-6xl lg:text-7xl">
            Practice like you're
            <span className="landing-headline-accent block bg-clip-text text-transparent">
              already in the room.
            </span>
          </h1>

          <p className="landing-reveal landing-reveal-3 mt-8 max-w-2xl text-base leading-8 text-slate-400 sm:text-lg">
            Prepare for technical interviews with an AI interviewer that
            asks questions, evaluates your answers, adapts the difficulty,
            and gives you actionable feedback.
          </p>

          {/* CTA */}
          <div className="landing-reveal landing-reveal-4 mt-10 flex flex-col gap-3 sm:flex-row">
            <button
              type="button"
              onClick={() => navigate("/register")}
              className="landing-primary-cta group inline-flex items-center justify-center gap-3 rounded-xl px-6 py-3.5 text-sm font-bold transition duration-200 active:translate-y-0"
            >
              Start practicing
              <span className="transition-transform duration-200 group-hover:translate-x-1">
                →
              </span>
            </button>

            <button
              type="button"
              onClick={() => navigate("/login")}
              className="inline-flex items-center justify-center rounded-xl border border-white/10 bg-white/[0.025] px-6 py-3.5 text-sm font-semibold text-slate-200 transition hover:border-white/20 hover:bg-white/[0.06]"
            >
              I already have an account
            </button>
          </div>
        </div>

        {/* =================================================
            AI INTERVIEW VISUAL
        ================================================== */}

        <div className="landing-reveal landing-reveal-4 relative mx-auto w-full max-w-xl lg:pl-8">
          {/* Glow */}
          <div className="absolute inset-10 rounded-full bg-violet-400/15 blur-[90px]" />

          {/* Main card */}
          <div className="landing-visual-card relative rounded-3xl border border-white/[0.1] bg-[#11111b]/85 p-5 shadow-2xl backdrop-blur-xl">
            {/* Top bar */}
            <div className="flex items-center justify-between border-b border-white/[0.06] pb-4">
              <div>
                <div className="text-[9px] uppercase tracking-[0.25em] text-violet-300">
                  Live interview
                </div>

                <div className="mt-1 text-sm font-semibold">
                  Python · Technical
                </div>
              </div>

              <div className="flex items-center gap-2 rounded-full border border-emerald-400/10 bg-emerald-400/[0.05] px-3 py-1.5">
                <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-emerald-400" />
                <span className="text-[10px] text-emerald-300">
                  AI online
                </span>
              </div>
            </div>

            {/* AI listening state */}
            <div className="relative flex h-64 items-center justify-center">
              <div className="absolute h-48 w-48 animate-[spin_18s_linear_infinite] rounded-full border border-violet-400/10" />

              <div className="absolute h-36 w-36 rounded-full border border-violet-300/10" />

              <div className="absolute h-28 w-28 animate-pulse rounded-full bg-violet-500/10 blur-2xl" />

              <div className="relative flex h-24 w-24 items-center justify-center rounded-full border border-violet-300/30 bg-[#111326] shadow-[0_0_60px_rgba(167,139,250,0.2)]">
                <div className="h-4 w-4 animate-pulse rounded-full bg-violet-200 shadow-[0_0_22px_rgba(196,181,253,1)]" />
              </div>
            </div>

            <div className="mb-4 flex items-center gap-3 rounded-2xl border border-cyan-300/10 bg-cyan-300/[0.04] p-4">
              <div className="flex h-8 w-8 items-center justify-center rounded-full bg-cyan-300/10 text-cyan-200">
                ✦
              </div>
              <div>
                <div className="text-[9px] uppercase tracking-[0.2em] text-cyan-200/70">
                  AI interviewer
                </div>
                <p className="mt-1 text-xs text-slate-300">
                  Listening for your reasoning...
                </p>
              </div>
            </div>

            {/* Question */}
            <div className="rounded-2xl border border-white/[0.06] bg-black/20 p-5">
              <div className="mb-3 flex items-center justify-between">
                <span className="text-[9px] uppercase tracking-[0.2em] text-slate-600">
                  Question 03
                </span>

                <span className="rounded-full border border-violet-300/20 bg-violet-400/5 px-2.5 py-1 text-[9px] uppercase tracking-wider text-violet-300">
                  Medium
                </span>
              </div>

              <p className="text-base font-medium leading-7 text-slate-100">
                Explain the difference between a list and a tuple in Python.
              </p>

              {/* Fake waveform */}
              <div
                className="landing-waveform mt-5 flex h-8 items-center gap-1"
                aria-label="Active voice waveform"
              >
                {[
                  18, 28, 12, 24, 35, 17, 29, 40, 22, 31, 16, 27, 20, 34,
                ].map((height, index) => (
                  <span
                    key={index}
                    className="landing-wave-bar w-1 rounded-full bg-violet-200/70"
                    style={{
                      height: `${height}%`,
                      animationDelay: `${index * 80}ms`,
                    }}
                  />
                ))}
              </div>
            </div>

            {/* Bottom status */}
            <div className="mt-4 flex items-center justify-between px-1">
              <span className="text-[10px] text-slate-600">
                AI is evaluating your response
              </span>

              <span className="text-[10px] font-medium text-violet-300">
                75 / 100
              </span>
            </div>

            <div className="mt-4 border-t border-white/[0.06] pt-4 text-xs text-slate-400">
              <span className="text-emerald-300">Feedback ready</span>
              <span className="ml-2">
                Clear structure, add one concrete example.
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
