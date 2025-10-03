from django.shortcuts import render
from rest_framework import viewsets 
from .models import Todo
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class UserTodo(viewsets.ModelViewSet):
    # queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return TodoCreateSerializer
        return TodoUpdateSerializer