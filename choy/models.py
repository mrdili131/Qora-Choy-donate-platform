from django.db import models
from users.models import User
import uuid

class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    sender = models.CharField(max_length=100, default='Anonymous sender')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    card = models.CharField(max_length=100, null=True, blank=True)
    valid = models.CharField(max_length=20, null=True, blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} || {self.sent_at.ctime()}'
    
    