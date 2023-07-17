from rest_framework import routers
from task.viewsets import TaskViewset,TaskListViewset,AttachmentViewset
router = routers.DefaultRouter()

router.register('tasks',TaskViewset)
router.register('task-lists',TaskListViewset)
router.register('attachments',AttachmentViewset)




