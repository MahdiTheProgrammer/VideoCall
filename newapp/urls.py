from django.contrib import admin
from django.urls import path, include
from newapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('videocall_opener', views.videocall_opener, name='videocall_opener'),
    path('get_token/', views.getToken),
]