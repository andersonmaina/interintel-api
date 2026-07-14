from django.contrib import admin
from .models import Sender, Notification

# Register your models here.

admin.site.register(Sender)
admin.site.register(Notification)