from django.urls import path

from . import views

urlpatterns = [
    path("", views.game, name="game"),
    path("buildings", views.buildings, name="buildings"),
    path("fleets", views.fleets, name="fleets"),
]