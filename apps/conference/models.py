from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_rooms')
    participants = models.ManyToManyField(User, through='Participant')
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    allow_anonymous = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def is_participant(self, user: User) -> bool:
        if self.allow_anonymous or self.admin == user:
            return True
        return self.participants.filter(id=user.id).exists()

    def is_admin(self, user: User):
        return self.admin == user

class Participant(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.room.name)
