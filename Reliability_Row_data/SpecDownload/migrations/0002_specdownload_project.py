# Generated by Django 2.1.7 on 2023-02-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpecDownload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specdownload',
            name='Project',
            field=models.CharField(default='', max_length=20, verbose_name='Project'),
        ),
    ]
