# Generated by Django 2.1.7 on 2021-12-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoResult', '0006_auto_20211210_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoresult',
            name='Status',
            field=models.CharField(choices=[('V', 'V'), ('X', 'X')], default='', max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='autoitems',
            name='Owner',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='autoitems',
            name='Status',
            field=models.CharField(choices=[('V', 'V'), ('X', 'X')], default='', max_length=50, verbose_name='Status'),
        ),
    ]
