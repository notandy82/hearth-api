from django.db import models
import datetime
from django.contrib.auth.models import User
from parties.models import Party


class Event(models.Model):
    """
    Stores info about events
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    about = models.TextField()
    when = models.DateTimeField()

    def __unicode__(self):
        return self.title
