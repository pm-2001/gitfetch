# from django.contrib import admin,include
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
]