import type { ReactNode } from "react";
import { Navigate } from "react-router-dom";

/**
 * Gate for the redesigned /app section. Reads the same localStorage
 * auth state as the existing ProtectedRoute, so both systems stay
 * in sync. Admins are redirected to the existing admin area.
 */
export default function RequireUser({ children }: { children: ReactNode }) {
  const token = localStorage.getItem("access_token");

  const rawUser = localStorage.getItem("user");

  let role: string | null = null;

  try {
    if (rawUser) {
      role = (JSON.parse(rawUser) as { role?: string }).role ?? null;
    }
  } catch {
    role = null;
  }

  if (!token || !rawUser) {
    return <Navigate to="/login" replace />;
  }

  if (role === "admin") {
    return <Navigate to="/admin/dashboard" replace />;
  }

  return <>{children}</>;
}
