# Generated by Django 2.1.7 on 2022-06-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0019_auto_20210928_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='department',
            field=models.IntegerField(choices=[(3, 'PM'), (2, '开发部门'), (1, '测试部门'), (4, '其它部门')], default=1, verbose_name='部门'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='is_SVPuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
