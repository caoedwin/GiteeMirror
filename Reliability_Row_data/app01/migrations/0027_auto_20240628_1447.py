# Generated by Django 2.1.7 on 2024-06-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0026_auto_20240528_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.IntegerField(choices=[(1, '测试部门'), (2, '开发部门'), (3, 'PM'), (4, '其它部门')], default=1, verbose_name='部门'),
        ),
    ]
