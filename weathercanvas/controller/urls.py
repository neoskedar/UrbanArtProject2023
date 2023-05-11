from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getweather/', views.getweather, name='getweather'),
    path('getweather/<str:lat>/<str:long>/', views.getweather, name='getweather'),
    path('getlocation/', views.getlocation, name='getlocation'),
    path('home/', views.home, name='home'),
]