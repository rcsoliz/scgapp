from django import forms
from .models import Ganado

class GanadoForm(forms.ModelForm):
    class Meta:
        model = Ganado
        fields ='__all__'