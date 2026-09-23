import { useReducedMotion } from "framer-motion";

/**
 * Shared framer-motion variants for the app.
 *
 * Every exported hook respects `prefers-reduced-motion`: when the OS
 * setting is on, motion is reduced to a short opacity fade with no
 * translation, keeping the UI responsive without movement.
 */

const EASE_OUT = [0.16, 1, 0.3, 1] as const;

/** Page-level fade/slide used by the animated route outlet. */
export function usePageTransition() {
  const reduceMotion = useReducedMotion();

  return {
    initial: reduceMotion ? { opacity: 0 } : { opacity: 0, y: 10 },
    animate: reduceMotion ? { opacity: 1 } : { opacity: 1, y: 0 },
    exit: reduceMotion ? { opacity: 0 } : { opacity: 0, y: -8 },
    transition: {
      duration: reduceMotion ? 0.12 : 0.22,
      ease: EASE_OUT,
    },
  };
}

/** Parent container that staggers its children by 60ms. */
export function useStaggerContainer() {
  const reduceMotion = useReducedMotion();

  return {
    hidden: {},
    show: {
      transition: {
        staggerChildren: reduceMotion ? 0 : 0.06,
      },
    },
  };
}

/** Child of a stagger container: fade + slide-up, or fade only. */
export function useStaggerItem() {
  const reduceMotion = useReducedMotion();

  return {
    hidden: reduceMotion
      ? { opacity: 0 }
      : { opacity: 0, y: 12 },
    show: {
      opacity: 1,
      y: 0,
      transition: {
        duration: reduceMotion ? 0.12 : 0.3,
        ease: EASE_OUT,
      },
    },
  };
}

/** Viewport config so stagger groups animate once, on first reveal. */
export const onceInView = { once: true, amount: 0.2 } as const;
