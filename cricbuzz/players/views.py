from django.shortcuts import render
from players.models import PlayersModel
from players.serializer import PlayerSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def AddPlayer(request):
    playerSerializer = PlayerSerializer(data = request.data)
    if playerSerializer.is_valid():
        playerSerializer.save()
        return Response({'message':'Player added successfully', "player-id":playerSerializer.data['player_id']}, status = 200)
    else:
        return Response({'message':'Method not allowed'}, status = 405)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def statsById(request, id):
    player = PlayersModel.objects.get(player_id = id)
    playerSerializer = PlayerSerializer(player)
    return Response(playerSerializer.data, status = 200)