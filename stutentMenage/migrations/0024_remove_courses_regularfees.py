# Generated by Django 3.2.7 on 2022-04-21 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stutentMenage', '0023_remove_courses_dy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='regularFees',
        ),
    ]