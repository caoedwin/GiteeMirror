# Generated by Django 2.1.7 on 2019-10-08 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Package', '0003_auto_20191008_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_m',
            name='Pattern',
            field=models.CharField(max_length=30),
        ),
    ]
