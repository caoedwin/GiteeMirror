# Generated by Django 2.1.7 on 2021-02-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdapterPowerCode', '0002_auto_20210225_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adapterpowercode',
            name='Number',
            field=models.CharField(max_length=64, unique=True, verbose_name='編號'),
        ),
    ]
