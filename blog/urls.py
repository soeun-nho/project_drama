from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns=[
    path('', views.bloghome, name='bloghome'),
    path('create/', views.create, name='create'),
    path('post_list/',views.post_list, name='post_list'),
    path('update/<int:id>/', views.post_update, name='post_update'),
    path('delete/<int:id>/',views.post_delete, name='post_delete'),
    path('detail/<int:id>', views.post_detail, name='post_detail'),
]