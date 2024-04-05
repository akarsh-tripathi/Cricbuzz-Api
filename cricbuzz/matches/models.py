import uuid
from django.db import models


class MatchTable(models.Model):
    match_id = models.AutoField(primary_key=True, unique=True)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    match_date = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    
class PlayersSquadTable(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    team_name = models.CharField(max_length=100)
    player_name = models.CharField(max_length=100)
    player_role = models.CharField(max_length=100)
    