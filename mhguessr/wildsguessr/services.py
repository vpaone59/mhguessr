import random
from typing import List

import requests
from django.conf import settings

from .models.monster import Monster


class MHWildsAPIService:
    """
    Service to interact with MH Wilds API
    """

    def __init__(self):
        self.base_url = settings.MHWILDS_API_BASE_URL

    def get_monsters(self) -> List[dict]:
        """
        Get all monsters from the API
        """
        url = f"{self.base_url}monsters"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        monsters = response.json()
        return monsters if isinstance(monsters, list) else []

    def get_random_monster(self) -> dict:
        """
        Get a random monster from the API for the daily game
        """

        monsters = self.get_monsters()
        if monsters:
            return random.choice(monsters)
        return {}
