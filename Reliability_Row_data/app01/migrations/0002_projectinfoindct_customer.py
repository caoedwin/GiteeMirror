# Generated by Django 2.1.7 on 2020-12-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfoindct',
            name='Customer',
            field=models.CharField(default='', max_length=10, verbose_name='Customer'),
        ),
    ]
