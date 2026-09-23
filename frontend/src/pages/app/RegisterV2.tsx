import { useState, type FormEvent } from "react";
import { Link, useNavigate } from "react-router-dom";
import { ArrowLeft } from "lucide-react";

import { register } from "../../api/auth";
import { Button, Card, Input } from "../../components/primitives";

export default function RegisterV2() {
  const navigate = useNavigate();

  const [fullName, setFullName] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [error, setError] = useState("");

  const [loading, setLoading] = useState(false);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();

    setError("");

    setLoading(true);

    try {
      await register({
        full_name: fullName,
        email,
        password,
      });

      navigate("/login", { replace: true });
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Couldn't create the account. Try again?",
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
          Start practicing<span className="text-accent">.</span>
        </h1>

        <p className="mt-2 text-[15px] text-ink-2">
          One account, both modes: AI interviews and the coding gym.
        </p>

        <Card elevation="sm" padding="lg" className="mt-8">
          <form onSubmit={handleSubmit} className="flex flex-col gap-4">
            <Input
              label="Full name"
              value={fullName}
              onChange={(event) => setFullName(event.target.value)}
              placeholder="Ada Lovelace"
              autoComplete="name"
              required
            />

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
              placeholder="At least 8 characters"
              autoComplete="new-password"
              minLength={8}
              required
              hint="Use something you don't reuse elsewhere."
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
              {loading ? "Creating…" : "Create account"}
            </Button>
          </form>
        </Card>

        <p className="mt-6 text-center text-[13px] text-ink-2">
          Already practicing?{" "}
          <Link to="/login" className="font-medium text-accent hover:underline">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
}
