# Generated by Django 2.1.7 on 2022-06-15 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_auto_20220614_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertoken',
            name='account',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.IntegerField(choices=[(3, 'PM'), (2, '开发部门'), (4, '其它部门'), (1, '测试部门')], default=1, verbose_name='部门'),
        ),
        migrations.DeleteModel(
            name='UserToken',
        ),
    ]
