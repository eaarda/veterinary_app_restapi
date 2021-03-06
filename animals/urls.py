from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from animals.views import AnimalViews, CatViews


urlpatterns = [
    path('animals/', AnimalViews.Animal_Objects.as_view()),
    path('cats/', CatViews.Cat_Objects.as_view()),
    path('cats/<int:pk>', CatViews.Cat_Detail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)  # generalize urls
