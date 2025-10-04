from django.shortcuts import render
from rest_framework import viewsets 
from .models import Todo
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

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
    
    @action(detail=False, methods=["get"])
    def statistic(self, request):
        todos = self.get_queryset()
        completed_count = todos.filter(completed=True).count()
        not_completed_count = todos.filter(completed=False).count()

        return Response({
            "completed": completed_count,
            "not_completed": not_completed_count,
            "total": todos.count()
        })
