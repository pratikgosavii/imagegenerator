from django import forms
from .models import *
from django.forms import ModelForm

class user_details_Form(forms.ModelForm):
    
    avatar = forms.ImageField(widget = forms.FileInput(attrs = {'class' : 'form-control' } ))


    class Meta:
        model = user_details
        fields = "__all__"

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
                 'email',
                 'first_name',
                )
        
from django.contrib.auth.forms import UserCreationForm
        
class registerForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1']