from django.urls import path, include

from .views import *

urlpatterns = [
    path('plane/', PlaneApiView.as_view()),
    path('plane/<int:pk>/', PlaneDetailApiView.as_view()),
    path('flight/', FlightApiView.as_view()),
    path('flight/<int:pk>/', FlightDetailApiView.as_view()),
    path('airline/', AirlineApiView.as_view()),
    path('airline/<int:pk>/', AirlineDetailApiView.as_view()),
]
