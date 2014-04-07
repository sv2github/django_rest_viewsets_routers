from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

from task.models import Task
from api.serializers import TaskSerializer
from api.permissions import IsOwnerOrReadOnly

class TaskMixin(object):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_class = (IsOwnerOrReadOnly, )
    
    def pre_save(self, obj):
        obj.owner = self.request.user

class TaskViewSet(TaskMixin, viewsets.ModelViewSet):
    pass

task_list = TaskViewSet.as_view({
	
	'get':'list',
	'post':'create'
})

task_detail = TaskViewSet.as_view({

	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
})

task_router = DefaultRouter()
task_router.register(r'tasks', TaskViewSet)
