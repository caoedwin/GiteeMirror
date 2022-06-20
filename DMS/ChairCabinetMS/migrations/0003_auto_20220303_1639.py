# Generated by Django 2.1.7 on 2022-03-03 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChairCabinetMS', '0002_auto_20220223_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaircabinetlnv',
            name='BrwStatus',
            field=models.CharField(blank=True, choices=[('使用中', '使用中'), ('申請中', '申請中'), ('歸還中', '歸還中'), ('轉帳中', '轉帳中'), ('接收中', '接收中'), ('閑置中', '閑置中'), ('已損壞', '已損壞'), ('申請確認中', '申請確認中'), ('歸還確認中', '歸還確認中'), ('轉帳確認中', '轉帳確認中')], max_length=64, null=True, verbose_name='使用狀態'),
        ),
    ]
