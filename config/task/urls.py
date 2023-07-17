from task.routers import router
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',include(router.urls)),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)