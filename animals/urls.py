from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from animals import views


urlpatterns = [
    path('animals/', views.Animal_Objects.as_view()),
    path('cat/', views.Cat_Objects.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)  # generalize urls
