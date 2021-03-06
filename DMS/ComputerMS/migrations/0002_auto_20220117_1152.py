# Generated by Django 2.1.7 on 2022-01-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComputerMS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computerlnvhis',
            name='Area',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='地區'),
        ),
        migrations.AddField(
            model_name='computerlnvhis',
            name='Plant',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='廠區'),
        ),
        migrations.AddField(
            model_name='computerlnvhis',
            name='Purpose',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='電腦用途'),
        ),
    ]
