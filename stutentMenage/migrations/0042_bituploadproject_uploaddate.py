# Generated by Django 3.2.7 on 2022-05-09 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stutentMenage', '0041_bituploadproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='bituploadproject',
            name='uploaddate',
            field=models.DateTimeField(auto_now=True, verbose_name='curentdate'),
        ),
    ]
