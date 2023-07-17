from django.db import models

# Create your models here.

class House(models.Model):
    name = models.CharField(max_length=200)
    image=models.FileField(upload_to='media/house_media',null=True,blank=True)
    created_date =models.DateTimeField(auto_now_add=True)
    description =  models.TextField()
    manager = models.OneToOneField('users.profile',on_delete=models.SET_NULL,null=True,blank=True,related_name='manager_house')
    points = models.IntegerField(default=0)
    completed_tasks_count = models.IntegerField(default=0)
    not_completed_tasks_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.name}|{self.manager}'
