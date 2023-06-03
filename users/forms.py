from django import forms
from .models import *
from django.forms import ModelForm

# class user_details_Form(forms.ModelForm):
    
#     avatar = forms.ImageField(widget = forms.FileInput(attrs = {'class' : 'form-control' } ))


#     class Meta:
#         model = user_details
#         fields = "__all__"

# from django import forms




from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

from django.core.validators import FileExtensionValidator


class UserCreateForm(UserCreationForm):

    
    password1 = forms.CharField(label=("Password"), required=False,
                            widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"),
                            widget=forms.PasswordInput, required=False)

    avatar = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/png'}))



    class Meta:
        model = User
        fields = ("phone", "avatar", "first_name", "email")

   
    def save(self, commit=True): 
        user = super(UserCreateForm, self).save(commit=False) 
        clean_email = self.cleaned_data["phone"] 
        clean_password = self.data.get("password") 

        user.phone= clean_email 
        if clean_password:
            user.set_password(password)

        if commit:

            user.save()

        custom_user = User()

        custom_user = user 
        
        custom_user.save()

        return user

      