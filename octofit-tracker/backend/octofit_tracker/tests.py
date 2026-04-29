from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test')
        self.assertEqual(str(t), 'Test')
    def test_user_create(self):
        t = Team.objects.create(name='Test')
        u = User.objects.create(username='test', email='test@test.com', team=t)
        self.assertEqual(u.team, t)
    def test_activity_create(self):
        t = Team.objects.create(name='Test')
        u = User.objects.create(username='test', email='test@test.com', team=t)
        a = Activity.objects.create(user=u, type='run', duration=10, calories=100)
        self.assertEqual(a.user, u)
    def test_workout_create(self):
        w = Workout.objects.create(name='W', description='desc', duration=10)
        self.assertEqual(w.name, 'W')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='Test')
        u = User.objects.create(username='test', email='test@test.com', team=t)
        l = Leaderboard.objects.create(user=u, points=10)
        self.assertEqual(l.user, u)
