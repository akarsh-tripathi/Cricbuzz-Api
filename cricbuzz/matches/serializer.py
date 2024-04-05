from rest_framework import serializers
from matches.models import MatchTable, PlayersSquadTable


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchTable
        fields = '__all__'

class PlayersSquadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersSquadTable
        fields = '__all__'
