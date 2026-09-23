import { useReducedMotion } from "framer-motion";

type AIOrbState = "idle" | "listening" | "thinking" | "speaking";

interface AIOrbProps {
  /**
   * Interview status driving the orb's animation and color:
   * - `idle`: waiting for the candidate — calm, slow breathing.
   * - `listening`: microphone active — cyan ring, gentle continuous
   *   pulse while speech is being captured.
   * - `thinking`: AI evaluating an answer — violet pulse, pinging
   *   outer ring, highest intensity.
   * - `speaking`: AI voice active — mint accent, medium pulse.
   *
   * @default "idle"
   */
  state?: AIOrbState;
}

const stateConfig: Record<
  AIOrbState,
  {
    ring: string;
    coreBg: string;
    glow: string;
    coreDot: string;
    coreDotShadow: string;
    ping: boolean;
    pulse: boolean;
    label: string;
  }
> = {
  idle: {
    ring: "border-violet-400/10",
    coreBg: "bg-slate-900",
    glow: "bg-violet-500/20",
    coreDot: "bg-violet-300",
    coreDotShadow: "shadow-[0_0_20px_rgba(196,181,253,0.8)]",
    ping: false,
    pulse: false,
    label: "AI interviewer",
  },
  listening: {
    ring: "border-cyan-400/30",
    coreBg: "bg-cyan-950/60",
    glow: "bg-cyan-400/15",
    coreDot: "bg-cyan-300",
    coreDotShadow: "shadow-[0_0_22px_rgba(103,232,249,0.8)]",
    ping: false,
    pulse: true,
    label: "AI is listening",
  },
  thinking: {
    ring: "border-violet-400/30",
    coreBg: "bg-slate-900",
    glow: "bg-violet-500/30",
    coreDot: "bg-violet-200",
    coreDotShadow: "shadow-[0_0_26px_rgba(196,181,253,1)]",
    ping: true,
    pulse: true,
    label: "AI is thinking",
  },
  speaking: {
    ring: "border-emerald-400/25",
    coreBg: "bg-slate-900",
    glow: "bg-emerald-400/15",
    coreDot: "bg-emerald-300",
    coreDotShadow: "shadow-[0_0_22px_rgba(110,231,183,0.8)]",
    ping: false,
    pulse: true,
    label: "AI is speaking",
  },
};

export default function AIOrb({ state = "idle" }: AIOrbProps) {
  const reduceMotion = useReducedMotion();

  const config = stateConfig[state];

  const animate =
    reduceMotion || config.pulse === false
      ? ""
      : config.ping
        ? "animate-ping"
        : "animate-pulse";

  const middleAnimate =
    reduceMotion || !config.pulse ? "" : "animate-pulse";

  return (
    <div
      className="
        relative
        flex
        h-40
        w-40
        items-center
        justify-center
      "
      aria-label={config.label}
      role="img"
    >
      {/* Outer ping ring — strongest activity signal */}
      <div
        className={`
          absolute
          inset-0
          rounded-full
          border
          ${config.ring}
          ${animate}
        `}
      />

      {/* Middle ring */}
      <div
        className={`
          absolute
          inset-5
          rounded-full
          border
          border-violet-400/20
          ${middleAnimate}
        `}
      />

      {/* Glow */}
      <div
        className={`
          absolute
          h-24
          w-24
          rounded-full
          blur-2xl
          ${config.glow}
        `}
      />

      {/* Core */}
      <div
        className={`
          relative
          flex
          h-20
          w-20
          items-center
          justify-center
          rounded-full
          border
          border-violet-300/30
          ${config.coreBg}
          ${config.coreDotShadow}
          ${
            reduceMotion
              ? ""
              : state === "speaking"
                ? "animate-pulse"
                : ""
          }
        `}
      >
        <div
          className={`
            h-3
            w-3
            rounded-full
            ${config.coreDot}
            ${config.coreDotShadow}
            ${reduceMotion ? "" : state === "thinking" ? "animate-pulse" : ""}
          `}
        />
      </div>
    </div>
  );
}
