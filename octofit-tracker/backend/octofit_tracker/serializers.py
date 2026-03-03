# Django REST Framework serializers for all models

from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class ObjectIdField(serializers.Field):
	def to_representation(self, value):
		return str(value) if value else None
	def to_internal_value(self, data):
		return data

class TeamSerializer(serializers.ModelSerializer):
	id = ObjectIdField(read_only=True)
	class Meta:
		model = Team
		fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
	id = ObjectIdField(read_only=True)
	team = ObjectIdField(source='team_id', read_only=True)
	team_id = ObjectIdField(write_only=True)
	class Meta:
		model = User
		fields = ['id', 'name', 'email', 'team', 'team_id']

class ActivitySerializer(serializers.ModelSerializer):
	id = ObjectIdField(read_only=True)
	user = ObjectIdField(source='user_id', read_only=True)
	user_id = ObjectIdField(write_only=True)
	class Meta:
		model = Activity
		fields = ['id', 'user', 'user_id', 'type', 'distance', 'duration']

class WorkoutSerializer(serializers.ModelSerializer):
	id = ObjectIdField(read_only=True)
	user = ObjectIdField(source='user_id', read_only=True)
	user_id = ObjectIdField(write_only=True)
	class Meta:
		model = Workout
		fields = ['id', 'user', 'user_id', 'workout', 'reps']

class LeaderboardSerializer(serializers.ModelSerializer):
	id = ObjectIdField(read_only=True)
	team = ObjectIdField(source='team_id', read_only=True)
	team_id = ObjectIdField(write_only=True)
	class Meta:
		model = Leaderboard
		fields = ['id', 'team', 'team_id', 'points']
