const features = [
  {
    number: "01",
    title: "Adaptive interviews",
    text: "Strong answers can increase the difficulty while weaker performance can bring the interview back to fundamentals.",
    accent: "violet" as const,
  },
  {
    number: "02",
    title: "Semantic AI evaluation",
    text: "Your answer is evaluated for technical correctness, relevance, communication, completeness, and practical understanding.",
    accent: "cyan" as const,
  },
  {
    number: "03",
    title: "Actionable feedback",
    text: "Receive scores, strengths, weaknesses, feedback, and recommendations after your answers and at the end of the interview.",
    accent: "purple" as const,
  },
];

const accentStyles = {
  violet: {
    border: "hover:border-violet-300/20",
    icon: "border-violet-300/20 bg-violet-400/10 text-violet-200",
  },
  cyan: {
    border: "hover:border-cyan-300/20",
    icon: "border-cyan-300/20 bg-cyan-400/10 text-cyan-200",
  },
  purple: {
    border: "hover:border-purple-300/20",
    icon: "border-purple-300/20 bg-purple-400/10 text-purple-200",
  },
};

/**
 * Landing features grid: the three numbered capability cards.
 */
export default function LandingFeatures() {
  return (
    <section id="features" className="mx-auto max-w-7xl px-6 py-28 lg:px-8">
      <div className="max-w-2xl">
        <div className="text-[10px] font-semibold uppercase tracking-[0.25em] text-violet-300">
          Built for better interviews
        </div>

        <h2 className="mt-4 text-3xl font-semibold tracking-tight sm:text-4xl">
          Not just questions.
          <span className="text-slate-500"> Real preparation.</span>
        </h2>

        <p className="mt-5 leading-7 text-slate-400">
          Every interview session is designed to help you understand what
          you know, where you struggle, and what you should improve.
        </p>
      </div>

      <div className="mt-14 grid gap-5 md:grid-cols-3">
        {features.map((feature) => {
          const accent = accentStyles[feature.accent];

          return (
            <div
              key={feature.number}
              className={`group rounded-2xl border border-white/[0.07] bg-white/[0.025] p-7 transition duration-300 hover:-translate-y-1 ${accent.border} hover:bg-white/[0.04]`}
            >
              <div
                className={`mb-8 flex h-11 w-11 items-center justify-center rounded-xl ${accent.icon}`}
              >
                {feature.number}
              </div>

              <h3 className="text-lg font-semibold">{feature.title}</h3>

              <p className="mt-3 text-sm leading-7 text-slate-500">
                {feature.text}
              </p>
            </div>
          );
        })}
      </div>
    </section>
  );
}
