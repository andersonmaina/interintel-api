from django.test import TestCase
from notifications.models import Sender, Notification
from notifications.services import (
    create_sender_with_notifications,
    EmptyNotificationsError,
)


class CreateSenderWithNotificationsServiceTests(TestCase):
    def _validated_data(self, notifications_data):
        return {
            "name": "Jumia Kenya",
            "email": "alerts@jumia.co.ke",
            "notifications": notifications_data,
        }

    def test_creates_sender_and_notifications(self):
        data = self._validated_data([
            {"title": "Order Shipped", "channel": "email", "message": "Your order is on its way."},
            {"title": "Delivery Update", "channel": "sms", "message": "Arriving today between 2-5pm."},
        ])
        sender, notifications = create_sender_with_notifications(data)

        self.assertEqual(Sender.objects.count(), 1)
        self.assertEqual(Notification.objects.count(), 2)
        self.assertEqual(sender.name, "Jumia Kenya")

    def test_empty_notifications_raises(self):
        data = self._validated_data([])
        with self.assertRaises(EmptyNotificationsError):
            create_sender_with_notifications(data)

        self.assertEqual(Sender.objects.count(), 0)

