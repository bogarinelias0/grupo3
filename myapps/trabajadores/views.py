from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from myapps.trabajadores.models import Post, Comentario
from myapps.trabajadores.forms import posteoForm
from .forms import posteoForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "trabajadores/trabajadores.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "trabajadores/detalles.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "trabajadores/crear.html"

    form_class = posteoForm
    success_url  =  "trabajadores"



class PostUpdateView(UpdateView):
    model = Post
    template_name = "trabajadores/editar.html"

    form_class = posteoForm
    success_url  =  "trabajadores"
