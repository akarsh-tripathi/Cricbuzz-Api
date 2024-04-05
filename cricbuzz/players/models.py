import uuid
from django.db import models

# Create your models here.
class PlayersModel(models.Model):
    player_id = models.UUIDField(primary_key=True,default = uuid.uuid4, editable = False, unique= True)
    name = models.CharField(max_length=100)
    matches_played = models.IntegerField()
    player_role = models.CharField(default='batsman',max_length=100)
    average = models.FloatField()
    strike_rate = models.FloatField()
    
    def __str__(self):
        return self.name