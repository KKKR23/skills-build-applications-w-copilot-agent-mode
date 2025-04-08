from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import users, teams, activity, leaderboard, workouts

class UserView(APIView):
    def get(self, request):
        user_list = list(users.find())
        return Response(user_list, status=status.HTTP_200_OK)

class TeamView(APIView):
    def get(self, request):
        team_list = list(teams.find())
        return Response(team_list, status=status.HTTP_200_OK)

class ActivityView(APIView):
    def get(self, request):
        activity_list = list(activity.find())
        return Response(activity_list, status=status.HTTP_200_OK)

class LeaderboardView(APIView):
    def get(self, request):
        leaderboard_list = list(leaderboard.find())
        return Response(leaderboard_list, status=status.HTTP_200_OK)

class WorkoutView(APIView):
    def get(self, request):
        workout_list = list(workouts.find())
        return Response(workout_list, status=status.HTTP_200_OK)

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://obscure-train-97jj4vvgg9453pj7r-8000.app.github.dev/'
    return Response({
        'users': base_url + 'users/',
        'teams': base_url + 'teams/',
        'activity': base_url + 'activity/',
        'leaderboard': base_url + 'leaderboard/',
        'workouts': base_url + 'workouts/'
    })