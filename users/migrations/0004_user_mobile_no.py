# Generated by Django 4.1.5 on 2023-05-17 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
