from django.contrib import admin
from task.models import Task,TaskList,Attachment
# Register your models here.
admin.site.register(Task)
admin.site.register(TaskList)
admin.site.register(Attachment)
