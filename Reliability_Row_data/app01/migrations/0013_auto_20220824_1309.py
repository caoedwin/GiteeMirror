# Generated by Django 2.1.7 on 2022-08-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_auto_20220615_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.IntegerField(choices=[(2, '开发部门'), (4, '其它部门'), (1, '测试部门'), (3, 'PM')], default=1, verbose_name='部门'),
        ),
    ]
