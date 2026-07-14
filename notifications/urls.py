from django.urls import path
from .views import CreateSenderWithNotificationsView

urlpatterns = [
    path(
        "senders/bulk/",
        CreateSenderWithNotificationsView.as_view(),
        name="sender-bulk-create",
    ),
]