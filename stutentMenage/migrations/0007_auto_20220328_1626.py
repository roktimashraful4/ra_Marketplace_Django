# Generated by Django 3.2.7 on 2022-03-28 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stutentMenage', '0006_auto_20220328_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='secoundpaydate',
            field=models.DateTimeField(verbose_name='secounddate'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='thirdpaydate',
            field=models.DateTimeField(verbose_name='thirddate'),
        ),
    ]
