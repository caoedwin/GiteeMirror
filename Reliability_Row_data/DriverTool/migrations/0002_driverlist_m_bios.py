# Generated by Django 2.1.7 on 2020-12-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriverTool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverlist_m',
            name='BIOS',
            field=models.CharField(default='', max_length=150),
        ),
    ]
