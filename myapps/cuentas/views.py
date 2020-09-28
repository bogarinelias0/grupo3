from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.models import User

from .forms import UserForm, PerfilForm, RegistrarUsuarioForm

# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = RegistrarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            authenticate(request, username=username, password=password)
            return redirect('login')
    form = RegistrarUsuarioForm()
    return render(request, 'cuentas/register.html', {'form': form})


@login_required
@transaction.atomic
def editar_perfil(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, '¡Perfil editado con éxito!')
            return redirect('detalles_usuario', pk=request.user.id)
        else:
            messages.error(request, 'Por favor, corrija los errores abajo.')
    else:
        user_form = UserForm(instance=request.user)
        perfil_form = PerfilForm(instance=request.user.perfil)
    return render(request, 'perfiles/editar.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })


class UserDetailView(DetailView):
    model = User
    template_name = "perfiles/detalles.html"
