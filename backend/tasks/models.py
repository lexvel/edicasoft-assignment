from django.db import models
from django.conf import settings


class Task(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='tasks',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
