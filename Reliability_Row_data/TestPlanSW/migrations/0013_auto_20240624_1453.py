# Generated by Django 2.1.7 on 2024-06-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestPlanSW', '0012_auto_20230612_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testitemsw',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(NB)-SMB', 'C38(NB)-SMB'), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('T89(NB)', 'T89(NB)'), ('A39', 'A39'), ('C85', 'C85'), ('Others', 'Others')], default='C38(NB)', max_length=20, verbose_name='Customer'),
        ),
    ]
