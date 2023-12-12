from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateTask.as_view(), name="create_task"),
    path('', views.TaskList.as_view(), name='task_list'),
    path('delete/<int:pk>', views.DeleteTask.as_view(), name="delete_task")
]