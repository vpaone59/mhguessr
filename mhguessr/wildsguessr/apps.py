import os

from django.apps import AppConfig
from django.core.management import call_command


class WildsguesserConfig(AppConfig):
    """
    Configuration for the WildsGuessr app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "wildsguessr"

    def ready(self):
        if os.environ.get("POPULATE_MONSTERS_ON_STARTUP") == "true":
            try:
                call_command("populate_monsters")
            except Exception as e:
                print(f"Failed to populate monsters: {e}")
