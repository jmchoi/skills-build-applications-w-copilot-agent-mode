
from django.core.management.base import BaseCommand
from pymongo import MongoClient
import uuid

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Teams
        marvel_id = str(uuid.uuid4())
        dc_id = str(uuid.uuid4())
        marvel = {'id': marvel_id, 'name': 'Team Marvel'}
        dc = {'id': dc_id, 'name': 'Team DC'}
        db.teams.insert_many([marvel, dc])

        # Users (superheroes)
        users = [
            {'id': str(uuid.uuid4()), 'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': marvel_id},
            {'id': str(uuid.uuid4()), 'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel_id},
            {'id': str(uuid.uuid4()), 'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': dc_id},
            {'id': str(uuid.uuid4()), 'name': 'Batman', 'email': 'batman@dc.com', 'team': dc_id},
        ]
        db.users.insert_many(users)

        # Map user ids for activities/workouts
        user_ids = [u['id'] for u in users]

        # Activities
        activities = [
            {'id': str(uuid.uuid4()), 'user': user_ids[0], 'type': 'run', 'distance': 5, 'duration': 30},
            {'id': str(uuid.uuid4()), 'user': user_ids[1], 'type': 'cycle', 'distance': 20, 'duration': 60},
            {'id': str(uuid.uuid4()), 'user': user_ids[2], 'type': 'swim', 'distance': 1, 'duration': 40},
            {'id': str(uuid.uuid4()), 'user': user_ids[3], 'type': 'run', 'distance': 10, 'duration': 50},
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {'id': str(uuid.uuid4()), 'user': user_ids[0], 'workout': 'Pushups', 'reps': 50},
            {'id': str(uuid.uuid4()), 'user': user_ids[1], 'workout': 'Situps', 'reps': 100},
            {'id': str(uuid.uuid4()), 'user': user_ids[2], 'workout': 'Squats', 'reps': 80},
            {'id': str(uuid.uuid4()), 'user': user_ids[3], 'workout': 'Pullups', 'reps': 20},
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard (sample)
        leaderboard = [
            {'id': str(uuid.uuid4()), 'team': marvel_id, 'points': 150},
            {'id': str(uuid.uuid4()), 'team': dc_id, 'points': 120},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
