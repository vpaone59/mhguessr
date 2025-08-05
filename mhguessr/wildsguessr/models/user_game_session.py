from django.contrib.auth.models import User
from django.db import models

from .puzzle import Puzzle


class UserGameSession(models.Model):
    """
    Tracks a user's session for a daily game
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(
        max_length=40, null=True, blank=True
    )  # For anonymous users
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    is_won = models.BooleanField(default=False)
    guesses_count = models.IntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [["user", "puzzle"], ["session_key", "puzzle"]]

    def __str__(self):
        identifier = (
            self.user.username if self.user else f"Anonymous({self.session_key[:8]})"
        )
        return f"{identifier} - {self.puzzle.date}"
