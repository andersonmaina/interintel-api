from django.test import TestCase
from notifications.serializers import SenderNotificationSerializer


class SenderNotificationSerializerTests(TestCase):
    def _valid_payload(self, **overrides):
        payload = {
            "name": "Equity Bank Kenya",
            "email": "notifications@equitybank.co.ke",
            "notifications": [
                {"title": "Account Opened", "channel": "email", "message": "Welcome to Equity Bank."},
            ],
        }
        payload.update(overrides)
        return payload

    def test_valid_payload_passes(self):
        serializer = SenderNotificationSerializer(data=self._valid_payload())
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_missing_email_fails(self):
        serializer = SenderNotificationSerializer(data=self._valid_payload(email=""))
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_invalid_channel_fails(self):
        payload = self._valid_payload()
        payload["notifications"][0]["channel"] = "carrier-pigeon"
        serializer = SenderNotificationSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_missing_notification_title_fails(self):
        payload = self._valid_payload()
        del payload["notifications"][0]["title"]
        serializer = SenderNotificationSerializer(data=payload)
        self.assertFalse(serializer.is_valid())