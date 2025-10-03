from rest_framework import serializers
from .models import Todo

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "description"]

class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "description", "completed", "created_at"]
