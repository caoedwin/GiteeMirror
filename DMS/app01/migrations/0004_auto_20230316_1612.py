# Generated by Django 2.1.7 on 2023-03-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_remove_userinfo_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Seat',
            field=models.CharField(choices=[('KS-Plant5', 'KS-Plant5'), ('KS-Plant3', 'KS-Plant3'), ('KS-Plant2', 'KS-Plant2'), ('CQ', 'CQ'), ('CD', 'CD')], default='KS-Plant5', max_length=108),
        ),
    ]
