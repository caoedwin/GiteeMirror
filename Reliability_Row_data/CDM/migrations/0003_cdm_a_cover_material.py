# Generated by Django 2.1.7 on 2019-10-25 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CDM', '0002_auto_20191015_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdm',
            name='A_cover_Material',
            field=models.CharField(default='', max_length=50),
        ),
    ]
