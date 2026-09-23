const stats = [
  { value: "3", label: "Difficulty levels" },
  { value: "AI", label: "Answer evaluation" },
  { value: "4", label: "Evaluation metrics" },
  { value: "∞", label: "Practice sessions" },
];

/**
 * Landing stats strip: the four headline numbers between hero
 * and features.
 */
export default function LandingStatsStrip() {
  return (
    <section className="border-y border-white/[0.06] bg-white/[0.015]">
      <div className="mx-auto grid max-w-7xl grid-cols-2 divide-x divide-white/[0.06] px-6 lg:grid-cols-4 lg:px-8">
        {stats.map((stat) => (
          <div key={stat.label} className="px-5 py-8 text-center">
            <div className="text-2xl font-semibold">{stat.value}</div>

            <div className="mt-1 text-xs text-slate-500">{stat.label}</div>
          </div>
        ))}
      </div>
    </section>
  );
}
