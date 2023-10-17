from django.db import models
from django.utils.timezone import now

# Create your models here.

class Comment(models.Model):
    title = models.CharField(max_length=128)
    comment = models.TextField()
    date_time = models.DateTimeField(default=now)
