import type { Difficulty, Interview } from "../../lib/api";

/**
 * Pure formatting/display helpers for the dashboard.
 * No React, no fetching — safe to unit test in isolation.
 */

export function formatDate(dateString: string): string {
  return new Date(dateString).toLocaleDateString(undefined, {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}

export function formatDateTime(dateString: string): string {
  return new Date(dateString).toLocaleString(undefined, {
    day: "numeric",
    month: "short",
    year: "numeric",
    hour: "numeric",
    minute: "2-digit",
  });
}

export function capitalize(value: string): string {
  return value.charAt(0).toUpperCase() + value.slice(1);
}

export function getDifficultyLabel(difficulty: Difficulty): string {
  return capitalize(difficulty);
}

export function getStatusLabel(status: Interview["status"]): string {
  if (status === "in_progress") {
    return "In Progress";
  }

  if (status === "completed") {
    return "Completed";
  }

  return "Abandoned";
}

export function getStatusClass(status: Interview["status"]): string {
  if (status === "completed") {
    return "dashboard-status dashboard-status-success";
  }

  if (status === "in_progress") {
    return "dashboard-status dashboard-status-warning";
  }

  return "dashboard-status dashboard-status-danger";
}

export function getScoreClass(score: number | null): string {
  if (score === null) {
    return "dashboard-score dashboard-score-muted";
  }

  if (score >= 80) {
    return "dashboard-score dashboard-score-good";
  }

  if (score >= 60) {
    return "dashboard-score dashboard-score-average";
  }

  return "dashboard-score dashboard-score-low";
}

export function getScoreTone(
  score: number | null,
): "success" | "warning" | "error" | "neutral" {
  if (score === null) {
    return "neutral";
  }

  if (score >= 80) {
    return "success";
  }

  if (score >= 60) {
    return "warning";
  }

  return "error";
}

export function getStatusTone(
  status: Interview["status"],
): "success" | "warning" | "error" {
  if (status === "completed") {
    return "success";
  }

  if (status === "in_progress") {
    return "warning";
  }

  return "error";
}
