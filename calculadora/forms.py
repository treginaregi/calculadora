from django import forms
from .models import Jugadores

class CrearRetoForm(forms.Form):
    nombre = forms.CharField(label='Nombre del usuario', max_length=100)
    minutos = forms.IntegerField()

class JugadorModelForm(forms.ModelForm):
    class Meta:
        model = Jugadores
        fields = ['grupo','num_lista']