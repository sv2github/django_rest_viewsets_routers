from django.db import models

# Create your models here.
class Task(models.Model):
    owner = models.ForeignKey('auth.User', related_name = 'tasks')
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()

