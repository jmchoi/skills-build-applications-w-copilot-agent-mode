# Djongo models for MongoDB collections
from djongo import models

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	class Meta:
		db_table = 'teams'
	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
	class Meta:
		db_table = 'users'
	def __str__(self):
		return self.name

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	type = models.CharField(max_length=50)
	distance = models.FloatField()
	duration = models.IntegerField()
	class Meta:
		db_table = 'activities'

class Workout(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
	workout = models.CharField(max_length=100)
	reps = models.IntegerField()
	class Meta:
		db_table = 'workouts'

class Leaderboard(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
	points = models.IntegerField()
	class Meta:
		db_table = 'leaderboard'
