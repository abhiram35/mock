/**
 * Landing footer.
 */
export default function LandingFooter() {
  return (
    <footer className="border-t border-white/[0.06]">
      <div className="mx-auto flex max-w-7xl flex-col gap-4 px-6 py-8 sm:flex-row sm:items-center sm:justify-between lg:px-8">
        <div>
          <div className="text-sm font-semibold">AI Mock Interview</div>

          <div className="mt-1 text-xs text-slate-600">
            Practice. Improve. Succeed.
          </div>
        </div>

        <div className="text-xs text-slate-600">
          © {new Date().getFullYear()} AI Mock Interview
        </div>
      </div>
    </footer>
  );
}
