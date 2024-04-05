from players.models import PlayersModel
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersModel
        fields = '__all__'
        