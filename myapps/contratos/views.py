from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import reverse, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, Http404
# Create your views here.
from .models import Contrato
from myapps.ofertas.models import Oferta
from .forms import PuntajeForm
from django.views.defaults import page_not_found
 
def mi_error_404(request,exception):
    nombre_template = '404.html'
 
    return page_not_found(request, template_name=nombre_template)

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


# @method_decorator([login_required], name='dispatch')
# class ContratoDetailView(FormMixin, DetailView):
#     model = Contrato
#     template_name = 'contratos/detalles_contrato.html'
#     form_class = PuntajeForm

#     def get_success_url(self):
#         print('EXITOS')
#         return reverse('contratos_detalles', kwargs={'pk': self.object.id})

#     def get_context_data(self, **kwargs):
#         context = super(ContratoDetailView, self).get_context_data(**kwargs)
#         context['form'] = PuntajeForm(instance=self.object)
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         print(form)
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


@login_required
def contrato_detail_view(request, pk):
    # contrato = Contrato.objects.get(id=pk)
    contrato = get_object_or_404(Contrato, id=pk)
    context = {'object': contrato}
    if request.user == contrato.contratante or request.user == contrato.contratado:
        if request.method == 'POST':
            form = PuntajeForm(request.POST, instance=contrato)
            if form.is_valid():
                form.save()
                return redirect('contratos_detalles', pk=contrato.id)
        form = PuntajeForm(instance=contrato)
        context['form'] = form
    else:
        # para los que están logueados pero no tienen nada que ver
        raise Http404()
    return render(request, 'contratos/detalles_contrato.html', context=context)


@method_decorator([login_required], name="dispatch")
class ContratoUpdateView(UpdateView):
    model = Contrato
    template_name = 'contratos/detalles_contrato.html'


@login_required
def cancelar_contrato(request, id_contrato):
    """Funcion para cancelar un contrato antes de enviar al trabajador"""
    contrato = Contrato.objects.get(id=id_contrato)
    if request.user == contrato.contratante:
        if contrato:
            id_oferta = contrato.oferta.id
            contrato.delete()
            return redirect('oferta_detalles', pk=id_oferta)
        else:
            return redirect("ofertas")
    else:
        raise Http404()
    

@login_required
def aceptar_contrato(request, id_contrato):
    """Función para aceptar el contrato que alguien nos envía."""
    contrato = Contrato.objects.get(id=id_contrato)
    if request.user == contrato.contratado:
        contrato.aceptar()
        contrato.save()
    return redirect('contratos_detalles', pk=contrato.id)


@login_required
def rechazar_contrato(request, id_contrato):
    contrato = Contrato.objects.get(id=id_contrato)
    if request.user == contrato.contratado:
        contrato.rechazar()
        contrato.delete()
        return redirect('mis_contratos')


@login_required
def confirmar_contrato(request, id_contrato):
    """Confirmar el envío del contrato al trabajador."""
    contrato = Contrato.objects.get(id=id_contrato)
    if request.user == contrato.contratante:
        contrato.confirmar()
        contrato.save()
    return redirect('contratos_detalles', pk=contrato.id)

@login_required
def mis_contratos(request):
    """Muestra los contratos que tengo, ya sea como contratante o contratado"""
    contratos = Contrato.objects.filter(Q(contratado=request.user)|Q(contratante=request.user)).exclude(estado='borrador')
    # contratos = Contrato.objects.
    context = {'contratos': contratos}
    return render(request, 'contratos/mis_contratos.html', context=context)

@login_required
def finalizar_contrato(request, id_contrato):
    """Finaliza el contrato, significa que el trabajo se ha terminado"""
    contrato = Contrato.objects.get(id=id_contrato)
    if request.user == contrato.contratado:
        contrato.finalizar()
        contrato.save()
    return redirect('contratos_detalles', pk=contrato.id)

@login_required
def puntuar(request, id_contrato):
    """Función para puntuar un contrato/trabajo realizado, 
    ahora se usa la vista de detalles para esa función."""
    contrato = Contrato.objects.get(id=id_contrato)
    if request.method == 'POST':
        form = PuntajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contratos_detalles', pk=contrato.id)
    form = PuntajeForm(instance=contrato)
    context = {'form': form}
    return reverse_lazy('contratos_detalles', pk=contrato.id)

    # contrato_receptor = Contrato.objects.get(id=id_contrato)
    # if request.user == contrato_receptor.contratante:
    #     puntaje = request.POST.get('puntaje')
    #     if puntaje in [1, 2, 3, 4, 5]:
    #         contrato_receptor.set_puntaje(puntaje)
    #         contrato_receptor.save()
    #         return redirect('contratos_detalles', pk=contrato_receptor.id)
    # else:
    #     return redirect('contratos_detalles', pk=contrato_receptor.id)
