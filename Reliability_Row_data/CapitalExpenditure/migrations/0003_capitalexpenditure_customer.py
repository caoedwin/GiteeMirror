# Generated by Django 2.1.7 on 2024-05-31 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CapitalExpenditure', '0002_auto_20240507_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitalexpenditure',
            name='Customer',
            field=models.CharField(default='', max_length=20, verbose_name='客戶別'),
        ),
    ]
