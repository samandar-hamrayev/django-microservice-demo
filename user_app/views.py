import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .services import UserService

class UserListView(APIView):
    def get(self, request):
        users = UserService.get_all_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        user = UserService.create_user(name, email)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserDetailView(APIView):
    def get(self, request, user_id):
        user = UserService.get_user(user_id)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id):
        name = request.data.get('name')
        email = request.data.get('email')
        user = UserService.update_user(user_id, name, email)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, user_id):
        if UserService.delete_user(user_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class UserTasksView(APIView):
    def get(self, request, user_id):
        # Get user from User Service
        user = UserService.get_user(user_id)
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Fetch tasks from Task Service
        task_service_url = 'http://localhost:8000/api/tasks/'  # Task Service URL
        try:
            response = requests.get(task_service_url, params={'user_id': user_id})
            response.raise_for_status()
            tasks = response.json()
        except requests.RequestException:
            tasks = []

        # Combine user and tasks data
        serializer = UserSerializer(user)
        return Response({
            'user': serializer.data,
            'tasks': tasks
        })