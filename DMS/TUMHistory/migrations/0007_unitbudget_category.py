# Generated by Django 2.1.7 on 2023-10-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUMHistory', '0006_auto_20231009_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitbudget',
            name='Category',
            field=models.CharField(choices=[('', ''), ('領用', '領用'), ('退還', '退還')], default='', max_length=30, verbose_name='Category'),
        ),
    ]