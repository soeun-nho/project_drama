from django.contrib import admin
from django.urls import path
from ranking import views

urlpatterns = [
    path("", views.ranking,  name='ranking'),
   #두번째 페이지도 만들까
]