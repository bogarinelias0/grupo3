from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
# Create your views here.
from .models import Contrato
from myapps.ofertas.models import Oferta


def contratar(request, id_oferta=None, id_usuario=None):
    contrato = Contrato()
    contrato.contratante = request.user
    if id_oferta:
        contrato.oferta = Oferta.objects.get(pk=id_oferta)
        if contrato.oferta:
            contrato.contratado = Oferta.objects.get(pk=id_oferta).ofertante
        else:
            raise ValueError
    elif id_usuario:
        contrato.contratado = User.objects.get(pk=id_usuario)
        if contrato.contratado is None:
            raise ValueError
    else:
        raise ValueError
    contrato.save()
    return redirect('contratos_detalles', pk=contrato.id)


@method_decorator([login_required], name='dispatch')
class ContratoDetailView(DetailView):
    model = Contrato
    template_name = 'contratos/detalles_contrato.html'


@method_decorator([login_required], name="dispatch")
class UpdateDetailView(UpdateView):
    model = Contrato
    template_name = 'contratos/detalles_contrato.html'
