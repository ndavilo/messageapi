from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    name            = models.CharField(max_length=1000)
    creator         = models.ForeignKey(User, on_delete=models.CASCADE)
    allowed_users   = models.ManyToManyField(User, related_name='allowedusers')

class Message(models.Model):
    value   = models.CharField(max_length=1000000)
    date    = models.DateTimeField(default=timezone.now)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    room    = models.ForeignKey(Room, on_delete=models.CASCADE)