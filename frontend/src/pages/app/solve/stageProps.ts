import type { CodingQuestion } from "../../../lib/api";

import type {
  PlanState,
  RunNarration,
  SolveProgress,
} from "../../../lib/practice/types";

export interface StageProps {
  problem: CodingQuestion;

  progress: SolveProgress;

  /** Advance to the next stage. */
  onNext: () => void;

  /** Jump directly to a stage (stage rail). */
  onJump: (stage: SolveProgress["stage"]) => void;
}

export interface PlanStageProps extends StageProps {
  onPlanChange: (plan: PlanState) => void;
}

export interface CodeStageProps extends StageProps {
  code: string;

  onCodeChange: (code: string) => void;

  onRun: () => void;

  onSubmit: () => void;

  runResult: import("../../../lib/api").CodeExecutionResponse | null;

  narration: RunNarration | null;

  isRunning: boolean;

  runError: string | null;

  onProceedToVerify: () => void;
}

export interface VerifyStageProps extends StageProps {
  runResult: import("../../../lib/api").CodeExecutionResponse | null;

  onBack: () => void;

  onNext: () => void;

  submitted: boolean;
}

export interface ReflectStageProps extends StageProps {
  onReflectionChange: (text: string) => void;

  onRestart: () => void;
}
