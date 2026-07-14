from rest_framework import serializers
from .models import Sender, Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "title", "channel", "message", "status", "created_at"]
        read_only_fields = ["id", "status", "created_at"]
        
class SenderNotificationSerializer(serializers.ModelSerializer):
    notifications = NotificationSerializer(many=True)

    class Meta:
        model = Sender
        fields = ["id", "name", "email", "notifications", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Sender email required.")
        return value