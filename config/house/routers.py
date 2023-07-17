from rest_framework import routers
from house.viewsets import HouseViewset
router = routers.DefaultRouter()

router.register('houses',HouseViewset),


