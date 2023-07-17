from django.db import models
import uuid 

NOT_COMPLETE = 'NC'
COMPLETE ='C'
TASK_STATUS_CHOICES = [
    (NOT_COMPLETE,'Not Completed'),
    (COMPLETE,'Complete')
]

class TaskList(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(null=True,blank=True)
    created_by = models.ForeignKey('users.Profile',null=True,blank=True,on_delete=models.SET_NULL,related_name="lists")
    house = models.ForeignKey('house.House',on_delete=models.CASCADE,related_name="lists")
    name = models.CharField(max_length=120)
    description = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=2,choices=TASK_STATUS_CHOICES,default=NOT_COMPLETE)

    def __str__(self):
        return f'{self.id}|{self.name}'


class Task(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(null=True,blank=True)
    created_by = models.ForeignKey('users.Profile',null=True,blank=True,on_delete=models.SET_NULL,related_name='created_tasks')
    completed_by = models.ForeignKey('users.Profile',null=True,blank=True,on_delete=models.SET_NULL,related_name='completed_tasks')
    task_list = models.ForeignKey('task.TaskList',on_delete=models.CASCADE,related_name='tasks')
    name = models.CharField(max_length=120)
    description = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=2,choices=TASK_STATUS_CHOICES,default=NOT_COMPLETE)

    def __str__(self):
        return f'{self.id}|{self.name}'


class Attachment(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    data = models.FileField(upload_to='media/tasks/')
    task = models.ForeignKey('task.Task',on_delete=models.CASCADE,related_name="attachments")

    def __str__(self):
        return f'{self.id}|{self.task}'