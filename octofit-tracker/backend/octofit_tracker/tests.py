from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class OctoFitAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_users_endpoint(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teams_endpoint(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activity_endpoint(self):
        response = self.client.get('/activity/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workouts_endpoint(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)