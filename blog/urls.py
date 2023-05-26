from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns=[
    path('', views.blogHome, name='blogHome'),
    path('create/', views.create, name='create'),
    path('post_list/',views.post_list, name='post_list'),
    path('detail/<int:id>', views.post_detail, name='post_detail'),
    path('update/<int:id>/', views.post_update, name='post_update'),
    path('delete/<int:id>/',views.post_delete, name='post_delete'),
    path('create_comment/<int:id>/', views.create_comment, name='create_comment'),
    path('update_comment/<int:post_id>/<int:com_id>', views.update_comment, name='update_comment'),
    path('delete_comment/<int:post_id>/<int:com_id>', views.delete_comment, name='delete_comment'),
]