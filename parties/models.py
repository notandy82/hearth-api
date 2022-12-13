from django.db import models
from django.contrib.auth.models import User


class Party(models.Model):
    """
    Model to organize posts for a group
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='images/', default='../default_post_q98lks', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}'
