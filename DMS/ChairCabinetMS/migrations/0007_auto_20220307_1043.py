# Generated by Django 2.1.7 on 2022-03-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChairCabinetMS', '0006_chaircabinetlnvhis_brwstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaircabinetlnv',
            name='BrwStatus',
            field=models.CharField(blank=True, choices=[('使用中', '使用中'), ('轉帳中', '轉帳中'), ('閑置中', '閑置中'), ('已損壞', '已損壞'), ('維修中', '維修中'), ('申請中', '申請中'), ('轉帳中', '轉帳中'), ('申請確認中', '申請確認中'), ('接收中', '接收中'), ('申請核准中', '申請核准中'), ('接收核准中', '接收核准中')], max_length=64, null=True, verbose_name='使用狀態'),
        ),
    ]
