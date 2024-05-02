from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskList(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.task} - {self.done} (by {self.owner})"
