from .models import Task
from django.core.exceptions import ObjectDoesNotExist

class TaskService:
    @staticmethod
    def create_task(title, description, user_id):
        return Task.objects.create(title=title, description=description, user_id=user_id)

    @staticmethod
    def get_task(task_id):
        try:
            return Task.objects.get(id=task_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def update_task(task_id, title=None, description=None):
        try:
            task = Task.objects.get(id=task_id)
            if title:
                task.title = title
            if description:
                task.description = description
            task.save()
            return task
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete_task(task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return True
        except ObjectDoesNotExist:
            return False

    @staticmethod
    def get_tasks_by_user(user_id):
        return Task.objects.filter(user_id=user_id)