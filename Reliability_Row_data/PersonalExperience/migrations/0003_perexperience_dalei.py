# Generated by Django 2.1.7 on 2023-08-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalExperience', '0002_auto_20230817_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='perexperience',
            name='Dalei',
            field=models.CharField(blank=True, choices=[('', ''), ('NPI', 'NPI'), ('OSR', 'OSR'), ('INV', 'INV')], max_length=20, null=True, verbose_name='大类'),
        ),
    ]
