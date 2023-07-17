from rest_framework import serializers
from house.models import House
class HouseSeralizer(serializers.ModelSerializer):
    members_count = serializers.IntegerField(read_only=True)
    members = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name='profile-detail')
    manager = serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='profile-detail')
    lists = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name='tasklist-detail')
    
    class Meta:
        model = House
        fields=['url','id','image','name','created_date','description','manager','members','members_count','lists']
        read_only_feilds=['points','completed_tasks_count','not_completed_tasks_count',]