from django.urls import path
from .views import UserListView, UserDetailView, UserTasksView

urlpatterns = [
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/users/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
    path('api/user/<int:user_id>/tasks/', UserTasksView.as_view(), name='user-tasks'),
]