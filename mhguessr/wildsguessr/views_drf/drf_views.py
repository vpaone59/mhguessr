"""
Django REST Framework API for MHGuessr daily game functionality.
"""

from datetime import date

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from wildsguessr.models import Puzzle, Monster
from wildsguessr.views_drf.serializers import PuzzleSerializer, MonsterSerializer


class DailyPuzzle(APIView):
    """
    Get today's puzzle, or create a new puzzle.
    """

    def get(self, request, format=None):
        """
        Get today's puzzle
        """
        today = date.today()
        puzzle = Puzzle.objects.get(date=today)
        serializer = PuzzleSerializer(puzzle)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new puzzle
        """
        serializer = PuzzleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MonsterView(generics.RetrieveUpdateDestroyAPIView):
    """
    Includes methods for GET, PUT and DELETE
    """

    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
