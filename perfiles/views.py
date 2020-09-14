from django.shortcuts import render
from django.views.generic import DetailView
# Create your views here.
from .models import Perfil


class PerfilDetailView(DetailView):
    model = Perfil
    template_name = 'perfiles/detalles.html'
