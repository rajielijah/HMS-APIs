from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hms import views


router = routers.DefaultRouter()
router.register(r'api/hostel', views.HostelView)
router.register(r'api/block', views.BlockView)
router.register(r'api/room', views.RoomView)
router.register(r'api/warden', views.WardenView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

