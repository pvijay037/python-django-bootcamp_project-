from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Profile

class ProfileSeralizer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail',read_only=True, ) 
    class Meta:
        model = Profile
        fields = ['url','id','user','image',]

class UserSeralizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=False)
    old_password = serializers.CharField(write_only=True,required=False)
    username = serializers.CharField(read_only=True)
    profile = ProfileSeralizer(read_only=True)
    def validate(self, data):
        request_method = self.context['request'].method
        password = data.get('password',None)
        if request_method == 'POST':
            if password == None:
                raise serializers.ValidationError({"info":"Please provide a password"})
        elif request_method == 'PUT' or request_method == 'PATCH':
            old_password = data.get('old_password',None)
            if password != None and old_password ==None:
                raise serializers.ValidationError({"info":"Please provide the old password"})
        raise data

    def create(self, validated_data):
        password=validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        try:
            user =instance
            if 'password' in validated_data:
                password = validated_data.pop('password')
                old_password = validated_data.pop('old_password')
                if user.check_password(old_password):
                    user.set_password(password)
                else:
                    raise Exception("Old password is incorrect")
        except Exception as err:
            raise serializers.ValidationError({"info":err})
        return super(UserSeralizer,self).update(instance, validated_data)
    
    class Meta:
        model = User
        fields = ['url','id','username','first_name','password','is_staff','email','old_password','profile']