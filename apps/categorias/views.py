from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import redirect, reverse

# Create your views here.

from .models import Categoria


class CategoriaListView(ListView):
    model = Categoria
    template_name = "categorias/listar_categorias.html"


@method_decorator([login_required, permission_required('categorias.can_add_categoria')], name="dispatch")
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = "categorias/editar_categoria.html"
    fields = '__all__'
    # success_url = 'categoria_lista'

    def get_context_data(self, **kwargs):
        context=super(CategoriaUpdateView, self).get_context_data(**kwargs)
        next_page = self.request.GET.get('next')
        if next_page:
            context["next"] = next_page
        return context

    def get_success_url(self):
        redirect_to = self.request.POST.get('next')
        return redirect_to or reverse('categoria_lista')


@method_decorator([login_required, permission_required('categorias.can_add_categoria')], name="dispatch")
class CategoriaCrearView(CreateView):
    model = Categoria
    template_name = "categorias/crear_categoria.html"
    fields = ('nombre', 'descripcion', 'foto')
    # success_url = 'categoria_lista'

    def get_context_data(self, **kwargs):
        context = super(CategoriaCrearView, self).get_context_data(**kwargs)
        next_page = self.request.GET.get('next')
        if next_page:
            context["next"] = next_page
        return context

    def get_success_url(self):
        redirect_to=self.request.POST.get('next')
        print(redirect_to)
        return redirect_to or reverse('categoria_lista')


@login_required
@permission_required('categorias.can_add_categoria')
def administrar_categorias(request):
    if request.user.has_perm('categoria.can_add_categoria'):
        categorias = Categoria.objects.all()
        contexto = {'categorias': categorias }
        return render(request, template_name='categorias/administrar_categorias.html', context=contexto)


@login_required
@permission_required('categorias.can_delete_categoria')
def borrar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
        categoria.delete()
        messages.success(request, 'Categoría Borrada')
    except Exception:
        messages.error(request, 'No se pudo borrar la categoría')
    return redirect('categoria_administrar')
