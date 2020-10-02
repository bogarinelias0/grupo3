from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.views.generic import TemplateView
from myapps.categorias.models import Categoria
from django.views.defaults import page_not_found
 



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
 
def mi_error_404(request,exeption):
    nombre_template = '404.html'
 
    return HttpResponseNotFound(request, template_name='404')
