# Generated by Django 2.1.7 on 2021-12-03 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoResult', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoitems',
            name='Owner',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='autoresult',
            name='Owner',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='autoresult',
            name='ProjectName',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='ProjectName'),
        ),
        migrations.AddField(
            model_name='autoresult',
            name='Year',
            field=models.CharField(default='', max_length=20, verbose_name='SS年份'),
        ),
        migrations.AlterField(
            model_name='autoproject',
            name='Year',
            field=models.CharField(default='', max_length=20, verbose_name='SS年份'),
        ),
    ]
