# Generated by Django 3.2.7 on 2022-04-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stutentMenage', '0028_auto_20220430_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcetagory',
            name='shortdis',
            field=models.TextField(verbose_name='Short Discriptions'),
        ),
    ]
