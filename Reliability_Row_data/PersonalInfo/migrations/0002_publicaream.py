# Generated by Django 2.1.7 on 2021-03-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicAreaM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=50, verbose_name='Category')),
                ('XX', models.CharField(max_length=50, verbose_name='細項')),
                ('FZR', models.CharField(max_length=50, verbose_name='負責人')),
                ('CHU', models.CharField(max_length=50, verbose_name='處')),
                ('DEPARTMENT', models.CharField(default='', max_length=50, verbose_name='部別')),
                ('MAIL', models.CharField(max_length=50, verbose_name='郵件地址')),
                ('LXFS', models.CharField(max_length=50, verbose_name='聯係方式')),
            ],
        ),
    ]