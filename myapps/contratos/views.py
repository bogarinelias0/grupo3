from django.shortcuts import render
from django.views.generic import DetailView
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


class ContratoDetailView(DetailView):
    model = Contrato
    template_name = 'contratos/detalles_contrato.html'
