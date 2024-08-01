from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('subject/<str:value>/', views.subject),
]