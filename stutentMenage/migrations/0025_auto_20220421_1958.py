# Generated by Django 3.2.7 on 2022-04-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stutentMenage', '0024_remove_courses_regularfees'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='dy',
            field=models.CharField(default='', max_length=150, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='courses',
            name='regularFees',
            field=models.CharField(default='100', max_length=5, verbose_name='regular Fess'),
        ),
    ]
