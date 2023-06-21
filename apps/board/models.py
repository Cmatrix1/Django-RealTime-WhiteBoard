from django.db import models


class ImageBoard(models.Model):
    room = models.ForeignKey("conference.ConferenceRoom", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/board")
    