# Generated by Django 4.1.5 on 2023-05-17 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='static/user'),
        ),
    ]