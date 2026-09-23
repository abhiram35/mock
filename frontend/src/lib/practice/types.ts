import type {
  CodingQuestion,
  CodeExecutionResponse,
  CodingSubmission,
  Difficulty,
} from "../api";

export type { CodingQuestion, Difficulty };

/** A subject track groups coding problems into a guided path. */
export interface PracticeTrack {
  /** Backend topic id, as a string. */
  id: string;

  /** Machine subject key, e.g. "dsa". */
  subject: string;

  /** Display name (the backend topic name). */
  name: string;

  /** One-line promise of the track. */
  tagline: string;

  /** CSS var for the subject accent, e.g. "var(--subject-dsa)". */
  color: string;

  /** Live count of problems in the track. */
  problemCount: number;

  /** True only when the backend sandbox executes this language. */
  executable: boolean;
}

/** Stage metadata for the 5-stage solve flow. */
export type SolveStageId =
  | "understand"
  | "plan"
  | "code"
  | "verify"
  | "reflect";

export const SOLVE_STAGES: Array<{
  id: SolveStageId;
  label: string;
  hint: string;
}> = [
  { id: "understand", label: "Understand", hint: "Restate the problem" },
  { id: "plan", label: "Plan", hint: "Pattern + complexity" },
  { id: "code", label: "Code", hint: "Write the solution" },
  { id: "verify", label: "Verify", hint: "Run the tests" },
  { id: "reflect", label: "Reflect", hint: "Compare and note" },
];

/** What the user declares before coding. */
export interface PlanState {
  pattern: string;
  timeComplexity: string;
  spaceComplexity: string;
  notes: string;
}

export const EMPTY_PLAN: PlanState = {
  pattern: "",
  timeComplexity: "",
  spaceComplexity: "",
  notes: "",
};

/** Local, per-problem progress through the stages. */
export interface SolveProgress {
  stage: SolveStageId;
  plan: PlanState;
  reflection: string;
  completedAt: Partial<Record<SolveStageId, number>>;
}

/** Narrated execution phases shown while code runs. */
export interface RunNarration {
  phase: "submitting" | "compiling" | "running" | "comparing" | "done";
  message: string;
}

export type PracticeRunResult = CodeExecutionResponse;

export type PracticeSubmission = CodingSubmission;
