from rest_framework.serializers import serializers
from .models import Task

class TaskSerializer(serializers.mod):
    class Meta:
        model = Task
        fields = '__all__'