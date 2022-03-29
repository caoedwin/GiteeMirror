# Generated by Django 2.1.7 on 2021-09-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceABO', '0018_auto_20210901_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceabohis',
            name='Devstatus',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Devstatus'),
        ),
        migrations.AddField(
            model_name='deviceabohis',
            name='Result',
            field=models.CharField(blank=True, choices=[('Pass', 'Pass'), ('Fail', 'Fail')], max_length=16, null=True, verbose_name='Result'),
        ),
        migrations.AlterField(
            model_name='deviceabo',
            name='BrwStatus',
            field=models.CharField(blank=True, choices=[('已借出', '已借出'), ('可借用', '可借用'), ('長期借用', '長期借用'), ('預定確認', '預定確認'), ('歸還確認', '歸還確認'), ('續借確認', '續借確認')], max_length=64, null=True, verbose_name='借還狀態'),
        ),
    ]
