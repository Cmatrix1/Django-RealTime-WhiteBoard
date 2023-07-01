from django.db import models


class ImageBoard(models.Model):
    room = models.ForeignKey("conference.ConferenceRoom", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/board")
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room.name} {self.create_at.strftime('%Y/%m/%d  %H:%M')}" 
    