from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from matches.models import MatchTable, PlayersSquadTable
from matches.serializer import MatchSerializer, PlayersSquadSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# @api_view(['POST','GET'])

class getOrCreateMatches(APIView):
    def get(self, request):
        matches = MatchTable.objects.all()
        matchesSerializer = MatchSerializer(matches, many = True)
        return Response({'matches':matchesSerializer.data}, status = 200)
    
    @authentication_classes([SessionAuthentication, TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def post(self, request):
        # data = JSONParser().parse(request)
        addmatchSerializer = MatchSerializer(data = request.data)
        if addmatchSerializer.is_valid():
            addmatchSerializer.save()
            return Response({'message':'Match added successfully', 'match_id':addmatchSerializer.data['match_id']}, status = 200)
        else:
            return Response({'message':'Match not added','errors':MatchSerializer.errors}, status = 405)


@api_view(['GET'])
def getMatchById(request, id):
    try:
        match = MatchTable.objects.get(match_id = id)
        matchSerializer = MatchSerializer(match)
        # playerteam1 = PlayersSquadTable.objects.filter(team_name = matchSerializer.data['team1'])
        # print(matchSerializer.data['team1'])
        # print(matchSerializer.data['team2'])
        # print(playerteam1.values())        
        
        # return Response({'match':matchSerializer.data}, status = 200)
        players_of_team1 = PlayersSquadTable.objects.filter(team_name =matchSerializer.data['team1'])
        players_of_team2 = PlayersSquadTable.objects.filter(team_name =matchSerializer.data['team2'])
        return Response({'match':matchSerializer.data, 'squads':{'team1':players_of_team1.values(),'team2':players_of_team2.values()}}, status = 200)
    except:
        return Response({'message':'Match not found'}, status = 404)
    
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def addPlayersToSquad(request, id):
    serializer = PlayersSquadSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        serializer.data['team_name'] = id
        return Response({'message':'Player added to squad successfully'}, status = 200)
    return Response({'message':'There is some problem','error':serializer.errors}, status = 404)
    