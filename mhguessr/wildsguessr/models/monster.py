from django.db import models


class Monster(models.Model):
    """
    Represents a Monster from the MH Wilds API with all detailed information
    """

    MONSTER_KINDS = (
        ("small", "Small Monster"),
        ("large", "Large Monster"),
    )

    MONSTER_SPECIES = (
        ("flying-wyvern", "Flying Wyvern"),
        ("fish", "Fish"),
        ("herbivore", "Herbivore"),
        ("lynian", "Lynian"),
        ("neopteron", "Neopteron"),
        ("carapaceon", "Carapaceon"),
        ("fanged-beast", "Fanged Beast"),
        ("bird-wyvern", "Bird Wyvern"),
        ("piscine-wyvern", "Piscine Wyvern"),
        ("leviathan", "Leviathan"),
        ("brute-wyvern", "Brute Wyvern"),
        ("fanged-wyvern", "Fanged Wyvern"),
        ("amphibian", "Amphibian"),
        ("temnoceran", "Temnoceran"),
        ("snake-wyvern", "Snake Wyvern"),
        ("elder-dragon", "Elder Dragon"),
        ("cephalopod", "Cephalopod"),
        ("construct", "Construct"),
        ("wingdrake", "Wingdrake"),
        ("demi-elder", "Demi-Elder"),
    )

    game_id = models.CharField(
        max_length=100,
        unique=True,
        help_text="The ID used by the game files to identify the monster",
    )
    kind = models.CharField(
        max_length=20, choices=MONSTER_KINDS, help_text="The monster's category"
    )
    species = models.CharField(
        max_length=50, choices=MONSTER_SPECIES, help_text="The monster's species"
    )
    name = models.CharField(max_length=255, help_text="The monster's name")
    size = models.JSONField(
        default=dict, help_text="The monster's base size and crown size breakpoints"
    )
    description = models.TextField(help_text="The monster's description")
    features = models.TextField(
        blank=True, help_text="The 'features' section from the monster guide"
    )
    tips = models.TextField(
        blank=True, help_text="The 'tips' section from the monster guide"
    )
    base_health = models.IntegerField(
        null=True,
        blank=True,
        help_text="The monster's base health",
    )
    locations = models.JSONField(
        default=list, help_text="The locations in which the monster can be found"
    )
    resistances = models.JSONField(
        default=list, help_text="The monster's elemental and status resistances"
    )
    weaknesses = models.JSONField(
        default=list, help_text="The monster's elemental and status weaknesses"
    )
    rewards = models.JSONField(
        default=list, help_text="Items can be obtained from fighting the monster"
    )
    parts = models.JSONField(
        default=list, help_text="An array of various parts and hitzones on the monster"
    )
    ailments = models.JSONField(
        default=list, help_text="The ailments the monster can inflict"
    )
    elements = models.JSONField(
        default=list, help_text="The elements the monster can use in combat"
    )

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta options for the Monster model
        """

        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.species})"
