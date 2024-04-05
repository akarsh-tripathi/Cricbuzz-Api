from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from matches.models import MatchTable, PlayersSquadTable
from matches.serializer import MatchSerializer, PlayersSquadSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['POST','GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def getOrCreateMatches(request):
    if request.method == 'GET':
        matches = MatchTable.objects.all()
        matchesSerializer = MatchSerializer(matches, many = True)
        return Response({'matches':matchesSerializer.data}, status = 200)
    
    elif request.method == 'POST':
        matchSerializer = MatchSerializer(data = request.data)
        if matchSerializer.is_valid():
            matchSerializer.save()
            return Response({'message':'Match added successfully', 'match_id':matchSerializer.data['match_id']}, status = 200)
        else:
            return Response({'message':'Match not added','errors':MatchSerializer.errors}, status = 405)
    else:
        return Response({'message':'Method not allowed'}, status = 405)
        


# @api_view(['POST', 'GET'])
# def getOrCreateMatches(request):
#     authentication_classes_set = []
#     permission_classes_set = []
    
#     if request.method == 'POST':
#         authentication_classes_set = [SessionAuthentication, TokenAuthentication]
#         permission_classes_set = [IsAuthenticated]
    
#     @authentication_classes(authentication_classes_set)
#     @permission_classes(permission_classes_set)
#     def inner_view(request):
#         if request.method == 'GET':
#             matches = MatchTable.objects.all()
#             matchesSerializer = MatchSerializer(matches, many=True)
#             return Response({'matches': matchesSerializer.data}, status=200)
        
#         elif request.method == 'POST':
#             matchSerializer = MatchSerializer(data=request.data)
#             if matchSerializer.is_valid():
#                 matchSerializer.save()
#                 return Response({'message': 'Match added successfully', 'match_id': matchSerializer.data['match_id']}, status=200)
#             else:
#                 return Response({'message': 'Match not added', 'errors': matchSerializer.errors}, status=405)
#         else:
#             return Response({'message': 'Method not allowed'}, status=405)
    
#     return inner_view(request)


@api_view(['GET'])
def getMatchById(request, id):
    try:
        match = MatchTable.objects.get(match_id = id)
        matchSerializer = MatchSerializer(match)

        players_of_team1 = PlayersSquadTable.objects.filter(team_name =matchSerializer.data['team1'])
        players_of_team2 = PlayersSquadTable.objects.filter(team_name =matchSerializer.data['team2'])
        return Response({'match':matchSerializer.data, 'squads':{'team1':players_of_team1,'team2':players_of_team2}}, status = 200)
    except:
        return Response({'message':'Match not found'}, status = 404)
    
@api_view(['POST'])
def addPlayersToSquad(request, id):
    serializer = PlayersSquadSerializer(data=request.data)
    
    if serializer.is_valid():
        
        serializer.save()
        serializer.data['team_name'] = id
        return Response({'message':'Player added to squad successfully'}, status = 200)
    return Response({'message':'There is some problem','error':serializer.errors}, status = 404)
    