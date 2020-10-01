from django import forms
from myapps.contratos.models import Contrato


class PuntajeForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ('puntaje', 'contratado', 'contratante')
