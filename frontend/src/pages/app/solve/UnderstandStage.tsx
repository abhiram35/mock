import { useMemo, useState } from "react";
import { ArrowRight, CheckSquare, Square } from "lucide-react";

import { Button, Card } from "../../../components/primitives";
import type { StageProps } from "./stageProps";

/**
 * UNDERSTAND — restate the problem in your own words, walk one
 * example by hand, and tick off the edge cases you can name.
 */
export default function UnderstandStage({
  problem,
  onNext,
}: StageProps) {
  const [restatement, setRestatement] = useState("");

  const firstExamples = useMemo(() => {
    /*
     * The seeded `examples` format is a plain "Example 1: Input: ...
     * Output: ..." block. Show it verbatim in a mono panel —
     * parsing it further would guess at formats the backend owns.
     */
    return problem.examples || "No worked example provided.";
  }, [problem.examples]);

  const [checked, setChecked] = useState<Record<string, boolean>>({});

  const edgeCases = [
    "Empty input",
    "Single element",
    "Duplicates",
    "Negative numbers",
    "Very large input",
  ];

  const allTicked = Object.values(checked).filter(Boolean).length >= 2;

  function toggle(name: string) {
    setChecked((current) => ({ ...current, [name]: !current[name] }));
  }

  return (
    <div className="grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
      <Card padding="lg">
        <h2 className="display text-xl text-ink">Say it back</h2>

        <p className="mt-1.5 text-sm leading-6 text-ink-2">
          In one or two sentences: what is this problem really asking?
          (Interviewers love this. So do we.)
        </p>

        <textarea
          value={restatement}
          onChange={(event) => setRestatement(event.target.value)}
          placeholder="Given an array of numbers and a target, return…"
          aria-label="Your restatement of the problem"
          className="
            mt-4 min-h-[96px] w-full resize-y rounded-lg border
            border-line-strong bg-paper-raised px-3 py-2.5 text-sm
            leading-6 text-ink outline-none transition-colors
            placeholder:text-ink-3 focus:border-accent
          "
        />

        <div className="mt-6">
          <h3 className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
            Walk the first example
          </h3>

          <pre className="mt-2 overflow-x-auto rounded-lg border border-line bg-paper-sunken/60 p-4 font-mono text-[12.5px] leading-6 text-ink-2">
            {firstExamples}
          </pre>
        </div>
      </Card>

      <div className="flex flex-col gap-6">
        <Card padding="lg">
          <h3 className="mono text-[11px] uppercase tracking-[0.14em] text-ink-3">
            Edge cases you can name
          </h3>

          <ul className="mt-3 flex flex-col gap-1">
            {edgeCases.map((name) => (
              <li key={name}>
                <button
                  type="button"
                  onClick={() => toggle(name)}
                  className="flex w-full items-center gap-2.5 rounded-lg px-2 py-1.5 text-left text-sm text-ink-2 transition-colors hover:bg-accent-soft hover:text-ink"
                >
                  {checked[name] ? (
                    <CheckSquare size={15} className="text-accent" />
                  ) : (
                    <Square size={15} className="text-ink-3" />
                  )}

                  {name}
                </button>
              </li>
            ))}
          </ul>

          <p className="mt-3 text-xs text-ink-3">
            Tick at least two to move on — naming edge cases is half the
            solution.
          </p>
        </Card>

        <div className="mt-auto flex justify-end">
          <Button
            onClick={onNext}
            disabled={!restatement.trim() || !allTicked}
            icon={<ArrowRight size={15} />}
          >
            I understand it — Plan
          </Button>
        </div>
      </div>
    </div>
  );
}
