# Generated by Django 2.1.7 on 2023-02-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestPlanSW', '0009_auto_20210422_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ffrtbyrd',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(NB)-SMB', 'C38(NB)-SMB'), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('A39', 'A39'), ('C85', 'C85'), ('Others', 'Others')], default='C38(NB)', max_length=20, verbose_name='Customer_R'),
        ),
        migrations.AlterField(
            model_name='retestitemsw',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(NB)-SMB', 'C38(NB)-SMB'), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('A39', 'A39'), ('C85', 'C85'), ('Others', 'Others')], default='C38(NB)', max_length=20, verbose_name='Customer_R'),
        ),
        migrations.AlterField(
            model_name='testitemsw',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(NB)-SMB', 'C38(NB)-SMB'), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('A39', 'A39'), ('C85', 'C85'), ('Others', 'Others')], default='C38(NB)', max_length=20, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='testplansw',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(NB)-SMB', 'C38(NB)-SMB'), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('A39', 'A39'), ('C85', 'C85'), ('Others', 'Others')], default='C38(NB)', max_length=20, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='testplanswaio',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('Others', 'Others')], max_length=20, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='testprojectsw',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(NB)-SMB', 'C38(NB)-SMB'), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('A39', 'A39'), ('C85', 'C85'), ('Others', 'Others')], max_length=20, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='testprojectswaio',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('Others', 'Others')], max_length=20, verbose_name='Customer'),
        ),
    ]