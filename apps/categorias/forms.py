from django import forms
from .models import Categoria


class CategoriaFormForm(forms.ModelForm):
    """Form definition for CategoriaForm."""

    class Meta:
        """Meta definition for CategoriaFormform."""

        model = Categoria
        fields = ('nombre', 'foto', 'descripcion',)
