# Generated by Django 4.1.5 on 2023-06-03 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='Rto raod', max_length=50),
            preserve_default=False,
        ),
    ]