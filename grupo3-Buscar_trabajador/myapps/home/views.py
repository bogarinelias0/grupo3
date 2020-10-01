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

def get_categorias_for_menu(request):
    """
    Un procesador de contexto, en settings > templates se añade esta función,
    para añadir las categorías a al navbar. Este contexto se añade en cada pagina del sitio.
    """
    categorias = Categoria.objects.all()[:5]
    context = {'categorias_menu': categorias}
    return context

def acercadenosotros(request):
    
    return render(request, 'acercadenosotros.html', {})


from django.http import HttpResponse, HttpResponseNotFound

def my_view(request):
    # ...
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')