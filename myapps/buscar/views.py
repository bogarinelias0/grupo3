from myapps.ofertas.models import Oferta
from django.shortcuts import render

def buscar(request):
    # hace algo acá
    palabra = request.GET.get('palabra', '')
    resultados = Oferta.objects.filter(titulo__icontains=palabra)
    context = {'resultados': resultados}
    return render(request, 'buscar/resultados.html', context=context)
