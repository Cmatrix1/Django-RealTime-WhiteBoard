from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from whiteboard.models import ConferenceRoom, Participant


class IsUserInConfrence(BasePermission):
    def has_permission(self, request, view):
        if view.room.is_participant(request.user):
            return True
        return False
