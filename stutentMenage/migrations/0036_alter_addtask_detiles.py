# Generated by Django 3.2.7 on 2022-05-02 15:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stutentMenage', '0035_alter_addtask_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtask',
            name='detiles',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]