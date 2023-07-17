from rest_framework import routers
from users.viewsets import UserViewset,ProfileViewset
router = routers.DefaultRouter()

router.register('users_creates',UserViewset),
router.register('profile_creates',ProfileViewset),

