from django.contrib import admin
from django.urls import path,include
from dramas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('ranking/', include('ranking.urls')),
    path('blog/',include('blog.urls')),
    path('ranking/', include('ranking.urls')),
] 