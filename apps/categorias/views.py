from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator

# Create your views here.

from .models import Categoria


class CategoriaListView(ListView):
    model = Categoria
    template_name = "categorias/listar_categorias.html"


@method_decorator([login_required, permission_required], name='dispatch')
class CategoriaCrearView(CreateView):
    model = Categoria
    template_name = "categorias/crear_categoria.html"
    fields = ('nombre', 'descripcion', 'foto')
    success_url = 'categoria_lista'


@login_required
@permission_required('categorias.can_add_categoria')
def administrar_categorias(request):
    if request.user.has_perm('categoria.can_add_categoria'):
        return render(request, template_name='categorias/administrar_categorias.html')
