interface ProfileInfoCardProps {
  label: string;
  value: string;
  valueClassName?: string;
}

export default function ProfileInfoCard({
  label,
  value,
  valueClassName = "text-sm font-medium text-slate-200",
}: ProfileInfoCardProps) {
  return (
    <div className="rounded-2xl border border-white/[0.06] bg-white/[0.02] p-6">
      <div className="font-mono text-[9px] uppercase tracking-[0.14em] text-slate-600">
        {label}
      </div>
      <div className={`mt-3 ${valueClassName}`}>
        {value}
      </div>
    </div>
  );
}
