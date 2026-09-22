from app.enums.question_difficulty import QuestionDifficulty
from app.services.adaptive_service import (
	AdaptiveDifficultyService,
)


def test_three_poor_scores_decrease_difficulty_and_reset_streaks():
	service = AdaptiveDifficultyService()
	difficulty = QuestionDifficulty.HARD
	poor_streak = 0
	strong_streak = 0

	for score in (59, 40, 20):
		(
			difficulty,
			poor_streak,
			strong_streak,
		) = service.update_performance(
			difficulty,
			poor_streak,
			strong_streak,
			score,
		)

	assert difficulty == QuestionDifficulty.MEDIUM
	assert poor_streak == 0
	assert strong_streak == 0


def test_three_strong_scores_increase_difficulty_and_reset_streaks():
	service = AdaptiveDifficultyService()
	difficulty = QuestionDifficulty.EASY
	poor_streak = 0
	strong_streak = 0

	for score in (80, 90, 100):
		(
			difficulty,
			poor_streak,
			strong_streak,
		) = service.update_performance(
			difficulty,
			poor_streak,
			strong_streak,
			score,
		)

	assert difficulty == QuestionDifficulty.MEDIUM
	assert poor_streak == 0
	assert strong_streak == 0


def test_acceptable_score_resets_streaks_without_changing_difficulty():
	service = AdaptiveDifficultyService()

	result = service.update_performance(
		QuestionDifficulty.MEDIUM,
		poor_streak=2,
		strong_streak=1,
		score=79,
	)

	assert result == (
		QuestionDifficulty.MEDIUM,
		0,
		0,
	)


def test_easy_difficulty_cannot_decrease_further():
	service = AdaptiveDifficultyService()

	result = service.update_performance(
		QuestionDifficulty.EASY,
		poor_streak=2,
		strong_streak=0,
		score=10,
	)

	assert result == (
		QuestionDifficulty.EASY,
		0,
		0,
	)


def test_hard_difficulty_cannot_increase_further():
	service = AdaptiveDifficultyService()

	result = service.update_performance(
		QuestionDifficulty.HARD,
		poor_streak=0,
		strong_streak=2,
		score=100,
	)

	assert result == (
		QuestionDifficulty.HARD,
		0,
		0,
	)
