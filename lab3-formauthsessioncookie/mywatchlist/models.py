from django.db import models


# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    rating = models.IntegerField(default=1)
    release_date = models.DateField()
    review = models.TextField(blank=True, null=True)
