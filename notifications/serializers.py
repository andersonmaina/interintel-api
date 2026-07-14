from rest_framework import serializers
from .models import Sender, Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "channel", "message", "status", "created_at"]
        read_only_fields = ["id", "status", "created_at"]