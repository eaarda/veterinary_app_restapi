from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url

from .views import CityViewSet, DistrictViewSet, ColorViewSet, SpecieViewSet, ProductTypeViewSet, UnitViewSet


router = routers.DefaultRouter()
router.register(r"cities", CityViewSet)
router.register(r"districts", DistrictViewSet)
router.register(r"colors", ColorViewSet)
router.register(r"species", SpecieViewSet)
router.register(r"product-types", ProductTypeViewSet)
router.register(r"units", UnitViewSet)


urlpatterns = [
    path('', include(router.urls)),

]