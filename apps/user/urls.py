from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url

from .views import UserProfileView


router = routers.DefaultRouter()


urlpatterns = [

    path('', include(router.urls)),

    url(r'', include('djoser.urls')),
    url(r'', include('djoser.urls.jwt')),

    path('profile/', UserProfileView.as_view(), name="profile"),

]