# Generated by Django 2.1.7 on 2020-12-23 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INVGantt', '0003_invgantt_unit_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invgantt',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('A39', 'A39'), ('Others', 'Others')], max_length=100, verbose_name='Customer'),
        ),
    ]