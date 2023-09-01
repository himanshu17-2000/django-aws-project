from django.contrib import admin
from django.urls import path,include
from djangoApp import views
urlpatterns = [
    path('',views.home_page)
]
