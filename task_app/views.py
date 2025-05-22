from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer
from .services import TaskService

class TaskListView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        if user_id:
            tasks = TaskService.get_tasks_by_user(user_id)
        else:
            tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        title = request.data.get('title')
        description = request.data.get('description', '')
        user_id = request.data.get('user_id')
        task = TaskService.create_task(title, description, user_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TaskDetailView(APIView):
    def get(self, request, task_id):
        task = TaskService.get_task(task_id)
        if task:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, task_id):
        title = request.data.get('title')
        description = request.data.get('description')
        task = TaskService.update_task(task_id, title, description)
        if task:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, task_id):
        if TaskService.delete_task(task_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)