# Generated by Django 3.2.7 on 2022-05-05 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stutentMenage', '0038_auto_20220502_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addtask',
            name='exptime',
        ),
    ]