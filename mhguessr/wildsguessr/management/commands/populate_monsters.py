from django.core.management.base import BaseCommand
from django.db import transaction

from wildsguessr.models.monster import Monster
from wildsguessr.services import MHWildsAPIService


class Command(BaseCommand):
    """
    Command to populate the database with monsters from the MH Wilds API
    """

    help = "Populate the database with monsters from the MH Wilds API"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Force update existing monsters",
        )

    def handle(self, *args, **options):
        self.stdout.write("Starting monster population...")

        try:
            api_service = MHWildsAPIService()
            monsters_data = api_service.get_monsters()
            print("Monsters data:", monsters_data)
            created_count = 0
            updated_count = 0

            with transaction.atomic():
                for monster_data in monsters_data:
                    monster, created = Monster.objects.update_or_create(
                        game_id=monster_data["gameId"],
                        defaults={
                            "kind": monster_data.get("kind", ""),
                            "species": monster_data.get("species", ""),
                            "name": monster_data.get("name", ""),
                            "size": monster_data.get("size", {}),
                            "description": monster_data.get("description", ""),
                            "features": monster_data.get("features", ""),
                            "tips": monster_data.get("tips", ""),
                            "base_health": monster_data.get("baseHealth"),
                            "locations": monster_data.get("locations", []),
                            "resistances": monster_data.get("resistances", []),
                            "weaknesses": monster_data.get("weaknesses", []),
                            "rewards": monster_data.get("rewards", []),
                            "parts": monster_data.get("parts", []),
                        },
                    )

                    if created:
                        created_count += 1
                        self.stdout.write(f"Created: {monster.name}")
                    elif options["force"]:
                        updated_count += 1
                        self.stdout.write(f"Updated: {monster.name}")

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully processed monsters: {created_count} created, {updated_count} updated"
                )
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error populating monsters: {str(e)}"))
            raise
