from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
