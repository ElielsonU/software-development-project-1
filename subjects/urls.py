from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('subject/<slug:slug>/', views.subject),
  path('avala/',views.avala,name='task-list'),
  path('elielson/',views.elielson),
]