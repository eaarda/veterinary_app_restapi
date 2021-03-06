from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from animals.views import AnimalViews, CatViews, DogViews, CowViews, AppointmentViews


urlpatterns = [
    path('animals/', AnimalViews.Animal_Objects.as_view()),
    path('animals/<int:pk>', AnimalViews.Animal_Detail.as_view()),
    path('cats/', CatViews.Cat_Objects.as_view()),
    path('cats/<int:pk>', CatViews.Cat_Detail.as_view()),
    path('dogs/', DogViews.Dog_Objects.as_view()),
    path('dogs/<int:pk>', DogViews.Dog_Detail.as_view()),
    path('cows/', CowViews.Cow_Objects.as_view()),
    path('cows/<int:pk>', CowViews.Cow_Detail.as_view()),
    path('appointments/', AppointmentViews.Appointments.as_view()),
    path('appointments/<int:pk>', AppointmentViews.Appointment_Detail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)  # generalize urls
