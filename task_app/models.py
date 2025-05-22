from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    user_id = models.IntegerField()  # References User ID from User Service
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title