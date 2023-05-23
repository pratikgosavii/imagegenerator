
from django.shortcuts import render, redirect


from .forms import *







import pandas as pd
from PIL import Image, ImageDraw, ImageFont

def generate_card(request):

   
    font = ImageFont.truetype("static/OpenSans-Semibold.ttf", size=25)

    a = theme.objects.last()

    a = a.image.url
    a = a[1:]

    template = Image.open('static/theme/theme_demo1.jpg')
    template = template.resize((1080, 1080))
    pic = Image.open(f"photos/1.jpg").resize((210, 213))
    template.paste(pic, (14, 847, 224, 1060))
    draw = ImageDraw.Draw(template)
    # draw.text((15, 350), str('Pratik Gosavi'), font=font, fill='black')

    # draw.text((315, 125), data['username'], font=font, fill='black')

    return template

def admin_dashbaord(request):

    if request.method == "POST":

        forms = theme_Form(request.POST, files = request.FILES)
        print(request.POST)

        
        if forms.is_valid():

            forms.save()


                    
            records = User.objects.all().values()
            print('---------------------------------records---------------------------')
            print(records)
            print('---------------------------------records---------------------------')
            
            for record in records:
                print('--------------------------------')
                card = generate_card(record)
                card.save(f"cards/{record['id']}.jpg")



            return redirect('admin_dashbaord')

        else:
            print('----------------------')
            print(forms.errors)

    else:

        context = {
            'form' : theme_Form()
        }

        return render(request, 'admin_dashboard.html', context)

def dashbaord(request):

    return render(request, 'dashbaord.html')
