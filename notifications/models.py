from django.db import models

# Create your models here.
from django.db import models

class Sender(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Notification(models.Model):
    CHANNEL_VAR = [
        ("email", "Email"),
        ("sms", "SMS"),
        ("push", "Push"),
    ]
    STATUS_VAR = [
        ("pending", "Pending"),
        ("sent", "Sent"),
    ]

    sender = models.ForeignKey(
        Sender,
        related_name="notifications",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    channel = models.CharField(max_length=10, choices=CHANNEL_VAR)
    message = models.TextField()
    status = models.CharField(
        max_length=10, choices=STATUS_VAR, default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.channel} to {self.sender_id} ({self.status})"