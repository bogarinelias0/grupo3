from django import forms

from .models import Oferta, ImagenOferta
from django.forms import modelformset_factory, inlineformset_factory
# from django.forms.models import inlineformset_factory


# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
# from .custom_crispy_layout import *


class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        # fields = '__all__'
        exclude = ('ofertante',)

class ImagenOfertaForm(forms.ModelForm):
    class Meta:
        model = ImagenOferta
        fields = '__all__'


ImagenFormSet = modelformset_factory(ImagenOferta, fields=('imagen',), can_delete=True)
CrearOfertaFormSet = inlineformset_factory(Oferta, ImagenOferta, fields=('imagen',))
