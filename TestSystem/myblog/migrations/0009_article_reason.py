# Generated by Django 2.1.7 on 2021-01-27 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_user_canedit'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='reason',
            field=models.CharField(default='', max_length=200, verbose_name='理由'),
            preserve_default=False,
        ),
    ]
