import { Link } from "react-router-dom";
import {
  ArrowRight,
  Check,
  ListChecks,
  Play,
  Terminal,
} from "lucide-react";

import { Badge, Button, Card, Kbd } from "../../components/primitives";

/*
 * Landing, redesigned: editorial split layout, product previews
 * built from the real UI patterns (question card + workspace), and
 * copy that sounds like a person. No orbs were harmed.
 */

const STEPS = [
  {
    n: "01",
    title: "Understand before you type",
    body: "Restate the problem, walk an example, name the edge cases. Half of interview nerves is skipping this step.",
  },
  {
    n: "02",
    title: "Declare the plan",
    body: "Pick the pattern and state your complexity — before the editor opens. It's how seniors think out loud.",
  },
  {
    n: "03",
    title: "Code, verify, reflect",
    body: "Run real tests with honest diffs, then compare what you planned with what happened. That loop is the whole game.",
  },
];

function InterviewPreview() {
  return (
    <Card elevation="md" padding="none" className="overflow-hidden">
      <div className="flex items-center justify-between border-b border-line px-4 py-2.5">
        <span className="mono text-[10.5px] uppercase tracking-[0.12em] text-ink-3">
          Live interview · DBMS
        </span>

        <Badge tone="ok" dot>
          Evaluating
        </Badge>
      </div>

      <div className="px-4 py-4">
        <p className="text-[13px] leading-6 text-ink">
          <span className="mono text-[11px] text-ink-3">Q3 · </span>
          Explain the difference between a clustered and a non-clustered
          index. When would you pick each?
        </p>

        <div className="mt-3 space-y-1.5">
          <div className="flex items-center gap-2 text-[12.5px] text-[color:var(--ok)]">
            <Check size={13} /> Technical accuracy — covered B-tree lookup
          </div>

          <div className="flex items-center gap-2 text-[12.5px] text-ink-2">
            <span className="h-[13px] w-[13px] rounded-full border border-line-strong" />
            Checking completeness…
          </div>
        </div>

        <div className="mt-4 flex items-center gap-2 border-t border-line pt-3">
          <span className="mono tnum text-[11px] text-ink-3">score 78</span>

          <span className="ml-auto text-[11px] text-ink-3">
            next: harder question
          </span>
        </div>
      </div>
    </Card>
  );
}

function WorkspacePreview() {
  return (
    <Card elevation="md" padding="none" className="overflow-hidden">
      <div className="flex items-center justify-between border-b border-line px-4 py-2.5">
        <span className="mono text-[10.5px] uppercase tracking-[0.12em] text-ink-3">
          two_sum.py
        </span>

        <span className="flex items-center gap-1.5 text-[11px] text-ink-3">
          <Kbd>Ctrl</Kbd>
          <Kbd>↵</Kbd> run
        </span>
      </div>

      <pre className="overflow-x-auto bg-paper-sunken/50 px-4 py-3 font-mono text-[12px] leading-6 text-ink-2">
        <span className="text-[color:var(--accent)]">def</span> two_sum(nums, target):
          {"\n"}  seen = {"{}"}
          {"\n"}  {"\n"}  <span className="text-ink-3"># plan: O(n) time, O(n) space</span>
          {"\n"}  <span className="text-[color:var(--accent)]">for</span> i, v <span className="text-[color:var(--accent)]">in</span> enumerate(nums):
          {"\n"}    <span className="text-[color:var(--accent)]">if</span> target - v <span className="text-[color:var(--accent)]">in</span> seen:
          {"\n"}      <span className="text-[color:var(--accent)]">return</span> seen[target - v], i
          {"\n"}    seen[v] = i
      </pre>

      <div className="flex items-center gap-2 border-t border-line px-4 py-2.5">
        <Check size={13} className="text-[color:var(--ok)]" />

        <span className="text-[12.5px] text-ink-2">
          4/4 cases · expected vs actual matched
        </span>
      </div>
    </Card>
  );
}

