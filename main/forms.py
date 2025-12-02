from django import forms
from .models import Compania

class CompaniaForm(forms.ModelForm):
    class Meta:
        model = Compania
        fields = ['nombre', 'rut', 'direccion']
