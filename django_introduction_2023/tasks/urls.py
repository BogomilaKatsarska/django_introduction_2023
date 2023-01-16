from django.urls import path

from django_introduction_2023.tasks.views import index, get_all_tasks, index2

urlpatterns = (
    path('', index),
    path('all/', get_all_tasks),
    path('index2', index2),
)