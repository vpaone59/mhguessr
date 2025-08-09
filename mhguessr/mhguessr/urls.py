"""
URL configuration for mhguessr project.

Includes URL setup for django-ninja API implementation of the wildsguessr application.
"""

from django.contrib import admin
from django.urls import include, path
from wildsguessr.views.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("wildsguessr.urls")),
    # django-ninja URLs
    path("api/puzzle/", api.urls),
]
