# Generated by Django 2.1.7 on 2020-06-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MQM', '0003_auto_20200317_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mqm',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('A39', 'A39'), ('Others', 'Others')], default='', max_length=10, verbose_name='Customer'),
        ),
    ]
