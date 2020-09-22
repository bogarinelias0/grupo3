from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

# Create your views here.

from .models import Categoria


class CategoriaListView(ListView):
    model = Categoria
    template_name = "categorias/listar_categorias.html"


class CategoriaCrearView(CreateView):
    model = Categoria
    template_name = "categorias/create_categoria.html"
    fields = ('nombre', 'descripcion', 'foto')
