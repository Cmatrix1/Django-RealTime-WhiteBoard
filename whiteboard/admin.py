from django.contrib import admin
from .models import ConferenceRoom, Participant, Message

class ParticipantInline(admin.TabularInline):
    model = Participant


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'joined_at')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'room', 'created_at')
    list_filter = ('room',)


class ConferenceRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin')
    inlines = [ParticipantInline]

    def participant_count(self, obj):
        return obj.participants.count()

    participant_count.short_description = "Participant Count"


admin.site.register(ConferenceRoom
, ConferenceRoomAdmin
)
admin.site.register(Participant
, ParticipantAdmin
)
admin.site.register(Message
, MessageAdmin
)
