from django.contrib.auth.models import User
from django.db import models

from wildsguessr.models.puzzle import Puzzle
from wildsguessr.models.user_game_session import UserGameSession


class UserGuess(models.Model):
    """
    Represents a user's guess for a puzzle
    """

    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session = models.ForeignKey(UserGameSession, on_delete=models.CASCADE)
    guess = models.CharField(max_length=255)
    guess_number = models.IntegerField()
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta options for UserGuess model
        """

        ordering = ["guess_number"]
        unique_together = ["session", "guess_number"]

    def __str__(self):
        return f"Guess {self.guess_number}: {self.guess}"
