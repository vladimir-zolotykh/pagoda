from django.urls import path
from . import views

urlpatterns = [
    path("", views.hanoi_game, name="hanoi"),
    path("reset/", views.reset_game, name="reset"),
]
