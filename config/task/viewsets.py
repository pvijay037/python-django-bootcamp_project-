from rest_framework import viewsets,response,filters
from task.models import Task,TaskList,Attachment
from task.seralizers import TaskSeralizer,TaskListSeralizer,AttachmentSeralizer
from task.permissions import IsTaskListAuthenticatedOrReadOnly,IsTaskAuthenticatedOrReadOnly,IsAttachmentAuthenticatedOrReadOnly
from rest_framework.decorators import action
from task.models import COMPLETE,NOT_COMPLETE 
from django.utils import timezone
from rest_framework import status as s
from django_filters.rest_framework import DjangoFilterBackend


class TaskViewset(viewsets.ModelViewSet):
    permission_classes=[IsTaskAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSeralizer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['status',]
    search_fields = ['user','status']


    def get_queryset(self):
        queryset = super(TaskViewset,self).get_queryset()
        user_profile = self.request.user.profile
        updated_queryset = queryset.filter(created_by = user_profile)
        return updated_queryset
    @action(detail=True, methods=['patch'])
    def update_task_status(self, request, pk=None):
        try:
            task = self.get_object()
            profile = request.user.profile
            status = request.data['status']
            if status == NOT_COMPLETE:
                if task.status == COMPLETE:
                    task.status = NOT_COMPLETE
                    task.completed_on =None
                    task.completed_by = None
                else:
                    raise Exception("Task is alredy as not completed.")
            elif status == COMPLETE:
                if task.status ==NOT_COMPLETE:
                    task.status = COMPLETE
                    task.completed_on = timezone.now()
                    task.completed_by = profile
                else:
                    raise Exception("Task already marked complete.")
                task.save()
                serialzer = TaskSeralizer(instance=task,context ={"request":request})
                return response.Response(serialzer.data,status=s.HTTP_201_CREATED)
        except Exception as e:
            return response.Response({"detail":str(e)},status=s.HTTP_400_BAD_REQUEST)


class TaskListViewset(viewsets.ModelViewSet):
    permission_classes=[IsTaskListAuthenticatedOrReadOnly,]
    queryset = TaskList.objects.all()
    serializer_class = TaskListSeralizer
    
    

class AttachmentViewset(viewsets.ModelViewSet):
    permission_classes=[IsAttachmentAuthenticatedOrReadOnly]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSeralizer

