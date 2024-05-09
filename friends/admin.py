from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import FriendRequest


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'created_at', 'status')
    list_filter = ('sender', 'receiver', 'created_at')
    date_hierarchy = 'created_at'
