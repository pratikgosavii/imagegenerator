from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import *



def login_page(request):
    forms = LoginForm()

    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            if user:

                if user.is_superuser:
                    print('admin')
                    login(request, user)

                    return redirect('admin_dashbaord')

                else:
                    print('not admin')

                    login(request, user)
                    return redirect('dashboard')
            else:
                print('error')
                messages.error(request, 'Incorrect Username Password')
        else:

            print(forms.errors)
    context = {'form': forms}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')   

def resgister_user(request):

    forms = registerForm()
    if request.method == 'POST':
        forms = registerForm(request.POST)
        if forms.is_valid():
            forms_instance = forms.save(commit = False)
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user:
                
                messages.error(request, 'user already exsist')
                return redirect('list_user')
            else:
                
                forms_instance.save()

                user_instance = User.objects.get(username = username)

                updated_request = request.POST.copy()
                updated_request.update({'user': user_instance})
                form2 = user_details_Form(updated_request, request.FILES)

                if form2.is_valid():
                    form2.save()
                else:
                    print(form2.errors)

                return redirect('login')
        else:
            print(forms.errors)
            context = {'form': forms}

            return render(request, 'login.html', context)
    else:
        context = {'form': forms}

        return render(request, 'login.html', context)


def update_user(request, user_id):

    instance = User.objects.get(id = user_id)

    password = request.POST.get('password1')
    

    if not password:

        password = instance.password_r


    forms = registerForm(instance = instance)
    if request.method == 'POST':


        print(request.POST)
        updated_request = request.POST.copy()
        updated_request.update({'password1': password})
        forms = registerForm(updated_request, files = request.FILES, instance = instance)
        if forms.is_valid():
            forms_instance = forms.save(commit = False)
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password1']
            user = authenticate(username=username)
            if user:

                messages.error(request, 'user already exsist')
                return redirect('list_use   r')
            else:

                forms_instance.password_r = password
                forms_instance.save()

                return redirect('list_user')
        else:
            context = {'form': forms}

            return render(request, 'users/update_user.html', context)

    else:
        context = {'form': forms}

        return render(request, 'users/update_user.html', context)


def delete_user(request, user_id):

    User.objects.get(id = user_id).delete()
    
    return redirect('list_user')

def list_user(request):

    data = User.objects.all()
    
    return render(request, 'users/list_user.html', {'data' : data})

def logout_page(request):
    logout(request)
    return redirect('login')



def user_profile(request):

    return render(request, 'user_profile.html')


from django.contrib.auth.forms import UserCreationForm  
from .models import *


def edit_user(request):

    if request.method == "POST":

        print(request.FILES)

        form = EditProfileForm(request.POST, instance = request.user)
        
        if form.is_valid():

            form.save()

        user_details_instance = user_details.objects.get(user = request.user)
        
        updated_request = request.POST.copy()
        updated_request.update({'user': request.user})
        form2 = user_details_Form(updated_request, request.FILES, instance = user_details_instance)

        if form2.is_valid():
            form2.save()
        else:
            print(form2.errors)


        return render(request, 'edit_user.html')
    
    else:

        return render(request, 'edit_user.html')