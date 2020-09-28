from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
from .models import Oferta, ImagenOferta
from .forms import OfertaForm, ImagenFormSet, CrearOfertaFormSet
from django.forms import inlineformset_factory
from django.shortcuts import redirect, Http404


class OfertaListView(ListView):
    model = Oferta
    template_name = 'ofertas/lista_ofertas.html'


@method_decorator([login_required], name='dispatch')
class OfertaCreateView(CreateView):
    model = Oferta
    template_name = 'ofertas/crear_oferta.html'
    exclude = ('ofertante',)

    form_class = OfertaForm
    success_url = reverse_lazy('ofertas')

    # def get(self):
    #     context['imagen_formset'] = ImagenFormSet(self.request.POST, self.request.FILES)

    def get_context_data(self, **kwargs):
        context = super(OfertaCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = CrearOfertaFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = CrearOfertaFormSet()
        return context

    def form_valid(self, form):
        """Para poner al usuario que crea el objecto como el ofertante."""
        self.object = form.save(commit=False)
        self.object.ofertante = self.request.user
        self.object.save()
        return super(OfertaCreateView, self).form_valid(form)

    def formset_valid(self, formset):
        for form in formset:
            self.object.imagen = form.save(commit=False)
            self.object.usuario = self.request.user
        # self.object.ofertante = self.request.user
        self.object.save()
        return super(CrearOfertaFormSet, self).form_valid(formset)
            


@method_decorator([login_required], name='dispatch')
class OfertaUpdateView(UpdateView):
    model = Oferta
    template_name = 'ofertas/editar_oferta.html'
    exclude = ('ofertante',)

    form_class = OfertaForm
    success_url = reverse_lazy('ofertas')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.ofertante != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(OfertaUpdateView, self).dispatch(request, *args, **kwargs)


class OfertaDetailView(DetailView):
    model = Oferta
    template_name = 'ofertas/detalles_oferta.html'


@login_required
def postear_oferta(request):
    # author = Author.objects.get(pk=author_id)
    OfertaInlineFormSet = inlineformset_factory(Oferta, ImagenOferta, fields=('imagen',))
    if request.method == "POST":
        form = OfertaForm(request.POST)
        formset = OfertaInlineFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            oferta = form.save(commit=False)
            oferta.ofertante = request.user
            oferta.save()
            imagenes = formset.save(commit=False)
            for imagen in imagenes:
                # asignamos oferta y usuario a la imagen
                imagen.oferta = oferta
                imagen.usuario = request.user
                imagen.save()
            return redirect('ofertas')
    else:
        form = OfertaForm()
        formset = OfertaInlineFormSet()
    return render(request, 'ofertas/crear_oferta.html', {'form': form, 'formset': formset})


@login_required
def editar_oferta(request, id):
    oferta = Oferta.objects.get(pk=id)
    OfertaInlineFormSet = inlineformset_factory(Oferta, ImagenOferta, fields=('imagen',))
    if request.method == "POST":
        form = OfertaForm(request.POST, instance=request.user)
        formset = OfertaInlineFormSet(request.POST, request.FILES, instance=oferta)
        if form.is_valid() and formset.is_valid():
            oferta = form.save(commit=False)
            # oferta.ofertante = request.user
            oferta.save()
            imagenes = formset.save(commit=False)
            for imagen in imagenes:
                # asignamos oferta y usuario a la imagen
                imagen.oferta = oferta
                # imagen.usuario = request.user
                imagen.save()
            return redirect('ofertas')
    else:
        form = OfertaForm(instance=request.user)
        formset = OfertaInlineFormSet(instance=oferta)
    return render(request, 'ofertas/crear_oferta.html', {'form': form, 'formset': formset})
