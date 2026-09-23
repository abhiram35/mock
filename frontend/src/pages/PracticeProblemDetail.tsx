import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Editor from "@monaco-editor/react";
import {
  CodeExecutionResponse,
  CodingQuestion,
  CodingSubmission,
  Difficulty,
  getCodingQuestion,
  getQuestionSubmissions,
  runCode,
  submitCode,
} from "../lib/api";

const DIFFICULTY_CONFIG: Record<
  Difficulty,
  { label: string; bg: string; text: string; border: string }
> = {
  easy: {
    label: "Easy",
    bg: "bg-emerald-400/10",
    text: "text-emerald-400",
    border: "border-emerald-400/20",
  },
  medium: {
    label: "Medium",
    bg: "bg-amber-400/10",
    text: "text-amber-400",
    border: "border-amber-400/20",
  },
  hard: {
    label: "Hard",
    bg: "bg-rose-400/10",
    text: "text-rose-400",
    border: "border-rose-400/20",
  },
};

const STARTER_CODE_TEMPLATES: Record<string, string> = {
  python: `# Write your Python solution below\ndef solve():\n    pass\n\nif __name__ == '__main__':\n    solve()\n`,
  javascript: `// Write your JavaScript solution below\nconst fs = require('fs');\n\nfunction solve() {\n    const input = fs.readFileSync(0, 'utf-8').trim();\n    console.log(input);\n}\n\nsolve();\n`,
  java: `// Write your Java solution below\nimport java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Read input\n    }\n}\n`,
  cpp: `// Write your C++ solution below\n#include <iostream>\nusing namespace std;\n\nint main() {\n    // Read input\n    return 0;\n}\n`,
};

