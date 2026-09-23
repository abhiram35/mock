import {
  getCodingQuestions,
  getCodingQuestion,
  getTopics,
  getQuestionSubmissions,
  getUserSolvedQuestionIds,
  runCode,
  submitCode,
} from "../api";

import type {
  PracticeRunResult,
  PracticeTrack,
  SolveProgress,
} from "./types";

/*
 * Subject identity for tracks. The backend executes Python only, so
 * `executable` is derived from the question language — non-Python
 * tracks render honestly as "coming soon", never faked.
 */

const SUBJECT_BY_NAME: Array<{
  match: RegExp;
  subject: string;
  color: string;
  tagline: string;
}> = [
  {
    match: /data structures|algorithms|dsa/i,
    subject: "dsa",
    color: "var(--subject-dsa)",
    tagline: "Patterns first, then the code.",
  },
  {
    match: /python/i,
    subject: "python",
    color: "var(--subject-python)",
    tagline: "Think in Python, cleanly.",
  },
  {
    match: /java/i,
    subject: "java",
    color: "var(--subject-java)",
    tagline: "Collections, classes, control.",
  },
  {
    match: /dbms|database|sql/i,
    subject: "dbms",
    color: "var(--subject-dbms)",
    tagline: "Data modeled properly.",
  },
  {
    match: /operating|os\b/i,
    subject: "os",
    color: "var(--subject-os)",
    tagline: "Processes, memory, order.",
  },
  {
    match: /network|cn\b/i,
    subject: "cn",
    color: "var(--subject-cn)",
    tagline: "How machines talk.",
  },
  {
    match: /software|swe|engineering/i,
    subject: "swe",
    color: "var(--subject-swe)",
    tagline: "Ship code that lasts.",
  },
];

function identityForTopic(name: string) {
  return (
    SUBJECT_BY_NAME.find((entry) => entry.match.test(name)) ?? {
      subject: "general",
      color: "var(--accent)",
      tagline: "Practice with intent.",
    }
  );
}

/**
 * Practice data layer.
 *
 * Narrow async interface over the EXISTING `lib/api.ts` endpoints —
 * the same calls the current practice pages make. No API behavior
 * changes. (Swap point for mock data during design iteration: every
 * consumer goes through this object, never through `lib/api`.)
 */
export const practiceClient = {
  /**
   * Tracks = backend topics that actually contain coding questions.
   * Derived from live data so the UI can never show a fake/empty
   * track. Counts come from the questions endpoint.
   */
  async listTracks(): Promise<PracticeTrack[]> {
    const [topics, questions] = await Promise.all([
      getTopics(),
      getCodingQuestions(),
    ]);

    const countByTopic = new Map<number, { count: number; language: string }>();

    questions.forEach((question) => {
      const entry = countByTopic.get(question.topic_id);

      const language = question.language;

      countByTopic.set(question.topic_id, {
        count: (entry?.count ?? 0) + 1,
        language: entry?.language ?? language,
      });
    });

    const tracks: PracticeTrack[] = [];

    topics.forEach((topic) => {
      const stats = countByTopic.get(topic.id);

      if (!topic.is_active || !stats) {
        return;
      }

      const identity = identityForTopic(topic.name);

      tracks.push({
        id: String(topic.id),
        subject: identity.subject,
        name: topic.name,
        tagline: identity.tagline,
        color: identity.color,
        problemCount: stats.count,
        executable: stats.language === "python",
      });
    });

    return tracks;
  },

  async listProblems(trackId?: string): Promise<
    Awaited<ReturnType<typeof getCodingQuestions>>
  > {
    return getCodingQuestions(
      trackId !== undefined ? Number(trackId) : undefined,
    );
  },

  getProblem(questionId: number) {
    return getCodingQuestion(questionId);
  },

  getSubmissions(questionId: number) {
    return getQuestionSubmissions(questionId);
  },

  getSolvedIds() {
    return getUserSolvedQuestionIds();
  },

  run(questionId: number, code: string): Promise<PracticeRunResult> {
    return runCode(questionId, code);
  },

  submit(questionId: number, code: string): Promise<PracticeRunResult> {
    return submitCode(questionId, code);
  },
};

/*
 * Solve-progress persistence (per user, per problem, localStorage).
 * The stages before "code" are working notes — they belong on the
 * client, not the database.
 */

const PROGRESS_KEY = "practice.solve-progress";

export function loadSolveProgress(
  questionId: number,
): SolveProgress | null {
  try {
    const raw = localStorage.getItem(
      `${PROGRESS_KEY}.${questionId}`,
    );

    return raw ? (JSON.parse(raw) as SolveProgress) : null;
  } catch {
    return null;
  }
}

export function saveSolveProgress(
  questionId: number,
  progress: SolveProgress,
): void {
  try {
    localStorage.setItem(
      `${PROGRESS_KEY}.${questionId}`,
      JSON.stringify(progress),
    );
  } catch {
    // Storage may be unavailable (private mode) — non-fatal.
  }
}

export function clearSolveProgress(questionId: number): void {
  try {
    localStorage.removeItem(`${PROGRESS_KEY}.${questionId}`);
  } catch {
    // Non-fatal.
  }
}
