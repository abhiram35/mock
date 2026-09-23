import { Navigate, Route, Routes } from "react-router-dom";

import ProtectedRoute from "./components/ProtectedRoute";
import AnimatedOutlet from "./components/motion/AnimatedOutlet";

import LandingPage from "./pages/LandingPage";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";

import Dashboard from "./pages/Dashboard";
import InterviewResult from "./pages/InterviewResult";
import Profile from "./pages/Profile";

import InterviewSetup from "./pages/InterviewSetup";
import InterviewRoom from "./pages/InterviewRoom";

import CodingInterviewSetup from "./pages/CodingInterviewSetup";
import CodingInterviewRoom from "./pages/CodingInterviewRoom";

import PracticeProblems from "./pages/PracticeProblems";
import PracticeProblemDetail from "./pages/PracticeProblemDetail";

import AdminDashboard from "./pages/admin/AdminDashboard";

function App() {
  return (
    <Routes>
      {/* =====================================================
          PUBLIC ROUTES
      ====================================================== */}

      <Route path="/" element={<LandingPage />} />

      <Route path="/login" element={<Login />} />

      <Route path="/register" element={<Register />} />

      {/* =====================================================
          USER PROTECTED ROUTES
      ====================================================== */}

      <Route element={<ProtectedRoute requiredRole="user" />}>
        {/* HOME */}

        <Route path="/home" element={<Home />} />

        {/* DASHBOARD + INTERVIEW + PRACTICE ROUTES — animated transitions */}

        <Route element={<AnimatedOutlet />}>
          <Route path="/dashboard" element={<Dashboard />} />

          <Route path="/profile" element={<Profile />} />

          {/* NORMAL INTERVIEW SETUP */}

          <Route path="/interviews/new" element={<InterviewSetup />} />

          {/* NORMAL INTERVIEW RESULT */}

          <Route
            path="/interviews/:sessionId/result"
            element={<InterviewResult />}
          />

          {/* CODING INTERVIEW SETUP */}

          <Route
            path="/coding-interview/new"
            element={<CodingInterviewSetup />}
          />

          {/* PRACTICE FLOW */}

          <Route path="/practice" element={<PracticeProblems />} />

          <Route
            path="/practice/:questionId"
            element={<PracticeProblemDetail />}
          />
        </Route>

        {/* FULL-SCREEN FLOWS — no transitions (security + focus) */}

        <Route path="/interviews/:sessionId" element={<InterviewRoom />} />

        <Route path="/coding-interview" element={<CodingInterviewRoom />} />
      </Route>

      {/* =====================================================
          ADMIN PROTECTED ROUTES
      ====================================================== */}

      <Route element={<ProtectedRoute requiredRole="admin" />}>
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
      </Route>

      {/* =====================================================
          FALLBACK
      ====================================================== */}

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}

export default App;
