# Generated by Django 2.1.7 on 2021-06-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceLNV', '0009_auto_20210629_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicelnvhis',
            name='DevID',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='設備編號'),
        ),
    ]
