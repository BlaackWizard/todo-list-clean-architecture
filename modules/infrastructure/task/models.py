from django.db import models


class TaskModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    confirmed = models.BooleanField(default=False)
    category = models.CharField(max_length=100)

