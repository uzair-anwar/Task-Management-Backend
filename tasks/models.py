from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    title = models.CharField(max_length=25, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    assignee = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='assigned_tasks')
    creator = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='created_tasks', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[(
        'todo', 'To Do'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
