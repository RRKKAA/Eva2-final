from django import forms
from EvaApp.models import videojuego
class formVideojuego(forms.ModelForm):
    class Meta:
        model = videojuego
        fields = '__all__'