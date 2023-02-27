# Generated by Django 2.1.7 on 2021-04-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestPlanME', '0004_auto_20200624_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keypartc38nb',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(NB)-SMB', 'C38(NB)-SMB'), ('C38(AIO)', 'C38(AIO)'), ('C38(AIO)-T88', 'C38(AIO)-T88'), ('A39', 'A39'), ('C85', 'C85'), ('Others', 'Others')], default='C38(NB)', max_length=20, verbose_name='Customer_R'),
        ),
        migrations.AlterField(
            model_name='testitemme',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(NB)-SMB', 'C38(NB)-SMB'), ('C38(AIO)', 'C38(AIO)'), ('A39', 'A39'), ('C85', 'C85'), ('Others', 'Others')], default='C38(NB)', max_length=20, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='testprojectme',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(NB)-SMB', 'C38(NB)-SMB'), ('C38(AIO)', 'C38(AIO)'), ('A39', 'A39'), ('C85', 'C85'), ('Others', 'Others')], max_length=20, verbose_name='Customer'),
        ),
    ]
