const steps = [
  {
    number: "01",
    title: "Choose a topic",
    text: "Select the technical topic you want to practice.",
  },
  {
    number: "02",
    title: "Pick difficulty",
    text: "Start with easy, medium, or hard questions.",
  },
  {
    number: "03",
    title: "Answer",
    text: "Respond to questions as you would in a real interview.",
  },
  {
    number: "04",
    title: "Improve",
    text: "Review AI feedback and use it to improve your next attempt.",
  },
];

/**
 * Landing "how it works" section: the four-step process strip.
 */
export default function LandingHowItWorks() {
  return (
    <section
      id="how-it-works"
      className="border-y border-white/[0.06] bg-white/[0.015]"
    >
      <div className="mx-auto max-w-7xl px-6 py-28 lg:px-8">
        <div className="text-center">
          <div className="text-[10px] font-semibold uppercase tracking-[0.25em] text-violet-300">
            The process
          </div>

          <h2 className="mt-4 text-3xl font-semibold tracking-tight sm:text-4xl">
            From setup to feedback
          </h2>
        </div>

        <div className="mt-16 grid gap-10 md:grid-cols-4">
          {steps.map((step) => (
            <div key={step.number} className="relative">
              <div className="text-xs font-semibold tracking-[0.2em] text-violet-300">
                {step.number}
              </div>

              <h3 className="mt-4 text-lg font-semibold">{step.title}</h3>

              <p className="mt-3 text-sm leading-7 text-slate-500">
                {step.text}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
