from rest_framework import viewsets,mixins

from django.contrib.auth.models import User
from users.seralizers import UserSeralizer,ProfileSeralizer
from users.permissions import IsUserAuthenticatedOrReadOnly,IsProfileAuthenticatedOrReadOnly
from users.models import Profile

class UserViewset(viewsets.ModelViewSet):
    permission_classes=[IsUserAuthenticatedOrReadOnly,]
    queryset=User.objects.all()
    serializer_class=UserSeralizer

class ProfileViewset(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    permission_classes =[IsProfileAuthenticatedOrReadOnly,]
    queryset=Profile.objects.all()
    serializer_class=ProfileSeralizer