export default function PracticeProblemDetail() {
  const { questionId } = useParams<{ questionId: string }>();
  const navigate = useNavigate();

  const [question, setQuestion] = useState<CodingQuestion | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Editor State
  const [language, setLanguage] = useState<string>("python");
  const [code, setCode] = useState<string>("");

  // Execution State
  const [isRunning, setIsRunning] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [executionResult, setExecutionResult] =
    useState<CodeExecutionResponse | null>(null);
  const [activeTab, setActiveTab] = useState<"results" | "submissions">(
    "results",
  );
  const [submissions, setSubmissions] = useState<CodingSubmission[]>([]);
  const [isConsoleOpen, setIsConsoleOpen] = useState(true);
  const [activeTestCaseTab, setActiveTestCaseTab] = useState(0);

  useEffect(() => {
    async function loadQuestion() {
      if (!questionId) return;
      try {
        setLoading(true);
        setError(null);
        const data = await getCodingQuestion(Number(questionId));
        setQuestion(data);
        setLanguage(data.language || "python");
        setCode(
          data.starter_code || STARTER_CODE_TEMPLATES[data.language] || "",
        );

        // Load submission history
        loadSubmissions(data.id);
      } catch (err: any) {
        setError(err.message || "Failed to load question details.");
      } finally {
        setLoading(false);
      }
    }

    loadQuestion();
  }, [questionId]);

  async function loadSubmissions(qid: number) {
    try {
      const history = await getQuestionSubmissions(qid);
      setSubmissions(history);
    } catch {
      // Non-blocking
    }
  }

  const handleLanguageChange = (newLang: string) => {
    setLanguage(newLang);
    // If current code is empty or matches default, give template
    if (!code.trim() || Object.values(STARTER_CODE_TEMPLATES).includes(code)) {
      setCode(STARTER_CODE_TEMPLATES[newLang] || "");
    }
  };

  const handleRun = async () => {
    if (!question) return;
    try {
      setIsRunning(true);
      setIsConsoleOpen(true);
      setActiveTab("results");
      setActiveTestCaseTab(0);
      const res = await runCode(question.id, code);
      setExecutionResult(res);
    } catch (err: any) {
      alert(`Run failed: ${err.message}`);
    } finally {
      setIsRunning(false);
    }
  };

  const handleSubmit = async () => {
    if (!question) return;
    try {
      setIsSubmitting(true);
      setIsConsoleOpen(true);
      setActiveTab("results");
      setActiveTestCaseTab(0);
      const res = await submitCode(question.id, code);
      setExecutionResult(res);
      // Reload submission history
      loadSubmissions(question.id);
    } catch (err: any) {
      alert(`Submission failed: ${err.message}`);
    } finally {
      setIsSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-slate-950 text-white">
        <div className="flex flex-col items-center gap-3">
          <div className="h-8 w-8 animate-spin rounded-full border-2 border-cyan-400 border-t-transparent" />
          <p className="font-mono text-xs uppercase tracking-widest text-slate-400">
            Loading problem workspace...
          </p>
        </div>
      </div>
    );
  }

  if (error || !question) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center bg-slate-950 px-6 text-center text-white">
        <div className="max-w-md rounded-2xl border border-rose-500/20 bg-rose-500/[0.05] p-6">
          <h2 className="text-lg font-semibold text-rose-300">
            Problem Not Found
          </h2>
          <p className="mt-2 text-sm text-slate-400">
            {error || "Could not retrieve question."}
          </p>
          <button
            onClick={() => navigate("/practice")}
            className="mt-5 rounded-xl bg-white/10 px-4 py-2 text-xs font-semibold text-white transition hover:bg-white/20"
          >
            ← Back to Problems
          </button>
        </div>
      </div>
    );
  }

  const diff = DIFFICULTY_CONFIG[question.difficulty] || DIFFICULTY_CONFIG.easy;

  return (
    <div className="flex h-screen flex-col bg-slate-950 text-slate-100 overflow-hidden">
      {/* Top Header */}
      <header className="flex h-14 shrink-0 items-center justify-between border-b border-white/[0.08] bg-slate-950/90 px-6">
        <div className="flex items-center gap-4">
          <button
            onClick={() => navigate("/practice")}
            className="flex items-center gap-2 rounded-xl border border-white/10 bg-white/[0.03] px-3 py-1.5 text-xs font-medium text-slate-300 transition hover:border-white/20 hover:bg-white/[0.06]"
          >
            <span>←</span>
            <span>Problem List</span>
          </button>
          <div className="h-4 w-px bg-white/10" />
          <span className="font-medium text-sm text-white truncate max-w-sm sm:max-w-md">
            {question.title}
          </span>
          <span
            className={`rounded-full border px-2.5 py-0.5 font-mono text-[10px] uppercase tracking-wider ${diff.bg} ${diff.text} ${diff.border}`}
          >
            {diff.label}
          </span>
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-3">
          {/* Language Selector */}
          <select
            value={language}
            onChange={(e) => handleLanguageChange(e.target.value)}
            className="rounded-xl border border-white/10 bg-slate-900 px-3 py-1.5 font-mono text-xs text-cyan-300 focus:border-cyan-500/50 focus:outline-none"
          >
            <option value="python">Python 3.12</option>
            <option value="javascript">JavaScript (Node 20)</option>
            <option value="java">Java (OpenJDK 21)</option>
            <option value="cpp">C++ (GCC)</option>
          </select>

          {/* Run Button */}
          <button
            onClick={handleRun}
            disabled={isRunning || isSubmitting}
            className="flex items-center gap-1.5 rounded-xl border border-white/15 bg-white/[0.05] px-4 py-1.5 text-xs font-semibold text-white transition hover:bg-white/10 disabled:opacity-50"
          >
            {isRunning ? (
              <span className="inline-block h-3 w-3 animate-spin rounded-full border border-white border-t-transparent" />
            ) : (
              <span>▶</span>
            )}
            <span>Run</span>
          </button>

          {/* Submit Button */}
          <button
            onClick={handleSubmit}
            disabled={isRunning || isSubmitting}
            className="flex items-center gap-1.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 px-4 py-1.5 text-xs font-semibold text-slate-950 shadow-md shadow-emerald-500/20 transition hover:from-emerald-400 hover:to-teal-400 disabled:opacity-50"
          >
            {isSubmitting ? (
              <span className="inline-block h-3 w-3 animate-spin rounded-full border border-slate-950 border-t-transparent" />
            ) : (
              <span>🚀</span>
            )}
            <span>Submit</span>
          </button>
        </div>
      </header>

      {/* Main Workspace (Two Panes) */}
      <div className="flex flex-1 flex-col overflow-hidden lg:flex-row">
        {/* Left Pane: Problem Description */}
        <div className="flex flex-1 flex-col overflow-y-auto border-b border-white/[0.08] p-6 lg:border-b-0 lg:border-r lg:max-w-[48%]">
          <div className="mb-6">
            <h1 className="text-2xl font-bold tracking-tight text-white">
              {question.title}
            </h1>
            <div className="mt-2 flex items-center gap-2">
              <span className="font-mono text-xs text-slate-400">
                Language template:
              </span>
              <span className="font-mono text-xs text-cyan-400 uppercase">
                {question.language}
              </span>
            </div>
          </div>

          <div className="space-y-6 text-sm text-slate-300">
            {/* Problem Statement */}
            <div>
              <h2 className="mb-2 font-mono text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                Problem Description
              </h2>
              <div className="rounded-xl border border-white/[0.06] bg-slate-900/40 p-4 leading-relaxed whitespace-pre-wrap">
                {question.problem_statement}
              </div>
            </div>

            {/* Input Format */}
            <div>
              <h2 className="mb-2 font-mono text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                Input Format
              </h2>
              <div className="rounded-xl border border-white/[0.06] bg-slate-900/40 p-4 font-mono text-xs text-slate-300 whitespace-pre-wrap">
                {question.input_format}
              </div>
            </div>

            {/* Output Format */}
            <div>
              <h2 className="mb-2 font-mono text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                Output Format
              </h2>
              <div className="rounded-xl border border-white/[0.06] bg-slate-900/40 p-4 font-mono text-xs text-slate-300 whitespace-pre-wrap">
                {question.output_format}
              </div>
            </div>

            {/* Constraints */}
            <div>
              <h2 className="mb-2 font-mono text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                Constraints
              </h2>
              <div className="rounded-xl border border-white/[0.06] bg-slate-900/40 p-4 font-mono text-xs text-amber-300/90 whitespace-pre-wrap">
                {question.constraints}
              </div>
            </div>

            {/* Examples */}
            <div>
              <h2 className="mb-2 font-mono text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                Examples
              </h2>
              <div className="rounded-xl border border-white/[0.06] bg-slate-900/40 p-4 font-mono text-xs text-cyan-300 whitespace-pre-wrap">
                {question.examples}
              </div>
            </div>
          </div>
        </div>

        {/* Right Pane: Monaco Code Editor + Collapsible Console */}
        <div className="flex flex-1 flex-col overflow-hidden bg-[#1e1e1e]">
          {/* Monaco Editor Container */}
          <div className="flex-1 overflow-hidden">
            <Editor
              height="100%"
              language={language === "cpp" ? "cpp" : language}
              theme="vs-dark"
              value={code}
              onChange={(value) => setCode(value || "")}
              options={{
                minimap: { enabled: false },
                fontSize: 14,
                lineNumbers: "on",
                automaticLayout: true,
                scrollBeyondLastLine: false,
                tabSize: 4,
                fontFamily:
                  "Fira Code, Menlo, Monaco, 'Courier New', monospace",
              }}
            />
          </div>

          {/* Console / Output Drawer */}
          <div
            className={`border-t border-white/[0.1] bg-slate-900 transition-all duration-300 flex flex-col ${
              isConsoleOpen ? "h-64 sm:h-72" : "h-10"
            }`}
          >
            {/* Console Bar */}
            <div className="flex h-10 shrink-0 items-center justify-between border-b border-white/[0.08] bg-slate-950/80 px-4">
              <div className="flex items-center gap-2">
                <button
                  onClick={() => {
                    setIsConsoleOpen(true);
                    setActiveTab("results");
                  }}
                  className={`border-b-2 px-3 py-2 text-xs font-semibold transition ${
                    activeTab === "results"
                      ? "border-cyan-400 text-cyan-400"
                      : "border-transparent text-slate-400 hover:text-white"
                  }`}
                >
                  Test Results
                </button>
                <button
                  onClick={() => {
                    setIsConsoleOpen(true);
                    setActiveTab("submissions");
                  }}
                  className={`border-b-2 px-3 py-2 text-xs font-semibold transition ${
                    activeTab === "submissions"
                      ? "border-cyan-400 text-cyan-400"
                      : "border-transparent text-slate-400 hover:text-white"
                  }`}
                >
                  Submissions ({submissions.length})
                </button>
              </div>

              <button
                onClick={() => setIsConsoleOpen(!isConsoleOpen)}
                className="text-xs text-slate-400 hover:text-white"
              >
                {isConsoleOpen ? "▼ Collapse" : "▲ Expand Console"}
              </button>
            </div>

            {/* Console Content */}
            {isConsoleOpen && (
              <div className="flex-1 overflow-y-auto p-4 text-xs font-mono">
                {activeTab === "results" ? (
                  !executionResult ? (
                    <div className="flex h-full items-center justify-center text-slate-500">
                      Run your code against test cases or submit your solution
                      for verdict.
                    </div>
                  ) : (
                    <div>
                      {/* Verdict Banner */}
                      <div
                        className={`mb-4 flex items-center justify-between rounded-xl border p-3 ${
                          executionResult.success
                            ? "border-emerald-400/30 bg-emerald-500/10 text-emerald-300"
                            : "border-rose-400/30 bg-rose-500/10 text-rose-300"
                        }`}
                      >
                        <div className="flex items-center gap-2">
                          <span className="text-base font-bold">
                            {executionResult.success
                              ? "✓ Accepted"
                              : "✗ Wrong Answer / Execution Error"}
                          </span>
                          {executionResult.status && (
                            <span className="rounded-md bg-white/10 px-2 py-0.5 text-[10px] uppercase">
                              Status: {executionResult.status}
                            </span>
                          )}
                        </div>
                        <div className="text-slate-400">
                          Passed: {executionResult.passed_test_cases} /{" "}
                          {executionResult.total_test_cases} test cases
                        </div>
                      </div>

                      {/* Test Case Tabs */}
                      <div className="mb-3 flex flex-wrap gap-2 border-b border-white/[0.08] pb-2">
                        {executionResult.results.map((r, i) => (
                          <button
                            key={i}
                            onClick={() => setActiveTestCaseTab(i)}
                            className={`flex items-center gap-1.5 rounded-lg px-2.5 py-1 text-xs font-medium transition ${
                              activeTestCaseTab === i
                                ? "bg-white/10 text-white"
                                : "text-slate-400 hover:bg-white/[0.05]"
                            }`}
                          >
                            <span
                              className={`h-2 w-2 rounded-full ${
                                r.passed ? "bg-emerald-400" : "bg-rose-400"
                              }`}
                            />
                            <span>
                              Case {r.test_case_number}{" "}
                              {r.is_hidden ? "(Hidden)" : ""}
                            </span>
                          </button>
                        ))}
                      </div>

                      {/* Active Case Detail */}
                      {executionResult.results[activeTestCaseTab] && (
                        <div className="space-y-3 rounded-xl border border-white/[0.06] bg-black/40 p-3">
                          {executionResult.results[activeTestCaseTab]
                            .is_hidden ? (
                            <div className="text-slate-400">
                              <p className="font-semibold text-slate-300">
                                Hidden Test Case
                              </p>
                              <p className="mt-1 text-[11px] text-slate-500">
                                Hidden test cases are evaluated during
                                submission. Test inputs and expected outputs are
                                hidden to verify general algorithmic
                                correctness.
                              </p>
                              {executionResult.results[activeTestCaseTab]
                                .error && (
                                <p className="mt-2 text-rose-400">
                                  {
                                    executionResult.results[activeTestCaseTab]
                                      .error
                                  }
                                </p>
                              )}
                            </div>
                          ) : (
                            <>
                              <div>
                                <span className="text-slate-500">Input:</span>
                                <pre className="mt-1 rounded bg-black/50 p-2 text-slate-300">
                                  {executionResult.results[activeTestCaseTab]
                                    .input_data || "(empty)"}
                                </pre>
                              </div>
                              <div>
                                <span className="text-slate-500">
                                  Expected Output:
                                </span>
                                <pre className="mt-1 rounded bg-black/50 p-2 text-emerald-400">
                                  {executionResult.results[activeTestCaseTab]
                                    .expected_output || "(empty)"}
                                </pre>
                              </div>
                              <div>
                                <span className="text-slate-500">
                                  Your Output:
                                </span>
                                <pre className="mt-1 rounded bg-black/50 p-2 text-cyan-300">
                                  {executionResult.results[activeTestCaseTab]
                                    .actual_output || "(empty)"}
                                </pre>
                              </div>
                              {executionResult.results[activeTestCaseTab]
                                .error && (
                                <div>
                                  <span className="text-rose-400 font-semibold">
                                    Error:
                                  </span>
                                  <pre className="mt-1 rounded bg-rose-950/30 p-2 text-rose-300">
                                    {
                                      executionResult.results[activeTestCaseTab]
                                        .error
                                    }
                                  </pre>
                                </div>
                              )}
                            </>
                          )}
                          <div className="text-[10px] text-slate-500">
                            Execution time:{" "}
                            {executionResult.results[activeTestCaseTab]
                              .execution_time_ms
                              ? `${executionResult.results[activeTestCaseTab].execution_time_ms!.toFixed(1)} ms`
                              : "N/A"}
                          </div>
                        </div>
                      )}
                    </div>
                  )
                ) : (
                  // Submissions History Tab
                  <div className="space-y-2">
                    {submissions.length === 0 ? (
                      <div className="text-center py-8 text-slate-500">
                        No submissions yet. Submit your code to build your track
                        record!
                      </div>
                    ) : (
                      submissions.map((sub) => (
                        <div
                          key={sub.id}
                          className="flex items-center justify-between rounded-xl border border-white/[0.06] bg-black/30 p-3"
                        >
                          <div className="flex items-center gap-3">
                            <span
                              className={`rounded-full px-2.5 py-0.5 text-[10px] font-semibold uppercase ${
                                sub.status === "solved"
                                  ? "bg-emerald-400/10 text-emerald-400 border border-emerald-400/20"
                                  : "bg-rose-400/10 text-rose-400 border border-rose-400/20"
                              }`}
                            >
                              {sub.status === "solved"
                                ? "✓ Accepted"
                                : "✗ Attempted"}
                            </span>
                            <span className="text-slate-400 uppercase font-mono">
                              {sub.language}
                            </span>
                          </div>
                          <div className="text-slate-500 text-[11px]">
                            {new Date(sub.submitted_at).toLocaleString()}
                          </div>
                        </div>
                      ))
                    )}
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
