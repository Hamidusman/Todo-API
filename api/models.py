from django.db import models

# Create your models here.
class Task(models.Mode):
    title = models.CharField(max_length=30)
    completed = models.BooleanField(default=False, blank=True, null=True)
 