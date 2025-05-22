from django.urls import path
from .views import TaskListView, TaskDetailView

urlpatterns = [
    path('api/tasks/', TaskListView.as_view(), name='task-list'),
    path('api/tasks/<int:task_id>/', TaskDetailView.as_view(), name='task-detail'),
]