from django.db import models


class Message(models.Model):
    sender = models.ForeignKey("conference.Participant", on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey("conference.ConferenceRoom", on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}: {}".format(self.sender.name, self.room.name, self.content[:50])

