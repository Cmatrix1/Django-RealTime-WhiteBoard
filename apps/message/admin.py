from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'room', 'created_at')
    list_filter = ('room',)


admin.site.register(Message
, MessageAdmin
)