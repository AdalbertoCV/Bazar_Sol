from django import forms
from .models import Cliente, Administrador
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.forms.widgets import DateInput


class FormCliente(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
        
        widgets = {
            #en forma de calendario
            'fecha_nacimiento': DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(attrs={'class':'form-control', 'data-url': reverse_lazy('busca_municipios')})
        }



class FormAdministrador(forms.ModelForm):

    class Meta:
        model = Administrador
        fields = '__all__'
        widgets = {
            #en forma de calendario
            'fecha_nacimiento': DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-control', 'data-url': reverse_lazy('busca_municipios')})
        }
            
class FromUser(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'
        #fields = ['clave, nombre']


class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        

class FormPerfilAdministrador(forms.ModelForm):
    class Meta:
        model = Administrador
        exclude = ['usuario']
        
        widgets = {
            #en forma de calendario
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(attrs={'class':'form-control', 'data-url': reverse_lazy('busca_municipios')})
        }

class FormPerfilCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['usuario']
        
        widgets = {
            #en forma de calendario
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(attrs={'class':'form-control', 'data-url': reverse_lazy('busca_municipios')})
        }

class UserForm(forms.ModelForm):
    re_pass = forms.CharField(
        label='Confirma contraseña',
        widget=forms.PasswordInput(),
        required=True
        )
    
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(),
        required=True
        )
    class Meta:
        model = User
        fields = ['username','email','password','email','re_pass']
        #fields = '__all__'
        
    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['re_pass']:
            raise forms.ValidationError('Las contraseñas no son iguales', code='passwords_not_equals')
        return self.data['password']
    
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    