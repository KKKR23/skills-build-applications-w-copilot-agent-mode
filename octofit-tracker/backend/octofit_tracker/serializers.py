from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField(max_length=100))

class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    activity_type = serializers.CharField(max_length=100)
    duration = serializers.DurationField()

class LeaderboardSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()