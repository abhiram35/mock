import Button from "../../components/ui/Button";

export interface DashboardHeaderProps {
  /** Called when the "Start New Interview" CTA is clicked. */
  onStartInterview: () => void;
}

/**
 * Dashboard page header: eyebrow, welcome heading, blurb and the
 * primary call-to-action.
 */
export default function DashboardHeader({
  onStartInterview,
}: DashboardHeaderProps) {
  return (
    <header className="dashboard-header">
      <div>
        <div className="dashboard-eyebrow">PERFORMANCE CENTER</div>

        <h1>Your Interview Performance</h1>

        <p>
          Track your progress, review previous interviews, and understand
          where you can improve.
        </p>
      </div>

      <Button size="lg" className="dashboard-primary-button" onClick={onStartInterview}>
        Start New Interview
        <span>→</span>
      </Button>
    </header>
  );
}
