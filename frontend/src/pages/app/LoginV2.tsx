import { useState, type FormEvent } from "react";
import { Link, useNavigate } from "react-router-dom";
import { ArrowLeft } from "lucide-react";

import { login } from "../../api/auth";
import { Button, Card, Input } from "../../components/primitives";

export default function LoginV2() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [error, setError] = useState("");

  const [loading, setLoading] = useState(false);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();

    setError("");

    setLoading(true);

    try {
      const token = await login({ email, password });

      localStorage.setItem("access_token", token.access_token);

      const meResponse = await fetch(
        `${import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000"}/auth/me`,
        {
          headers: { Authorization: `Bearer ${token.access_token}` },
        },
      );

      if (!meResponse.ok) {
        throw new Error("Signed in, but couldn't load your profile.");
      }

      const me = await meResponse.json();

      localStorage.setItem("user", JSON.stringify(me));

      if (me.role === "admin") {
        navigate("/admin/dashboard", { replace: true });
      } else {
        navigate("/app/dashboard", { replace: true });
      }
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "That email and password didn't match. Try again?",
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app-root flex min-h-screen flex-col">
      <div className="mx-auto w-full max-w-md px-5 pt-20">
        <Link
          to="/"
          className="inline-flex items-center gap-1.5 text-[13px] text-ink-3 transition-colors hover:text-ink"
        >
          <ArrowLeft size={14} /> Back home
        </Link>

        <h1 className="display mt-8 text-3xl text-ink">
          Welcome back<span className="text-accent">.</span>
        </h1>

        <p className="mt-2 text-[15px] text-ink-2">
          Your streak is waiting exactly where you left it.
        </p>

        <Card elevation="sm" padding="lg" className="mt-8">
          <form onSubmit={handleSubmit} className="flex flex-col gap-4">
            <Input
              label="Email"
              type="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              placeholder="you@example.com"
              autoComplete="email"
              required
            />

            <Input
              label="Password"
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              placeholder="••••••••"
              autoComplete="current-password"
              required
            />

            {error && (
              <p role="alert" className="text-[13px] text-[color:var(--bad)]">
                {error}
              </p>
            )}

            <Button
              type="submit"
              size="lg"
              fullWidth
              isLoading={loading}
              className="mt-1"
            >
              {loading ? "Checking…" : "Sign in"}
            </Button>
          </form>
        </Card>

        <p className="mt-6 text-center text-[13px] text-ink-2">
          New here?{" "}
          <Link to="/register" className="font-medium text-accent hover:underline">
            Create an account
          </Link>
        </p>
      </div>
    </div>
  );
}
