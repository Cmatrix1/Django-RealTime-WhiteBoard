from django.shortcuts import render
from django.views.generic import TemplateView



class WhiteBoardView(TemplateView):
    template_name = "whiteboard/whiteboard.html"