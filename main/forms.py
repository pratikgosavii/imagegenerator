from django import forms
from .models import *

from django.contrib.auth.models import User

class theme_Form(forms.ModelForm):
    
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    
    image = forms.ImageField(widget = forms.FileInput(attrs = {'class' : 'form-control' } ))
    
    
    class Meta:
        model = theme
        fields = "__all__"