from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getweather/', views.getweather, name='getweather'),
    path('home/', views.home, name='home'),
]