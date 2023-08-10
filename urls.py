from django.urls import path

from . import views

urlpatterns = [
    path('lesson_4/', views.index),
]