export default function LandingV2() {
  return (
    <div className="app-root">
      {/* Nav */}
      <header className="rule-b sticky top-0 z-30 bg-paper/90 backdrop-blur">
        <div className="mx-auto flex h-14 w-full max-w-6xl items-center justify-between px-5">
          <span className="display text-[17px] font-semibold text-ink">
            Mock<span className="text-accent">.</span>
          </span>

          <nav className="hidden items-center gap-6 text-[13.5px] text-ink-2 md:flex">
            <a href="#how" className="transition-colors hover:text-ink">
              How it works
            </a>

            <a href="#practice" className="transition-colors hover:text-ink">
              Practice
            </a>
          </nav>

          <div className="flex items-center gap-2">
            <Link to="/login">
              <Button variant="ghost" size="sm">
                Sign in
              </Button>
            </Link>

            <Link to="/register">
              <Button size="sm">Start free</Button>
            </Link>
          </div>
        </div>
      </header>

      <main className="mx-auto w-full max-w-6xl px-5">
        {/* Hero: asymmetric editorial split */}
        <section className="grid items-center gap-12 py-16 md:grid-cols-[1.05fr_0.95fr] md:py-24">
          <div>
            <p className="mono text-[11px] uppercase tracking-[0.16em] text-ink-3">
              Mock interviews · coding practice
            </p>

            <h1 className="display mt-4 text-[clamp(38px,6vw,64px)] font-semibold leading-[1.04] text-ink">
              Practice the method,
              <br />
              not just the answers.
            </h1>

            <p className="mt-5 max-w-lg text-[16px] leading-8 text-ink-2">
              AI mock interviews that adapt to your answers, and a coding
              gym that teaches you to think in patterns — plan first, run
              real tests, learn from honest diffs.
            </p>

            <div className="mt-8 flex flex-wrap items-center gap-3">
              <Link to="/register">
                <Button size="lg" icon={<ArrowRight size={16} />}>
                  Create your account
                </Button>
              </Link>

              <Link to="/login">
                <Button size="lg" variant="secondary">
                  I have one already
                </Button>
              </Link>
            </div>

            <p className="mt-4 text-xs text-ink-3">
              Free while in development. No card, no spam — just practice.
            </p>
          </div>

          {/* Previews: intentionally offset, not a symmetric grid */}
          <div className="relative flex flex-col gap-4 md:pl-6">
            <div className="md:translate-x-6">
              <InterviewPreview />
            </div>

            <div className="md:-translate-x-2">
              <WorkspacePreview />
            </div>
          </div>
        </section>

        {/* How it works: numbered editorial rows, not cards */}
        <section id="how" className="rule-t py-16">
          <div className="max-w-2xl">
            <h2 className="display text-3xl text-ink md:text-4xl">
              The five-stage loop
            </h2>

            <p className="mt-3 text-[15px] leading-7 text-ink-2">
              Every coding problem moves through the same method. You
              keep the habit; the difficulty adapts.
            </p>
          </div>

          <ol className="mt-10 flex flex-col">
            {STEPS.map((step, index) => (
              <li
                key={step.n}
                className={`
                  grid gap-4 border-line py-6 md:grid-cols-[80px_1fr]
                  ${index > 0 ? "rule-t" : ""}
                `}
              >
                <span className="display tnum text-2xl text-accent">
                  {step.n}
                </span>

                <div className="max-w-xl">
                  <h3 className="text-[17px] font-semibold text-ink">
                    {step.title}
                  </h3>

                  <p className="mt-1.5 text-sm leading-7 text-ink-2">
                    {step.body}
                  </p>
                </div>
              </li>
            ))}
          </ol>
        </section>

        {/* Practice strip */}
        <section id="practice" className="rule-t py-16">
          <div className="grid items-center gap-10 md:grid-cols-[0.9fr_1.1fr]">
            <div>
              <h2 className="display text-3xl text-ink md:text-4xl">
                Tracks, not random problems
              </h2>

              <p className="mt-3 max-w-md text-[15px] leading-7 text-ink-2">
                Data structures, Python, DBMS and more — each track shows
                exactly what's inside before you commit. Python runs in a
                real sandbox today; other languages are labeled honestly
                until their runners land.
              </p>

              <ul className="mt-6 space-y-2.5 text-sm text-ink-2">
                <li className="flex items-center gap-2.5">
                  <ListChecks size={15} className="text-accent" />
                  Visible and hidden test cases, honest diffs
                </li>

                <li className="flex items-center gap-2.5">
                  <Terminal size={15} className="text-accent" />
                  Python 3.12 sandbox with time and memory limits
                </li>

                <li className="flex items-center gap-2.5">
                  <Play size={15} className="text-accent" />
                  Plan-first flow that builds interview instincts
                </li>
              </ul>
            </div>

            {/* Track list preview with subject marks */}
            <Card elevation="sm" padding="none" className="overflow-hidden">
              {[
                { name: "Data Structures & Algorithms", n: 5, color: "var(--subject-dsa)", live: true },
                { name: "Python", n: 0, color: "var(--subject-python)", live: false },
                { name: "DBMS", n: 0, color: "var(--subject-dbms)", live: false },
              ].map((track, index) => (
                <div
                  key={track.name}
                  className={`flex items-center gap-3 px-5 py-4 ${
                    index > 0 ? "border-t border-line" : ""
                  }`}
                >
                  <span
                    aria-hidden="true"
                    className="subject-mark"
                    style={{ ["--mark" as string]: track.color }}
                  />

                  <span className="flex-1 text-sm font-medium text-ink">
                    {track.name}
                  </span>

                  <span className="mono tnum text-[11px] text-ink-3">
                    {track.n} {track.n === 1 ? "problem" : "problems"}
                  </span>

                  {track.live ? (
                    <Badge tone="ok">Python sandbox</Badge>
                  ) : (
                    <Badge tone="warn">Soon</Badge>
                  )}
                </div>
              ))}
            </Card>
          </div>
        </section>

        {/* Final CTA */}
        <section className="rule-t py-16">
          <div className="flex flex-col items-start justify-between gap-6 md:flex-row md:items-center">
            <h2 className="display max-w-xl text-3xl text-ink md:text-4xl">
              Nervous is normal. Practiced is better.
            </h2>

            <Link to="/register" className="shrink-0">
              <Button size="lg" icon={<ArrowRight size={16} />}>
                Start practicing
              </Button>
            </Link>
          </div>
        </section>
      </main>

      <footer className="rule-t py-8">
        <div className="mx-auto flex w-full max-w-6xl items-center justify-between px-5 text-xs text-ink-3">
          <span>Mock. — interview practice, done properly.</span>

          <span>© {new Date().getFullYear()}</span>
        </div>
      </footer>
    </div>
  );
}
