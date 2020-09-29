from django.contrib.auth.models import User
from myapps.ofertas.models import Oferta 
from django.shortcuts import render
from myapps.ofertas.models import buscar 

def buscar(resquest):
    palabra = resquest.GET.get('titulo', '')
    resultados = Oferta.objects.filter(titulo__icontains = palabra)
    contex = {"object_list":resultados}  

    return render(resquest, 'ofertas/lista_ofertas.html',contex )

def buscar(resquest):
    palabra = resquest.GET.get('titulo', '')
    resultados = Oferta.objects.filter(titulo__icontains = palabra)
    contex = {"resultado_busqueda":resultados}  

    return render(resquest, 'ofertas/resultado_busqueda.html',contex )