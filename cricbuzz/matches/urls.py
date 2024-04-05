from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('matches', views.getOrCreateMatches.as_view()),
    path('matches/<int:id>', views.getMatchById),
    path('team/<slug:id>/squad', views.addPlayersToSquad),
    
]
