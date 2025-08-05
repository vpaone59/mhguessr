"""
django-ninja API for MHGuessr daily game functionality.
"""

from datetime import date
from typing import List, Optional

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from ninja import NinjaAPI, Schema

from wildsguessr.models.puzzle import Puzzle
from wildsguessr.models.user_game_session import UserGameSession
from wildsguessr.models.user_guess import UserGuess
from wildsguessr.services import MHWildsAPIService
from wildsguessr.views import get_or_create_session

api = NinjaAPI(csrf=True)


class GuessRequest(Schema):
    guess: str


class GuessResponse(Schema):
    guess_number: int
    guess: str
    is_correct: bool
    feedback: str
    game_over: bool
    won: bool
    correct_answer: Optional[str] = None


class GameStatusResponse(Schema):
    puzzle_id: int
    item_: str
    guesses_made: int
    max_guesses: int
    is_completed: bool
    is_won: bool
    guesses: List[dict]


@api.get("/daily-status", response=GameStatusResponse)
def get_puzzle_status(request):
    """
    Get daily puzzle status for the user
    """
    today = date.today()

    # Get today's puzzle
    puzzle = get_object_or_404(Puzzle, date=today)

    # Get or create user session for this puzzle
    session = get_or_create_session(request, puzzle)

    # Get all guesses for this session
    guesses = UserGuess.objects.filter(session=session).order_by("guess_number")

    # Convert guesses to dict format for template
    guess_list = []
    for guess in guesses:
        feedback = (
            "correct" if guess.is_correct else "incorrect"
        )  # You may want to implement closer/further logic
        guess_list.append(
            {
                "guess_number": guess.guess_number,
                "guess": guess.guess,
                "feedback": feedback,
                "is_correct": guess.is_correct,
            }
        )

    return GameStatusResponse(
        puzzle_id=puzzle.id,
        item_=puzzle.monster.name if puzzle.monster else "Unknown Monster",
        guesses_made=session.guesses_count,
        max_guesses=8,  # Based on your template: "Guess the monster in 8 tries or less"
        is_completed=session.is_completed,
        is_won=session.is_won,
        guesses=guess_list,
    )


@api.post("/daily-guess", response=GuessResponse)
def submit_daily_guess(request):
    """
    Make a guess for the daily puzzle
    """
    # guess = request.POST.get("guess", "").strip()
    # if not guess:
    #     return HttpResponse("Invalid guess", status=400)

    # today = date.today()
    # puzzle = get_object_or_404(Puzzle, date=today)
    # session = get_or_create_session(request, puzzle)
    pass
