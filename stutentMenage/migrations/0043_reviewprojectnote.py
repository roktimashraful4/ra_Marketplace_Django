# Generated by Django 3.2.7 on 2022-05-09 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stutentMenage', '0042_bituploadproject_uploaddate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviewprojectnote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess', models.TextField(verbose_name='Message')),
                ('bittaskid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stutentMenage.bittask', verbose_name='Bit Task')),
            ],
            options={
                'verbose_name': 'Reviewprojectnote',
                'verbose_name_plural': 'Reviewprojectnotes',
            },
        ),
    ]
