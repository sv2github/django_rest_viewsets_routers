from rest_framework import serializers
from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.Field('owner.username')

    class Meta:
	model = Task
	fields = ('title', 'description', 'completed', 'owner')


