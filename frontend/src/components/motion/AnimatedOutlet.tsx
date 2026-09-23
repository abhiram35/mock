import { AnimatePresence, motion } from "framer-motion";
import { Outlet, useLocation } from "react-router-dom";

import { usePageTransition } from "./transitions";

/**
 * Route outlet wrapped in `AnimatePresence` so every page change
 * plays a short fade/slide. Mount this instead of a bare `<Outlet />`
 * inside a layout route.
 *
 * `mode="wait"` keeps only one page mounted during the handoff;
 * the exit is deliberately quick (0.22s) to stay out of the way.
 */
export default function AnimatedOutlet() {
  const location = useLocation();

  const page = usePageTransition();

  return (
    <AnimatePresence mode="wait" initial={false}>
      <motion.div
        key={location.pathname}
        initial={page.initial}
        animate={page.animate}
        exit={page.exit}
        transition={page.transition}
      >
        <Outlet />
      </motion.div>
    </AnimatePresence>
  );
}
