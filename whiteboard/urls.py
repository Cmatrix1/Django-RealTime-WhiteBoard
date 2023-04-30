from django.urls import path
from whiteboard.views import WhiteBoardView


urlpatterns = [
    path("", WhiteBoardView.as_view(), name="whiteboard")   
]
