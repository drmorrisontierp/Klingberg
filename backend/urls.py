from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dice", views.dice, name="dice"),
    path("luffer", views.luffer, name="luffer"),
    path("klingberg", views.klingberg, name="klingberg"),
]