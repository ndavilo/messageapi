from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    sender      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
    receiver    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')        
    value       = models.CharField(max_length=1000000)
    timestamp   = models.DateTimeField(auto_now_add=True)
    is_read     = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    class Meta:
        ordering = ('timestamp',)