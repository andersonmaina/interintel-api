from .models import Sender, Notification

class EmptyNotificationsError(ValueError):
    pass

def create_sender_with_notifications(validated_data):
    """
    Takes validated serializer data, creates the Sender and its
    Notifications in one transaction, and returns (sender, notifications).
    Business-rule checks (not just field-shape checks) live here.
    """
    notifications_data = validated_data.pop("notifications")
    if not notifications_data:
        raise EmptyNotificationsError("At least one notification is required.")
    #sender + bulk_create