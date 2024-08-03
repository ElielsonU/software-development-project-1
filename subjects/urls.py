from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('subject/<slug:slug>/', views.subject),
  path('',views.tasklist,name='task-list'),
]