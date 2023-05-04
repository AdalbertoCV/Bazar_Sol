from django.shortcuts import render
from django.views.generic import TemplateView

class Bienvenida(TemplateView):
    template_name = 'home.html'