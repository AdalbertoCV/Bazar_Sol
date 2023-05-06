from django import forms
from .models import Articulo

class FormArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'
        descripcion = forms.CharField(required=False)
        imagen = forms.ImageField(required=True)
        
        