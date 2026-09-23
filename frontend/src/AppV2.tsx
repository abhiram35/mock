import { useEffect, useState } from "react";
import { Navigate, Route, Routes, useNavigate } from "react-router-dom";

import AppShell from "./components/shell/AppShell";
import CommandPalette from "./components/shell/CommandPalette";
import RequireUser from "./components/shell/RequireUser";

import LandingV2 from "./pages/app/LandingV2";
import LoginV2 from "./pages/app/LoginV2";
import RegisterV2 from "./pages/app/RegisterV2";
import DashboardV2 from "./pages/app/DashboardV2";
import PracticeHome from "./pages/app/PracticeHome";
import TrackPage from "./pages/app/TrackPage";
import SolvePage from "./pages/app/SolvePage";
import ProfileV2 from "./pages/app/ProfileV2";

/*
 * Redesigned application. The /app section runs on the new design
 * system; the deep interview flows (/interviews/*, /coding-interview)
 * still resolve to the original pages until they are restaged —
 * logging out of the shell returns to the new landing.
 */
export default function AppV2() {
  const navigate = useNavigate();

  const [paletteOpen, setPaletteOpen] = useState(false);

  /* Global ⌘K / Ctrl+K */
  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        setPaletteOpen((open) => !open);
      }
    };

    document.addEventListener("keydown", onKeyDown);

    return () => document.removeEventListener("keydown", onKeyDown);
  }, []);

  function handleLogout() {
    localStorage.removeItem("access_token");

    localStorage.removeItem("user");

    navigate("/login", { replace: true });
  }

  return (
    <>
      <Routes>
        {/* Public, redesigned */}
        <Route path="/" element={<LandingV2 />} />
        <Route path="/login" element={<LoginV2 />} />
        <Route path="/register" element={<RegisterV2 />} />

        {/* Redesigned app section */}
        <Route
          path="/app"
          element={
            <RequireUser>
              <AppShell
                onLogout={handleLogout}
                onOpenCommandPalette={() => setPaletteOpen(true)}
              >
                <OutletProxy />
              </AppShell>
            </RequireUser>
          }
        >
          <Route index element={<Navigate to="/app/dashboard" replace />} />

          <Route path="dashboard" element={<DashboardV2 />} />

          <Route path="practice" element={<PracticeHome />} />

          <Route path="practice/:trackId" element={<TrackPage />} />

          <Route
            path="practice/:trackId/:questionId"
            element={<SolvePage />}
          />

          <Route path="profile" element={<ProfileV2 />} />
        </Route>

        {/* Deep flows still served by the current pages */}
        <Route path="/interviews/new" element={<LegacyInterviewSetup />} />
        <Route
          path="/interviews/:sessionId/result"
          element={<LegacyInterviewResult />}
        />
        <Route path="/interviews/:sessionId" element={<LegacyInterviewRoom />} />
        <Route
          path="/coding-interview/new"
          element={<LegacyCodingSetup />}
        />
        <Route path="/coding-interview" element={<LegacyCodingRoom />} />

        {/* Legacy pages kept reachable during the migration */}
        <Route path="/dashboard" element={<Navigate to="/app/dashboard" replace />} />
        <Route path="/home" element={<Navigate to="/app/dashboard" replace />} />
        <Route path="/practice" element={<Navigate to="/app/practice" replace />} />
        <Route
          path="/practice/:questionId"
          element={<Navigate to="/app/practice" replace />}
        />
        <Route path="/profile" element={<Navigate to="/app/profile" replace />} />

        <Route path="/admin/*" element={<LegacyAdmin />} />

        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>

      <CommandPalette
        isOpen={paletteOpen}
        onClose={() => setPaletteOpen(false)}
      />
    </>
  );
}

/*
 * Lazy-imported legacy pages keep this file honest about what is
 * migrated and what is not. Static imports are fine at this bundle
 * size; named clearly so the remaining work is greppable.
 */
import LegacyInterviewSetup from "./pages/InterviewSetup";
import LegacyInterviewResult from "./pages/InterviewResult";
import LegacyInterviewRoom from "./pages/InterviewRoom";
import LegacyCodingSetup from "./pages/CodingInterviewSetup";
import LegacyCodingRoom from "./pages/CodingInterviewRoom";
import LegacyAdmin from "./pages/admin/AdminDashboard";

import { Outlet } from "react-router-dom";

function OutletProxy() {
  return <Outlet />;
}
