from rest_framework import serializers
from task.models import Task,TaskList,Attachment

from house.models import House
from users.models import Profile

class TaskListSeralizer(serializers.ModelSerializer):
    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(),many=False,view_name='house-detail')
    created_by = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(),many=False,view_name='profile-detail')
    tasks = serializers.HyperlinkedRelatedField(queryset=Task.objects.all(),many=True,view_name='task-detail')
    
    class Meta:
        model = TaskList
        fields = ['url','id','created_on','completed_on','created_by','house','name','description','status','tasks']
        read_only_fields =['created_on','status']


class TaskSeralizer(serializers.ModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(),many=False,view_name='profile-detail')
    completed_by = serializers.HyperlinkedRelatedField(queryset=Profile.objects.all(),many=False,view_name='profile-detail')
    task_list = serializers.HyperlinkedRelatedField(queryset=TaskList.objects.all(),many=False,view_name='tasklist-detail')
    attachments = serializers.HyperlinkedRelatedField(queryset=Attachment.objects.all(),many=True,view_name='attachment-detail')

    class Meta:
        model = Task
        fields = ['url','id','created_on','completed_on','created_by','completed_by','task_list','name','description','status','attachments']

    def validate_task_list(self, value):
        user_profile = self.context['request'].user.profile       
        if value not in user_profile.house.lists.all():
            raise serializers.ValidationError({"info":"TaslList does nog provide to which is user member"})
        return value
    def create(self, validated_data):
        user_profile = self.context['request'].user.profile  
        task = Task.objects.create(**validated_data)  
        task.created_by =  user_profile
        task.save()
        return task 


        return super().create(validated_data)

class AttachmentSeralizer(serializers.ModelSerializer):
    task = serializers.HyperlinkedRelatedField(queryset=Task.objects.all(),many=False,view_name='task-detail')

    def validate(self, attrs):
        user_profile = self.context['request'].user.profile
        task = attrs['task']
        task_list =TaskList.objects.get(tasks__id__exact=task.id)
        if task_list not in user_profile.house.lists.all():
            raise serializers.ValidationError({"task":"Task provided does not belong to house for which user is member."})
        return attrs
    
    class Meta:
        model = Attachment
        fields = ['id','created_on','data','task']