# Generated by Django 2.1.7 on 2021-04-01 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdapterPowerCode', '0009_auto_20210401_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adapterpowercodebr',
            name='OAP',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='掛賬人'),
        ),
    ]
