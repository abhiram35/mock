import { useEffect, useState } from "react";
import Editor, { type OnMount, type Monaco } from "@monaco-editor/react";
import { ArrowLeft, Loader2, Play, Send } from "lucide-react";

import { Button, Card, Kbd } from "../../../components/primitives";
import type { CodeStageProps } from "./stageProps";

/* =========================================================
   Custom Monaco themes matching the paper/ink system
   ========================================================= */

function defineThemes(monaco: Monaco) {
  monaco.editor.defineTheme("paper-light", {
    base: "vs",
    inherit: true,
    rules: [
      { token: "keyword", foreground: "2F4FE0", fontStyle: "none" },
      { token: "string", foreground: "1A7F4F" },
      { token: "comment", foreground: "8A8378", fontStyle: "italic" },
      { token: "number", foreground: "9A6700" },
      { token: "type", foreground: "0F6D8C" },
    ],
    colors: {
      "editor.background": "#FFFFFF",
      "editorLineNumber.foreground": "#C9C2B6",
      "editorLineNumber.activeForeground": "#57524A",
      "editor.selectionBackground": "#2F4FE020",
      "editor.lineHighlightBackground": "#F1EDE580",
      "editorCursor.foreground": "#2F4FE0",
      "editorIndentGuide.background1": "#EDE9E1",
    },
  });

  monaco.editor.defineTheme("paper-dark", {
    base: "vs-dark",
    inherit: true,
    rules: [
      { token: "keyword", foreground: "7D95FF", fontStyle: "none" },
      { token: "string", foreground: "4CC38A" },
      { token: "comment", foreground: "756D61", fontStyle: "italic" },
      { token: "number", foreground: "D9A53F" },
      { token: "type", foreground: "53B1CF" },
    ],
    colors: {
      "editor.background": "#1C1915",
      "editorLineNumber.foreground": "#4A453C",
      "editorLineNumber.activeForeground": "#A89F92",
      "editor.selectionBackground": "#7D95FF30",
      "editor.lineHighlightBackground": "#26221C80",
      "editorCursor.foreground": "#7D95FF",
      "editorIndentGuide.background1": "#2C2822",
    },
  });
}

const NARRATION_STEPS = [
  "Sending to the sandbox…",
  "Setting up Python 3.12…",
  "Running your code…",
  "Comparing outputs…",
];

/**
 * CODE — the editor workspace. Run narrates real phases; rate
 * limits, timeouts, and sandbox-outage errors are shown as specific,
 * recoverable messages.
 */
export default function CodeStage({
  code,
  onCodeChange,
  onRun,
  onSubmit,
  narration,
  isRunning,
  runError,
  onBack,
  onProceedToVerify,
}: CodeStageProps & { onBack: () => void }) {
  const [theme, setTheme] = useState<"light" | "dark">(() =>
    document.documentElement.getAttribute("data-theme") === "dark"
      ? "dark"
      : "light",
  );

  useEffect(() => {
    const observer = new MutationObserver(() => {
      setTheme(
        document.documentElement.getAttribute("data-theme") === "dark"
          ? "dark"
          : "light",
      );
    });

    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["data-theme"],
    });

    return () => observer.disconnect();
  }, []);

  const onMount: OnMount = (editor, monaco) => {
    defineThemes(monaco);

    monaco.editor.setTheme(
      theme === "dark" ? "paper-dark" : "paper-light",
    );

    // Ctrl/Cmd+Enter runs; Ctrl/Cmd+Shift+Enter submits.
    editor.addCommand(
      monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter,
      () => onRun(),
    );

    editor.addCommand(
      monaco.KeyMod.CtrlCmd |
        monaco.KeyMod.Shift |
        monaco.KeyCode.Enter,
      () => onSubmit(),
    );
  };

  const phaseToIndex: Record<string, number> = {
    submitting: 0,
    compiling: 1,
    running: 2,
    comparing: 3,
    done: 3,
  };

  const narrationIndex = narration
    ? (phaseToIndex[narration.phase] ?? 0)
    : 0;

  return (
    <div className="flex flex-col gap-4">
      <Card padding="none" elevation="xs" className="overflow-hidden">
        <div className="flex items-center justify-between border-b border-line px-4 py-2.5">
          <div className="flex items-center gap-2">
            <span className="mono text-[11px] uppercase tracking-[0.12em] text-ink-3">
              Python 3.12 · main.py
            </span>
          </div>

          <div className="flex items-center gap-2">
            <Button
              size="sm"
              variant="secondary"
              onClick={onRun}
              isLoading={isRunning}
              icon={<Play size={13} />}
            >
              Run
            </Button>

            <Button
              size="sm"
              onClick={onSubmit}
              isLoading={isRunning}
              icon={<Send size={13} />}
            >
              Submit
            </Button>
          </div>
        </div>

        {/* Narrated run state */}
        {isRunning && (
          <div
            role="status"
            aria-live="polite"
            className="flex items-center gap-3 border-b border-line bg-accent-soft px-4 py-2.5"
          >
            <Loader2 size={14} className="animate-spin text-accent" />

            <span className="text-[13px] text-accent">
              {narration?.message ?? NARRATION_STEPS[narrationIndex]}
            </span>

            <span className="ml-auto hidden items-center gap-1 sm:flex">
              <Kbd>Ctrl</Kbd>
              <Kbd>↵</Kbd>
              <span className="text-ink-3">run</span>

              <Kbd>Ctrl</Kbd>
              <Kbd>⇧</Kbd>
              <Kbd>↵</Kbd>
              <span className="text-ink-3">submit</span>
            </span>
          </div>
        )}

        {/* Errors: specific + recoverable */}
        {runError && (
          <div
            role="alert"
            className="border-b border-line bg-[color:var(--bad-soft)] px-4 py-3"
          >
            <p className="text-[13px] font-medium text-[color:var(--bad)]">
              {runError}
            </p>

            <p className="mt-0.5 text-xs text-ink-2">
              Nothing was saved as a submission — fix and run again.
            </p>
          </div>
        )}

        <div className="h-[420px]">
          <Editor
            language="python"
            theme={theme === "dark" ? "paper-dark" : "paper-light"}
            value={code}
            onChange={(value) => onCodeChange(value ?? "")}
            onMount={onMount}
            loading={
              <div className="flex h-full items-center justify-center gap-2 text-sm text-ink-3">
                <Loader2 className="animate-spin" size={15} />
                Warming up the editor…
              </div>
            }
            options={{
              fontFamily: "'IBM Plex Mono', 'JetBrains Mono', monospace",
              fontSize: 13.5,
              lineHeight: 22,
              minimap: { enabled: false },
              scrollBeyondLastLine: false,
              padding: { top: 14, bottom: 14 },
              renderLineHighlight: "all",
              smoothScrolling: true,
              cursorBlinking: "smooth",
              tabSize: 4,
              automaticLayout: true,
            }}
          />
        </div>
      </Card>

      <div className="flex items-center justify-between">
        <Button variant="ghost" size="sm" icon={<ArrowLeft size={15} />} onClick={onBack}>
          Back to plan
        </Button>

        <Button
          variant="secondary"
          size="sm"
          onClick={onProceedToVerify}
          disabled={isRunning}
        >
          Review results
        </Button>
      </div>
    </div>
  );
}
