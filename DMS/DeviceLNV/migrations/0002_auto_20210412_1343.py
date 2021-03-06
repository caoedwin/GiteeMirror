# Generated by Django 2.1.7 on 2021-04-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceLNV', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PICS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='DeviceLNV/PIC/', verbose_name='图片地址')),
                ('single', models.CharField(blank=True, max_length=200, null=True, verbose_name='图片名称')),
            ],
        ),
        migrations.RemoveField(
            model_name='devicelnv',
            name='Application',
        ),
        migrations.AlterField(
            model_name='devicelnv',
            name='addnewdate',
            field=models.DateField(blank=True, max_length=64, null=True, verbose_name='設備添加日期'),
        ),
        migrations.DeleteModel(
            name='ApplicationNofile',
        ),
        migrations.AddField(
            model_name='devicelnv',
            name='Photo',
            field=models.ManyToManyField(blank=True, related_name='pics', to='DeviceLNV.PICS', verbose_name='图片表'),
        ),
    ]
