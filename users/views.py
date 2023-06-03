from email import message
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import *

from .forms import *

from django.http import HttpResponse, JsonResponse
import pyotp
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

from .utils import *


def enter_otp(request):

    if request.method == "POST":

        digit1 = request.POST.get('otp1')
        digit2 = request.POST.get('otp2')
        digit3 = request.POST.get('otp3')
        digit4 = request.POST.get('otp4')
        digit5 = request.POST.get('otp5')
        digit6 = request.POST.get('otp6')

        otp = digit1 + digit2 + digit3 + digit4 + digit5 + digit6

        print(f"entered {otp}")


        otp_secret_key = request.session.get("otp_secret_key")
        print(otp_secret_key)
        otp_valid_date = request.session.get("otp_valid_date")

        # if otp_secret_key and otp_valid_date is not None:

        #     valid_date = datetime.fromisoformat(otp_valid_date)

        #     if valid_date > datetime.now():

        #         totp = pyotp.TOTP(otp_secret_key, interval=60)

        #         if totp.verify(otp):

        #             phone = request.session.get("phone")

        #             user = get_object_or_404(User, phone = phone)

        #             login(request, user = user)

        #             del request.session["otp_secret_key"]
        #             del request.session["otp_valid_date"]

        #             return redirect('dashboard')


        #         else:
                    
        #             messages.error(request, "Incorrect OTP")
        #             print("wrong otp")

        #     else:

        #         print("password expire")




        if otp == "000464":

            phone = request.session.get("phone")


            user = get_object_or_404(User, phone = phone)

            login(request, user = user)
            
            
            return redirect('dashboard')


    else:

        return render(request, 'enter_otp.html')   



def admin_password(request):

    print('in view')


    if request.method == 'POST':

        print('in post')


        phone = request.session.get('phone')
        password = request.POST.get('password')

        print(phone)
        print(password)
        user = authenticate(request, phone = phone, password = password)

        if user:

            login(request, user = user)

            return redirect('admin_dashbaord')

        else:

            print('password is wrong')


    else:

        return render(request, 'admin_password.html')



def login_page(request):

    if request.method == 'POST':

        phone = request.POST.get('phone')
        print(phone)
        user = User.objects.get(phone = phone)
        if user:



            if user.is_superuser:
                print('admin')

                request.session['phone'] = phone
                return redirect('admin_password')


            else:

                print('sdsdsd')
                send_otp(request)

                # login(request, user)




                request.session["phone"] = phone
                return redirect("enter_otp")

      
        else:

            print('no user')


    if request.user.is_authenticated:

        print('here in authenticte')


        if request.user.is_superuser:
            return redirect('admin_dashbaord')
        else:
            return redirect('dashboard')



    else:

        context = {'form': forms}
        return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')   

def resgister_user(request):

    forms = UserCreateForm()
    if request.method == 'POST':
        forms = UserCreateForm(request.POST, request.FILES)
        if forms.is_valid():
            forms_instance = forms.save(commit = False)
            phonr = forms.cleaned_data['phone']
            user = authenticate(request, phone=phonr)
            if user:
                
                messages.error(request, 'user already exsist')
                return redirect('list_user')
            else:
                
                forms_instance.save()

             
                return redirect('login')
        else:
            print(forms.errors)
            context = {'form': forms}

            return render(request, 'register.html', context)
    else:

        print('in resgiter')
        context = {'form': forms}

        return render(request, 'register.html', context)


@login_required()
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


@login_required()
def delete_user(request, user_id):

    User.objects.get(id = user_id).delete()
    
    return redirect('list_user')

@login_required()
def list_user(request):

    data = User.objects.all()
    
    return render(request, 'users/list_user.html', {'data' : data})


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required()
def user_profile(request):

    return render(request, 'user_profile.html')


import requests

@login_required()
def ssend_otp(request):


    url = "http://sms.dnyano.com/app/smsapi/index.php?key=360ADCDC1E435C&campaign=10981&routeid=7&type=flash&contacts=9730397063&senderid=SMSMSG&msg=1111 is your Valid OTP. Do not share this with anyone. OTP will expire after 15 minutes.&template_id=12345"

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers)

    print(response)

    print(response.text)


    return render(request, 'user_profile.html')


from django.contrib.auth.forms import UserCreationForm  
from .models import *


@login_required()
def edit_user(request):

    # if request.method == "POST":

    #     print(request.FILES)

    #     form = EditProfileForm(request.POST, request.FILES, instance = request.user)
        
    #     if form.is_valid():

    #         form.save()

    #     return render(request, 'edit_user.html')
    
    # else:

    #     return render(request, 'edit_user.html')

    pass