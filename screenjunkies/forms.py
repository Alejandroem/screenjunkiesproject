__author__ = 'debian'

from django import forms
from django.forms import ModelForm
from screenjunkies.models import *

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=256)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
class VinculoForm(forms.ModelForm):
    class Meta:
        model = Vinculo
        fields = '__all__'