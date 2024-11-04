from django import forms
from EvaApp.models import (videojuego, computadora, usuario)
class formVideojuego(forms.ModelForm):
    class Meta:
        model = videojuego
        fields = '__all__'

class formComputadora(forms.ModelForm):
    class Meta:
        model = computadora
        fields = '__all__'

class formUsuario(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'