from datetime import date

from django.shortcuts import render

from wildsguessr.models.monster import Monster
from wildsguessr.models.puzzle import Puzzle


def index(request):
    """
    Main game page
    """
    # Get or create today's game
    puzzle = get_or_create_daily_puzzle()

    context = {
        "puzzle": puzzle,
    }

    return render(request, "wildsguessr/index.html", context)


def get_or_create_daily_puzzle() -> Puzzle:
    """
    Get or create today's puzzle
    """
    today = date.today()
    puzzle, created = Puzzle.objects.get_or_create(date=today)

    if created:
        random_monster = Monster.objects.order_by("?").first()
        puzzle.monster = random_monster
        puzzle.save()

    # Check if the puzzle solution is set
    # If not, assign a default monster
    if puzzle.monster == None:
        print("No monster assigned for today's puzzle, using default.")
        puzzle.monster = Monster.objects.first()
        puzzle.save()

    print("Today's puzzle:", puzzle)
    return puzzle
