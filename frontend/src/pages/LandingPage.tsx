import LandingFinalCta from "./landing/LandingFinalCta";
import LandingFeatures from "./landing/LandingFeatures";
import LandingFooter from "./landing/LandingFooter";
import LandingHero from "./landing/LandingHero";
import LandingHowItWorks from "./landing/LandingHowItWorks";
import LandingNavbar from "./landing/LandingNavbar";
import LandingStatsStrip from "./landing/LandingStatsStrip";

/**
 * Marketing landing page — a pure composition of the sections in
 * `src/pages/landing/`. Structure-only refactor of the original
 * monolithic page; visual output is unchanged.
 */
function LandingPage() {
  return (
    <div className="landing-page min-h-screen overflow-hidden text-white">
      {/* =====================================================
          AMBIENT BACKGROUND
      ====================================================== */}

      <div className="pointer-events-none fixed inset-0 overflow-hidden">
        <div className="landing-hero-glow absolute left-1/2 top-[-18rem] h-[52rem] w-[52rem] -translate-x-1/2 rounded-full" />
      </div>

      <LandingNavbar />

      <main className="relative z-10">
        <LandingHero />

        <LandingStatsStrip />

        <LandingFeatures />

        <LandingHowItWorks />

        <LandingFinalCta />
      </main>

      <LandingFooter />
    </div>
  );
}

export default LandingPage;
