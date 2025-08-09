"""
URL configuration for wildsguessr application.


"""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from wildsguessr.views_drf import drf_views

from .views import views

urlpatterns = [
    path("", views.index, name="index"),
    # DRF URLs
    path("drf/puzzle", drf_views.DailyPuzzle.as_view()),
    path("drf/monster/<int:pk>/", drf_views.MonsterView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
