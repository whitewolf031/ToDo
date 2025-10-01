from django.shortcuts import render
from rest_framework import viewsets 
from .models import Todo
from .serializers import SerializerTodo
from rest_framework.permissions import IsAuthenticated

class UserTodo(viewsets.ModelViewSet):
    # queryset = Todo.objects.all()
    serializer_class = SerializerTodo
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)