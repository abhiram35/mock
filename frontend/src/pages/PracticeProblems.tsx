import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  CodingLanguage,
  CodingQuestion,
  Difficulty,
  getCodingQuestions,
  getUserSolvedQuestionIds,
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

const LANGUAGE_LABELS: Record<string, string> = {
  python: "Python",
  javascript: "JavaScript",
  java: "Java",
  cpp: "C++",
};

export default function PracticeProblems() {
  const navigate = useNavigate();

  const [questions, setQuestions] = useState<CodingQuestion[]>([]);
  const [solvedIds, setSolvedIds] = useState<Set<number>>(new Set());
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Filters
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>("all");
  const [selectedLanguage, setSelectedLanguage] = useState<string>("all");
  const [statusFilter, setStatusFilter] = useState<"all" | "solved" | "unsolved">("all");

  useEffect(() => {
    async function loadData() {
      try {
        setLoading(true);
        setError(null);
        const [fetchedQuestions, fetchedSolvedIds] = await Promise.all([
          getCodingQuestions(),
          getUserSolvedQuestionIds().catch(() => []),
        ]);
        setQuestions(fetchedQuestions);
        setSolvedIds(new Set(fetchedSolvedIds));
      } catch (err: any) {
        setError(err.message || "Failed to load practice questions.");
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, []);

  const filteredQuestions = useMemo(() => {
    return questions.filter((q) => {
      // Search
      if (searchQuery.trim()) {
        const query = searchQuery.toLowerCase();
        const matchesTitle = q.title.toLowerCase().includes(query);
        const matchesStatement = q.problem_statement.toLowerCase().includes(query);
        if (!matchesTitle && !matchesStatement) return false;
      }

      // Difficulty
      if (selectedDifficulty !== "all" && q.difficulty !== selectedDifficulty) {
        return false;
      }

      // Language
      if (selectedLanguage !== "all" && q.language !== selectedLanguage) {
        return false;
      }

      // Solved status
      const isSolved = solvedIds.has(q.id);
      if (statusFilter === "solved" && !isSolved) return false;
      if (statusFilter === "unsolved" && isSolved) return false;

      return true;
    });
  }, [questions, solvedIds, searchQuery, selectedDifficulty, selectedLanguage, statusFilter]);

  const stats = useMemo(() => {
    const total = questions.length;
    const solved = questions.filter((q) => solvedIds.has(q.id)).length;
    const easyTotal = questions.filter((q) => q.difficulty === "easy").length;
    const easySolved = questions.filter((q) => q.difficulty === "easy" && solvedIds.has(q.id)).length;
    const mediumTotal = questions.filter((q) => q.difficulty === "medium").length;
    const mediumSolved = questions.filter((q) => q.difficulty === "medium" && solvedIds.has(q.id)).length;
    const hardTotal = questions.filter((q) => q.difficulty === "hard").length;
    const hardSolved = questions.filter((q) => q.difficulty === "hard" && solvedIds.has(q.id)).length;

    return {
      total,
      solved,
      easyTotal,
      easySolved,
      mediumTotal,
      mediumSolved,
      hardTotal,
      hardSolved,
    };
  }, [questions, solvedIds]);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 selection:bg-violet-500/30">
      {/* Top Header */}
      <header className="sticky top-0 z-30 border-b border-white/[0.08] bg-slate-950/80 backdrop-blur-md">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
          <div className="flex items-center gap-4">
            <button
              onClick={() => navigate("/home")}
              className="flex items-center gap-2 rounded-xl border border-white/10 bg-white/[0.03] px-3.5 py-1.5 text-xs font-medium text-slate-300 transition hover:border-white/20 hover:bg-white/[0.06]"
            >
              <span>←</span>
              <span>Back to Dashboard</span>
            </button>
            <div className="h-4 w-px bg-white/10" />
            <h1 className="font-display text-lg font-semibold tracking-tight text-white flex items-center gap-2.5">
              <span className="flex h-6 w-6 items-center justify-center rounded-lg bg-cyan-500/20 font-mono text-xs font-bold text-cyan-400 border border-cyan-500/30">
                {"</>"}
              </span>
              Practice Problems
            </h1>
          </div>

          <div className="flex items-center gap-3">
            <div className="rounded-full border border-emerald-400/20 bg-emerald-400/10 px-3.5 py-1 font-mono text-xs font-medium text-emerald-400">
              Solved: {stats.solved} / {stats.total}
            </div>
          </div>
        </div>
      </header>

      {/* Main Container */}
      <main className="mx-auto max-w-7xl px-6 py-8">
        {/* Progress Overview Hero Card */}
        <section className="mb-8 rounded-3xl border border-white/[0.08] bg-gradient-to-br from-violet-500/[0.08] via-slate-900/60 to-cyan-500/[0.05] p-6 shadow-xl md:p-8">
          <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">
            <div>
              <div className="font-mono text-[10px] uppercase tracking-[0.2em] text-cyan-400">
                Self-Serve Practice Bank
              </div>
              <h2 className="mt-2 text-2xl font-bold tracking-tight text-white sm:text-3xl">
                Master Algorithms & Data Structures
              </h2>
              <p className="mt-2 max-w-2xl text-sm leading-relaxed text-slate-400">
                Select a problem, test your solution against visible test cases with our Monaco code editor, and submit for full automated grading across hidden test suites.
              </p>
            </div>

            {/* Stat Counters */}
            <div className="grid grid-cols-3 gap-3">
              <div className="rounded-2xl border border-emerald-500/20 bg-emerald-500/[0.04] p-4 text-center">
                <div className="text-xs font-semibold uppercase tracking-wider text-emerald-400">Easy</div>
                <div className="mt-2 text-xl font-bold text-white">
                  {stats.easySolved} <span className="text-xs font-normal text-slate-500">/ {stats.easyTotal}</span>
                </div>
              </div>
              <div className="rounded-2xl border border-amber-500/20 bg-amber-500/[0.04] p-4 text-center">
                <div className="text-xs font-semibold uppercase tracking-wider text-amber-400">Medium</div>
                <div className="mt-2 text-xl font-bold text-white">
                  {stats.mediumSolved} <span className="text-xs font-normal text-slate-500">/ {stats.mediumTotal}</span>
                </div>
              </div>
              <div className="rounded-2xl border border-rose-500/20 bg-rose-500/[0.04] p-4 text-center">
                <div className="text-xs font-semibold uppercase tracking-wider text-rose-400">Hard</div>
                <div className="mt-2 text-xl font-bold text-white">
                  {stats.hardSolved} <span className="text-xs font-normal text-slate-500">/ {stats.hardTotal}</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Filters Bar */}
        <section className="mb-6 flex flex-col gap-4 rounded-2xl border border-white/[0.08] bg-slate-900/40 p-4 md:flex-row md:items-center md:justify-between">
          {/* Search */}
          <div className="relative flex-1 md:max-w-md">
            <span className="pointer-events-none absolute inset-y-0 left-3.5 flex items-center text-slate-500">
              🔍
            </span>
            <input
              type="text"
              placeholder="Search problem title or description..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full rounded-xl border border-white/10 bg-black/40 pl-10 pr-4 py-2 text-sm text-white placeholder-slate-500 transition focus:border-cyan-500/50 focus:outline-none focus:ring-1 focus:ring-cyan-500/50"
            />
          </div>

          {/* Dropdown Filters */}
          <div className="flex flex-wrap items-center gap-3">
            {/* Status Filter */}
            <select
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value as any)}
              className="rounded-xl border border-white/10 bg-slate-900 px-3 py-2 text-xs font-medium text-slate-300 focus:border-cyan-500/50 focus:outline-none"
            >
              <option value="all">Status: All</option>
              <option value="solved">Solved Only (✓)</option>
              <option value="unsolved">Unsolved</option>
            </select>

            {/* Difficulty Filter */}
            <select
              value={selectedDifficulty}
              onChange={(e) => setSelectedDifficulty(e.target.value)}
              className="rounded-xl border border-white/10 bg-slate-900 px-3 py-2 text-xs font-medium text-slate-300 focus:border-cyan-500/50 focus:outline-none"
            >
              <option value="all">Difficulty: All</option>
              <option value="easy">Easy</option>
              <option value="medium">Medium</option>
              <option value="hard">Hard</option>
            </select>

            {/* Language Filter */}
            <select
              value={selectedLanguage}
              onChange={(e) => setSelectedLanguage(e.target.value)}
              className="rounded-xl border border-white/10 bg-slate-900 px-3 py-2 text-xs font-medium text-slate-300 focus:border-cyan-500/50 focus:outline-none"
            >
              <option value="all">Language: All</option>
              <option value="python">Python</option>
              <option value="javascript">JavaScript</option>
              <option value="java">Java</option>
              <option value="cpp">C++</option>
            </select>
          </div>
        </section>

        {/* Problems List Table */}
        {loading ? (
          <div className="flex flex-col items-center justify-center rounded-2xl border border-white/[0.08] bg-slate-900/20 py-20">
            <div className="h-8 w-8 animate-spin rounded-full border-2 border-cyan-400 border-t-transparent" />
            <p className="mt-4 font-mono text-xs uppercase tracking-widest text-slate-400">Loading problem set...</p>
          </div>
        ) : error ? (
          <div className="rounded-2xl border border-rose-500/20 bg-rose-500/[0.05] p-6 text-center text-rose-300">
            <p className="text-sm font-medium">{error}</p>
            <button
              onClick={() => window.location.reload()}
              className="mt-4 rounded-xl bg-white/10 px-4 py-2 text-xs font-semibold text-white transition hover:bg-white/20"
            >
              Try Again
            </button>
          </div>
        ) : filteredQuestions.length === 0 ? (
          <div className="flex flex-col items-center justify-center rounded-2xl border border-dashed border-white/10 bg-slate-900/20 py-20 text-center">
            <span className="text-3xl">🔎</span>
            <h3 className="mt-3 text-base font-semibold text-white">No problems found</h3>
            <p className="mt-1 text-xs text-slate-500">
              Try adjusting your search query or filters.
            </p>
          </div>
        ) : (
          <div className="overflow-hidden rounded-2xl border border-white/[0.08] bg-slate-900/30 shadow-md">
            <table className="w-full text-left">
              <thead>
                <tr className="border-b border-white/[0.08] bg-white/[0.02] text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                  <th className="px-6 py-4">Status</th>
                  <th className="px-6 py-4">Title</th>
                  <th className="px-6 py-4">Difficulty</th>
                  <th className="px-6 py-4">Language</th>
                  <th className="px-6 py-4 text-right">Action</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-white/[0.06] text-sm">
                {filteredQuestions.map((q) => {
                  const isSolved = solvedIds.has(q.id);
                  const diff = DIFFICULTY_CONFIG[q.difficulty] || DIFFICULTY_CONFIG.easy;

                  return (
                    <tr
                      key={q.id}
                      onClick={() => navigate(`/practice/${q.id}`)}
                      className="group cursor-pointer transition hover:bg-white/[0.04]"
                    >
                      {/* Solved Status */}
                      <td className="whitespace-nowrap px-6 py-4">
                        {isSolved ? (
                          <span className="inline-flex items-center gap-1 rounded-full border border-emerald-400/30 bg-emerald-400/10 px-2.5 py-0.5 font-mono text-xs font-semibold text-emerald-400">
                            ✓ Solved
                          </span>
                        ) : (
                          <span className="font-mono text-xs text-slate-600">—</span>
                        )}
                      </td>

                      {/* Problem Title */}
                      <td className="px-6 py-4 font-medium text-white transition group-hover:text-cyan-300">
                        <div className="flex items-center gap-2">
                          <span>{q.title}</span>
                        </div>
                      </td>

                      {/* Difficulty Badge */}
                      <td className="whitespace-nowrap px-6 py-4">
                        <span
                          className={`inline-block rounded-full border px-2.5 py-0.5 font-mono text-[10px] uppercase tracking-wider ${diff.bg} ${diff.text} ${diff.border}`}
                        >
                          {diff.label}
                        </span>
                      </td>

                      {/* Supported Language */}
                      <td className="whitespace-nowrap px-6 py-4 font-mono text-xs text-slate-400">
                        {LANGUAGE_LABELS[q.language] || q.language}
                      </td>

                      {/* Action */}
                      <td className="whitespace-nowrap px-6 py-4 text-right">
                        <span className="inline-flex items-center gap-1 text-xs font-semibold text-cyan-400 transition group-hover:translate-x-0.5">
                          {isSolved ? "Practice Again" : "Solve"} →
                        </span>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </main>
    </div>
  );
}
