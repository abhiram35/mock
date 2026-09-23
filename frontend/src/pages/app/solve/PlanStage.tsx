import { ArrowLeft, ArrowRight, Sparkles, Zap } from "lucide-react";

import { Button, Card, Tooltip, Kbd } from "../../../components/primitives";
import type { PlanStageProps } from "./stageProps";

const PATTERNS = [
  "Hash map",
  "Two pointers",
  "Sliding window",
  "Stack",
  "Sorting",
  "Greedy",
  "Recursion",
  "Dynamic programming",
  "Prefix sum",
  "Simulation",
];

const COMPLEXITIES = ["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n²)", "O(2ⁿ)"];

function ChipGroup({
  options,
  value,
  onChange,
  allowCustom = true,
}: {
  options: string[];
  value: string;
  onChange: (next: string) => void;
  allowCustom?: boolean;
}) {
  return (
    <div className="flex flex-wrap gap-1.5">
      {options.map((option) => (
        <button
          key={option}
          type="button"
          onClick={() => onChange(option)}
          aria-pressed={value === option}
          className={`
            rounded-full border px-3 py-1 text-[12.5px] transition-colors
            ${
              value === option
                ? "border-accent-line bg-accent-soft font-medium text-accent"
                : "border-line-strong text-ink-2 hover:border-[color:var(--ink-3)] hover:text-ink"
            }
          `}
        >
          {option}
        </button>
      ))}

      {allowCustom && (
        <input
          value={options.includes(value) ? "" : value}
          onChange={(event) => onChange(event.target.value)}
          placeholder="or type your own…"
          aria-label="Custom value"
          className="
            w-36 rounded-full border border-dashed border-line-strong
            bg-transparent px-3 py-1 text-[12.5px] text-ink outline-none
            placeholder:text-ink-3 focus:border-accent
          "
        />
      )}
    </div>
  );
}

/**
 * PLAN — declare the approach and complexity BEFORE coding. The AI
 * nudge requires Gemini keys; until then the button explains itself
 * honestly instead of pretending.
 */
export default function PlanStage({
  progress,
  onPlanChange,
  onBack,
  onNext,
}: PlanStageProps & { onBack: () => void }) {
  const { plan } = progress;

  const canContinue = Boolean(
    plan.pattern.trim() && plan.timeComplexity.trim(),
  );

  return (
    <div className="grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
      <Card padding="lg">
        <h2 className="display text-xl text-ink">Choose your attack</h2>

        <p className="mt-1.5 text-sm leading-6 text-ink-2">
          Name the pattern before you name the variables.
        </p>

        <div className="mt-5 flex flex-col gap-6">
          <div>
            <p className="mb-2 text-[13px] font-medium text-ink-2">
              Approach
            </p>

            <ChipGroup
              options={PATTERNS}
              value={plan.pattern}
              onChange={(next) =>
                onPlanChange({ ...plan, pattern: next })
              }
            />
          </div>

          <div className="grid gap-5 sm:grid-cols-2">
            <div>
              <p className="mb-2 flex items-center gap-1.5 text-[13px] font-medium text-ink-2">
                <Zap size={13} aria-hidden="true" className="text-ink-3" />
                Time complexity
              </p>

              <ChipGroup
                options={COMPLEXITIES}
                value={plan.timeComplexity}
                onChange={(next) =>
                  onPlanChange({ ...plan, timeComplexity: next })
                }
                allowCustom={false}
              />
            </div>

            <div>
              <p className="mb-2 text-[13px] font-medium text-ink-2">
                Space complexity
              </p>

              <ChipGroup
                options={COMPLEXITIES}
                value={plan.spaceComplexity}
                onChange={(next) =>
                  onPlanChange({ ...plan, spaceComplexity: next })
                }
                allowCustom={false}
              />
            </div>
          </div>

          <div>
            <p className="mb-2 text-[13px] font-medium text-ink-2">
              Notes to your future self (optional)
            </p>

            <textarea
              value={plan.notes}
              onChange={(event) =>
                onPlanChange({ ...plan, notes: event.target.value })
              }
              placeholder="The trick is… watch out for…"
              aria-label="Plan notes"
              className="
                min-h-[72px] w-full resize-y rounded-lg border
                border-line-strong bg-paper-raised px-3 py-2.5 text-sm
                leading-6 text-ink outline-none transition-colors
                placeholder:text-ink-3 focus:border-accent
              "
            />
          </div>
        </div>
      </Card>

      <div className="flex flex-col gap-6">
        {/* Honest AI state — disabled until Gemini keys exist */}
        <Card padding="lg" className="border-dashed">
          <div className="flex items-center gap-2">
            <Sparkles size={14} className="text-ink-3" />

            <h3 className="text-[13px] font-medium text-ink-2">
              AI plan check
            </h3>

            <Tooltip
              content="Needs Gemini keys on the server — ask your admin to enable AI features."
              side="top"
            >
              <span className="ml-auto cursor-help text-[11px] text-ink-3 underline decoration-dotted">
                Why off?
              </span>
            </Tooltip>
          </div>

          <p className="mt-2 text-sm leading-6 text-ink-2">
            The interviewer would give your plan a quick sanity check and
            drop a hint if you're heading somewhere painful.
          </p>

          <Button
            variant="secondary"
            size="sm"
            className="mt-4"
            disabled
            title="AI features are unavailable — Gemini keys not configured"
          >
            Ask for a nudge
          </Button>
        </Card>

        <div className="mt-auto flex items-center justify-between">
          <Button variant="ghost" size="sm" icon={<ArrowLeft size={15} />} onClick={onBack}>
            Back
          </Button>

          <Tooltip content={<span className="flex items-center gap-1"><Kbd>Ctrl</Kbd>+<Kbd>↵</Kbd> from the editor</span>}>
            <span>
              <Button
                onClick={onNext}
                disabled={!canContinue}
                icon={<ArrowRight size={15} />}
              >
                Plan set — Code
              </Button>
            </span>
          </Tooltip>
        </div>
      </div>
    </div>
  );
}
