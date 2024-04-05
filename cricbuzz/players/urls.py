
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('players/<uuid:id>/stats', views.statsById),
    path('players/addplayer', views.AddPlayer),
]
