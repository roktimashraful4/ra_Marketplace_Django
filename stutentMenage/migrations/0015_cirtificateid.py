# Generated by Django 3.2.7 on 2022-03-31 19:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stutentMenage', '0014_auto_20220328_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='CirtificateId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catificateId', models.CharField(blank=True, default=uuid.uuid4, max_length=10, verbose_name='key')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stutentMenage.student', verbose_name='studentID')),
            ],
            options={
                'verbose_name': 'CirtificateId',
                'verbose_name_plural': 'CirtificateIds',
            },
        ),
    ]
