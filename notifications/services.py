from .models import Sender, Notification
from django.db import transaction

class EmptyNotificationsError(ValueError):
    pass

def create_sender_with_notifications(validated_data):
    #Takes validated serializer data, creates the Sender and its Notifications in one transaction, and returns (sender, notifications).
    
    notifications_data = validated_data.pop("notifications")
    if not notifications_data:
        raise EmptyNotificationsError("At least one notification is required.")
    #sender + bulk_create

def create_sender_with_notifications(validated_data):
    notifications_data = validated_data.pop("notifications")
    if not notifications_data:
        raise EmptyNotificationsError("At least one notification is required.")

    with transaction.atomic():
        sender = Sender.objects.create(**validated_data)
        notification_objs = [
            Notification(sender=sender, **data) for data in notifications_data
        ]
        return sender, notification_objs
