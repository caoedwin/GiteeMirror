# Generated by Django 2.1.7 on 2020-09-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_auto_20200729_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectinfoindct',
            name='CusPrjCode',
        ),
        migrations.AddField(
            model_name='projectinfoindct',
            name='PrjEngCode1',
            field=models.CharField(default='', max_length=50, verbose_name='PrjEngCode1'),
        ),
        migrations.AddField(
            model_name='projectinfoindct',
            name='PrjEngCode2',
            field=models.CharField(default='', max_length=50, verbose_name='PrjEngCode2'),
        ),
    ]
