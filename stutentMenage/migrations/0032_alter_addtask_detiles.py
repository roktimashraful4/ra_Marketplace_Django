# Generated by Django 3.2.7 on 2022-05-01 07:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stutentMenage', '0031_auto_20220501_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtask',
            name='detiles',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
