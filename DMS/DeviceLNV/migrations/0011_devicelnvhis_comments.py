# Generated by Django 2.1.7 on 2021-08-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceLNV', '0010_auto_20210629_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicelnvhis',
            name='Comments',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments'),
        ),
    ]
