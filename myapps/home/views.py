from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.views.generic import TemplateView
from myapps.categorias.models import Categoria


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        return context
