from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from . import forms

# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = forms.RegistrarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            authenticate(request, username=username, password=password)
            return redirect('login')
    form = forms.RegistrarUsuarioForm()
    return render(request, 'cuentas/register.html', {'form': form})


# def logout(request):
#     logout(request)
#     return redirect('home')


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
