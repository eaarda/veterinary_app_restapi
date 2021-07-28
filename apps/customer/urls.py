 
from django.urls import path, include
from rest_framework import routers

from .views import CustomerViewSet, AnimalViewSet, AppointmentViewSet


router = routers.DefaultRouter()
router.register(r"customers", CustomerViewSet)
router.register(r"animals", AnimalViewSet)
router.register(r"appointments", AppointmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]