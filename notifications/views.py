from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SenderNotificationSerializer, NotificationSerializer
from .services import create_sender_with_notifications, EmptyNotificationsError

# Create your views here.

class CreateSenderWithNotificationsView(APIView):
    def post(self, request):
        serializer = SenderNotificationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"success": False, "message": "Validation failed", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            sender, notifications = create_sender_with_notifications(serializer.validated_data)
        except EmptyNotificationsError as exc:
            return Response(
                {"success": False, "message": str(exc), "details": {}},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as exc: #debug
            return Response(
                {"success": False, "message": "Unexpected error", "details": str(exc)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return Response(
            {
                "success": True,
                "sender_id": sender.id,
                "created_count": len(notifications),
                "notifications": NotificationSerializer(notifications, many=True).data,
            },
            status=status.HTTP_201_CREATED,
        )




