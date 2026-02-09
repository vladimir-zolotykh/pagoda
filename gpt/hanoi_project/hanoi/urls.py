from django.urls import path
from . import views

urlpatterns = [
    path("", views.start, name="start"),
    path("game/", views.game, name="game"),
    path("step/", views.step_game, name="step_game"),
    path("reset/", views.reset_game, name="reset"),
]
