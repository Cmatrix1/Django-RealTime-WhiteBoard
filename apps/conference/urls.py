from django.urls import path
from conference.views import Conference


urlpatterns = [
    path("conference/<slug:slug>/", Conference.as_view(), name="conference"),
]
