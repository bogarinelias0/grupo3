from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
from .models import Oferta
from .forms import OfertaForm

class OfertaListView(ListView):
    model = Oferta
    template_name = 'ofertas/lista_ofertas.html'


@method_decorator([login_required], name='dispatch')
class OfertaCreateView(CreateView):
    model = Oferta
    template_name = 'ofertas/crear_oferta.html'
    exclude = ('ofertante',)
    success_url = 'ofertas'

    form_class = OfertaForm
    success_url = reverse_lazy('ofertas')

    def form_valid(self, form):
        """Para poner al usuario que crea el objecto como el ofertante."""
        self.object = form.save(commit=False)
        self.object.ofertante = self.request.user
        self.object.save()
        return super(OfertaCreateView, self).form_valid(form)


class OfertaDetailView(DetailView):
    model = Oferta
    template_name = 'ofertas/detalles_oferta.html'

