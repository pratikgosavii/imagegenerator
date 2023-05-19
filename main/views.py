
from django.shortcuts import render, redirect


from .forms import *







import pandas as pd
from PIL import Image, ImageDraw, ImageFont

def generate_card(data):

   
    font = ImageFont.truetype("static/OpenSans-Semibold.ttf", size=25)

    a = theme.objects.last()

    a = a.image.url
    a = a[1:]

    template = Image.open(a)
    template = template.resize((1080, 1080))
    pic = Image.open(f"photos/{data['id']}.jpg").resize((50, 50))
    template.paste(pic, (25, 75, 190, 265))
    draw = ImageDraw.Draw(template)
    draw.text((15, 350), str('Pratik Gosavi'), font=font, fill='black')

    draw.text((315, 125), data['username'], font=font, fill='black')
    return template

def admin_dashbaord(request):

    if request.method == "POST":

        forms = theme_Form(request.POST, files = request.FILES)
        print(request.POST)

        
        if forms.is_valid():

            forms.save()


                    
            records = User.objects.all().values()
            
            for record in records:
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
