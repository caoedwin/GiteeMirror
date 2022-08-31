# Generated by Django 2.1.7 on 2022-08-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestPlanSWOS', '0001_initial'),
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
            model_name='testprojectsw',
            name='Project',
            field=models.CharField(max_length=30, verbose_name='Project'),
        ),
        migrations.AlterField(
            model_name='testprojectswaio',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('Others', 'Others')], max_length=20, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='testprojectswaio',
            name='Project',
            field=models.CharField(max_length=30, verbose_name='Project'),
        ),
    ]