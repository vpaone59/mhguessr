from rest_framework import serializers
from wildsguessr.models import Monster, Puzzle, UserGameSession, UserGuess


class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = "__all__"


class PuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puzzle
        fields = "__all__"


class UserGameSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGameSession
        fields = "__all__"


class UserGuessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGuess
        fields = "__all__"
