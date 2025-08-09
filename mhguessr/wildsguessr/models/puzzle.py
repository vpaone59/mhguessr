from datetime import date

from django.db import models

from .monster import Monster


class Puzzle(models.Model):
    """
    Represents a daily game challenge with the target monster info
    """

    date = models.DateField(unique=True, default=date.today)
    monster = models.ForeignKey(
        Monster, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        """
        Meta options for Puzzle model

        """

        ordering = ["-date"]

    def __str__(self):
        return f"Puzzle for {self.date}: {self.monster.name}"
