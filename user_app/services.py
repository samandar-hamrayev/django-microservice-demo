from .models import User
from django.core.exceptions import ObjectDoesNotExist

class UserService:
    @staticmethod
    def create_user(name, email):
        return User.objects.create(name=name, email=email)

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def update_user(user_id, name=None, email=None):
        try:
            user = User.objects.get(id=user_id)
            if name:
                user.name = name
            if email:
                user.email = email
            user.save()
            return user
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete_user(user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return True
        except ObjectDoesNotExist:
            return False

    @staticmethod
    def get_all_users():
        return User.objects.all()