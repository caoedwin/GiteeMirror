# Generated by Django 2.1.7 on 2021-03-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_userinfo_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='Seat',
            field=models.CharField(default='', max_length=108),
        ),
        migrations.AlterField(
            model_name='imgs',
            name='img',
            field=models.ImageField(upload_to='img/UserInfo/', verbose_name='图片地址'),
        ),
    ]
