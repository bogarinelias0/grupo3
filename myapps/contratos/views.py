from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.db.models import Q
# Create your views here.
from .models import Contrato
from myapps.ofertas.models import Oferta


@login_required
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


@login_required
def cancelar_contrato(request, id_contrato):
    contrato = Contrato.objects.get(id=id_contrato)
    if contrato:
        id_oferta = contrato.oferta.id
        contrato.delete()
        return redirect('oferta_detalles', pk=id_oferta)
    else:
        return redirect("ofertas")

@login_required
def aceptar_contrato(request, id_contrato):
    contrato = Contrato.objects.get(id=id_contrato)
    contrato.aceptar()
    contrato.save()
    return redirect('contratos_detalles', pk=contrato.id)

@login_required
def confirmar_contrato(request, id_contrato):
    contrato = Contrato.objects.get(id=id_contrato)
    contrato.confirmar()
    contrato.save()
    return redirect('contratos_detalles', pk=contrato.id)

@login_required
def mis_contratos(request):
    contratos = Contrato.objects.filter(Q(contratado=request.user)|Q(contratante=request.user))
    # contratos = Contrato.objects.
    context = {'contratos': contratos}
    return render(request, 'contratos/mis_contratos.html', context=context)

@login_required
def finalizar_contrato(request, id_contrato):
    contrato = Contrato.objects.get(id=id_contrato)
    contrato.finalizar()
    contrato.save()
    return redirect('contratos_detalles', pk=contrato.id)
