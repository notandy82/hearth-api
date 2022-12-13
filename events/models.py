from django.db import models
import datetime
from django.contrib.auth.models import User


class Event(models.Model):
    """
    Stores info about events
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    when = models.DateTimeField()
    location = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title
