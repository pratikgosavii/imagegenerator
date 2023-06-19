
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .forms import *

from django.contrib.auth.decorators import login_required



from django.contrib.auth.decorators import user_passes_test

import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from PIL import Image, ImageDraw



from django.contrib.auth import get_user_model
User = get_user_model()

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 3, rad * 3)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

    

def generate_card(data):

   
    font = ImageFont.truetype("static/OpenSans-Semibold.ttf", size=32)
    font1 = ImageFont.truetype("static/OpenSans-Semibold.ttf", size=20)

    

    template = Image.open('static/theme/theme_demo1.jpg')
    template = template.resize((1080, 1080))

    a = theme.objects.last()

    a = a.image.url
    a = a[1:]

    im2 = Image.open(a).resize((968, 944)) 
    template.paste(im2, (47, 59, 1015, 1003))


    b = str(data.avatar)

    im = Image.open(b)
    im.save('username.png')

    b = 'username.png'

    pic = Image.open(b).convert("RGB")

    npImage=np.array(pic)
    h,w=pic.size

    # Create same size alpha layer with circle
    alpha = Image.new('L', pic.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)

    # Convert alpha Image to numpy array
    npAlpha=np.array(alpha)

    # Add alpha layer to RGB
    npImage=np.dstack((npImage,npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save(b)

    pic = Image.open(b).resize((234, 237))

   
    template.paste(pic, (6, 839, 240, 1076), pic)
    draw = ImageDraw.Draw(template)
    
    
    im2 = Image.open('static/images/caller_icon.png').resize((42, 34)) 
    template.paste(im2, (717,925, 759, 959))

    im2 = Image.open('static/images/location_icon.png').resize((23, 24)) 
    template.paste(im2, (241, 988, 264, 1012), im2)

   
    draw.text((278, 985), str(data.address), font=font1, fill='black')

    
    # draw.rectangle((10, 345), fill="black")
    position = (295, 920)

    left, top, right, bottom = draw.textbbox((position), str(data.first_name), font=font)
    draw.rectangle((left-55, top-15, right+0, bottom+15), fill="blue")
    draw.text((265, 920), str(data.first_name), font=font, fill='white', stroke_width=1)
    draw.text((780, 920), str(data.phone), font=font, fill='blue', stroke_width=1)

   
    
    return template



@user_passes_test(lambda u: u.is_superuser)
def admin_dashbaord(request):

    if request.method == "POST":

        forms = theme_Form(request.POST, files = request.FILES)
        print(request.POST)

        
        if forms.is_valid():

            forms.save()


                    
            records = User.objects.all()
            
            for record in records:
                card = generate_card(record)
                card.save(f"static/generated_cards/{record.phone}.jpg")
                


            return redirect('admin_dashbaord')

        else:
            print('----------------------')
            print(forms.errors)

    else:

        context = {
            'form' : theme_Form()
        }

        return render(request, 'admin_dashboard.html', context)


@login_required()
def dashbaord(request):

    festival_data = theme.objects.filter(category = 'festival')
    birthday_data = theme.objects.filter(category = 'happy birthday')



    print('-------------------')
    print('-------------------')
    print('-------------------')
    print('-------------------')
    print(festival_data)
    print(birthday_data)

    context = {
        'festival_data' : festival_data,
        'birthday_data' : birthday_data
    }

    return render(request, 'bottom_menu.html', context)


@login_required()
def all_generate_card(request):

    data = User.objects.all()

    return render(request, 'admin_list_all_images.html', { 'data' : data})





def downlaod_image(request, image_path):

    image_path = "static/generated_cards/" + image_path + ".jpg"

    file = open(image_path, "rb").read()
    rea_response = HttpResponse(file, content_type='image/jpeg')
    rea_response['Content-Disposition'] = 'attachment; filename={}'.format('name.jpg')
    return rea_response





def theme_details(request, theme_id):

    theme_instance = theme.objects.get(id = theme_id)

    # session.

    context = {

        'theme_instance' : theme_instance
    }

    return render(request, 'theme_details.html', context)


def select_frame(request):



    return render(request, 'select_frame.html')