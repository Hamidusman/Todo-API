from django.shortcuts import render
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task
# Create your views here.

from rest_framework.decorators import api_view

@api_view(['GET'])
def todolist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todoitem(request, pk):
    