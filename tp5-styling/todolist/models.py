from django.db import models


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
