from django.db import models
from django.contrib.auth.models import User
from parties.models import Party
from django.utils.text import Truncator


class Event(models.Model):
    """
    Model to allow owner to post events for the party
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=False, blank=False)
    time = models.TimeField(auto_now_add=False, blank=False)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        truncated_title = Truncator(self.title)
        return truncated_title.chars(30)
