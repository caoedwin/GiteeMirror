# Generated by Django 2.1.7 on 2021-04-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdapterPowerCode', '0011_auto_20210401_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='adapterpowercodebr',
            name='OAPcode',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='掛賬人工號'),
        ),
    ]
