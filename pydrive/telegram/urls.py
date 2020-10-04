from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from telegram import views

urlpatterns = [
    path('telegram', views.telegram,name='telegram'),
    path('single', views.single,name='single'),
    path('export/', views.export)
  
] 
