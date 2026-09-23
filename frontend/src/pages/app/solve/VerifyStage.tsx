import { ArrowLeft, ArrowRight, Check, X } from "lucide-react";

import { Badge, Button, Card, EmptyState } from "../../../components/primitives";
import type { VerifyStageProps } from "./stageProps";
import type { TestCaseResult } from "../../../lib/api";

function TestCaseRow({ result }: { result: TestCaseResult }) {
  const passed = result.passed;

  return (
    <div
      className={`
        rounded-lg border px-4 py-3
        ${
          passed
            ? "border-[color:var(--ok)] bg-[color:var(--ok-soft)]"
            : "border-[color:var(--bad)] bg-[color:var(--bad-soft)]"
        }
      `}
    >
      <div className="flex items-center gap-2">
        {passed ? (
          <Check size={14} className="text-[color:var(--ok)]" />
        ) : (
          <X size={14} className="text-[color:var(--bad)]" />
        )}

        <span className="text-[13px] font-medium text-ink">
          Case {result.test_case_number}
        </span>

        {result.is_hidden && (
          <Badge tone="neutral">hidden</Badge>
        )}

        {typeof result.execution_time_ms === "number" && (
          <span className="tnum ml-auto text-[11px] text-ink-3">
            {result.execution_time_ms} ms
          </span>
        )}
      </div>

      {!passed && (
        <div className="mt-3 grid gap-2 font-mono text-[12px] leading-5 sm:grid-cols-2">
          <div className="rounded-md border border-line bg-paper-raised p-2.5">
            <p className="text-[10px] uppercase tracking-[0.12em] text-ink-3">
              Expected
            </p>

            <pre className="mt-1 whitespace-pre-wrap text-ink">
              {result.expected_output ?? "—"}
            </pre>
          </div>

          <div className="rounded-md border border-line bg-paper-raised p-2.5">
            <p className="text-[10px] uppercase tracking-[0.12em] text-ink-3">
              Your output
            </p>

            <pre className="mt-1 whitespace-pre-wrap text-ink">
              {result.actual_output ?? "—"}
            </pre>
          </div>

          {result.error && (
            <p className="sm:col-span-2 text-[color:var(--bad)]">
              {result.error}
            </p>
          )}
        </div>
      )}

      {passed && result.input_data && (
        <pre className="mt-2 overflow-x-auto font-mono text-[11.5px] text-ink-3">
          {result.input_data}
        </pre>
      )}
    </div>
  );
}

/**
 * VERIFY — visible results first, then hidden. Failures show
 * expected-vs-actual side by side; hidden cases never leak data.
 */
export default function VerifyStage({
  runResult,
  submitted,
  onBack,
  onNext,
}: VerifyStageProps & { onBack: () => void }) {
  const results = runResult?.results ?? [];

  const total = runResult?.total_test_cases ?? 0;

  const passedCount = runResult?.passed_test_cases ?? 0;

  const allPassed = runResult?.success === true;

  return (
    <div className="flex flex-col gap-4">
      {runResult ? (
        <>
          {/* Verdict banner */}
          <div
            className={`
              flex items-center gap-3 rounded-xl border px-5 py-4
              ${
                allPassed
                  ? "border-[color:var(--ok)] bg-[color:var(--ok-soft)]"
                  : "border-[color:var(--bad)] bg-[color:var(--bad-soft)]"
              }
            `}
          >
            {allPassed ? (
              <Check size={16} className="text-[color:var(--ok)]" />
            ) : (
              <X size={16} className="text-[color:var(--bad)]" />
            )}

            <span className="text-sm font-medium text-ink">
              {allPassed
                ? submitted
                  ? `All ${total} cases passed — solution recorded.`
                  : `All ${total} cases passed. Submit to record it.`
                : `${passedCount} of ${total} cases passing.`}
            </span>

            <span className="tnum ml-auto text-xs text-ink-2">
              {total ? Math.round((passedCount / total) * 100) : 0}%
            </span>
          </div>

          <div className="flex flex-col gap-2.5">
            {results.map((result) => (
              <TestCaseRow key={result.test_case_number} result={result} />
            ))}
          </div>
        </>
      ) : (
        <Card padding="lg">
          <EmptyState
            title="No run yet"
            description="Head back to the editor and run your solution — results will land here, visible cases first."
          />
        </Card>
      )}

      <div className="mt-2 flex items-center justify-between">
        <Button variant="ghost" size="sm" icon={<ArrowLeft size={15} />} onClick={onBack}>
          Back to code
        </Button>

        <Button
          onClick={onNext}
          disabled={!runResult}
          icon={<ArrowRight size={15} />}
        >
          {allPassed ? "Next: Reflect" : "Continue anyway"}
        </Button>
      </div>
    </div>
  );
}
