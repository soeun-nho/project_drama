from django.contrib import admin
from django.urls import path
from ranking import views

urlpatterns = [
    path("", views.rankingHome, name='rankingHome'),
]