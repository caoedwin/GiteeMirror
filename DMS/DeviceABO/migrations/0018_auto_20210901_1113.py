# Generated by Django 2.1.7 on 2021-09-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceABO', '0017_auto_20210901_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceabo',
            name='Source',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='設備來源'),
        ),
    ]
