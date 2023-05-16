# Generated by Django 3.2.7 on 2022-05-11 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stutentMenage', '0045_auto_20220510_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requid', models.CharField(max_length=5, verbose_name='requid')),
                ('amount', models.CharField(max_length=50, verbose_name='Amount')),
                ('curenttime', models.DateTimeField(auto_now=True, verbose_name='time')),
                ('status', models.CharField(max_length=50, verbose_name='status')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User id')),
            ],
            options={
                'verbose_name': 'paymentrequest',
                'verbose_name_plural': 'paymentrequests',
            },
        ),
    ]