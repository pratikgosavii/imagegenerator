# Generated by Django 4.1.5 on 2023-05-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
