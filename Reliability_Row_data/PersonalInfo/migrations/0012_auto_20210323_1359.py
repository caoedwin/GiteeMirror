# Generated by Django 2.1.7 on 2021-03-23 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalInfo', '0011_publicaream'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaream',
            name='DEPARTMENT',
            field=models.CharField(default='', max_length=50, verbose_name='部別'),
        ),
        migrations.AlterField(
            model_name='publicaream',
            name='CHU',
            field=models.CharField(max_length=50, verbose_name='處'),
        ),
    ]
