# Django REST Framework viewsets and API root
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer
from rest_framework.reverse import reverse
import os

def get_base_url(request):
	codespace_name = os.environ.get('CODESPACE_NAME')
	if codespace_name:
		return f"https://{codespace_name}-8000.app.github.dev"
	return request.build_absolute_uri('/')[:-1]

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
	queryset = Leaderboard.objects.all()
	serializer_class = LeaderboardSerializer

@api_view(['GET'])
def api_root(request, format=None):
	base_url = get_base_url(request)
	return Response({
		'users': f'{base_url}/api/users/',
		'teams': f'{base_url}/api/teams/',
		'activities': f'{base_url}/api/activities/',
		'workouts': f'{base_url}/api/workouts/',
		'leaderboard': f'{base_url}/api/leaderboard/',
	})
