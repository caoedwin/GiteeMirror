# Generated by Django 2.1.7 on 2021-08-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceABO', '0010_auto_20210818_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceabo',
            name='Last_Phase',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='最近一次借Phase'),
        ),
        migrations.AddField(
            model_name='deviceabo',
            name='Last_ProjectCode',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='最近一次借機種'),
        ),
    ]
