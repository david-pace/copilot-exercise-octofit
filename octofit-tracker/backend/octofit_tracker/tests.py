from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Testuser", email="test@example.com", team="Alpha")
        self.assertEqual(user.name, "Testuser")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Alpha", description="Testteam")
        self.assertEqual(team.name, "Alpha")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user="Testuser", type="Run", duration=30, date="2024-01-01")
        self.assertEqual(activity.type, "Run")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team="Alpha", points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Do pushups", difficulty="Easy")
        self.assertEqual(workout.name, "Pushups")
