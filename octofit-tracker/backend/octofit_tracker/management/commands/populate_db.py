
import uuid
from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(id=str(uuid.uuid4()), name='Team Marvel')
        dc = Team.objects.create(id=str(uuid.uuid4()), name='Team DC')

        # Users (superheroes)
        spiderman = User.objects.create(id=str(uuid.uuid4()), name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        ironman = User.objects.create(id=str(uuid.uuid4()), name='Iron Man', email='ironman@marvel.com', team=marvel)
        wonderwoman = User.objects.create(id=str(uuid.uuid4()), name='Wonder Woman', email='wonderwoman@dc.com', team=dc)
        batman = User.objects.create(id=str(uuid.uuid4()), name='Batman', email='batman@dc.com', team=dc)

        # Activities
        Activity.objects.create(id=str(uuid.uuid4()), user=spiderman, type='run', distance=5, duration=30)
        Activity.objects.create(id=str(uuid.uuid4()), user=ironman, type='cycle', distance=20, duration=60)
        Activity.objects.create(id=str(uuid.uuid4()), user=wonderwoman, type='swim', distance=1, duration=40)
        Activity.objects.create(id=str(uuid.uuid4()), user=batman, type='run', distance=10, duration=50)

        # Workouts
        Workout.objects.create(id=str(uuid.uuid4()), user=spiderman, workout='Pushups', reps=50)
        Workout.objects.create(id=str(uuid.uuid4()), user=ironman, workout='Situps', reps=100)
        Workout.objects.create(id=str(uuid.uuid4()), user=wonderwoman, workout='Squats', reps=80)
        Workout.objects.create(id=str(uuid.uuid4()), user=batman, workout='Pullups', reps=20)

        # Leaderboard
        Leaderboard.objects.create(id=str(uuid.uuid4()), team=marvel, points=150)
        Leaderboard.objects.create(id=str(uuid.uuid4()), team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
