# Generated by Django 2.1.7 on 2023-02-27 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_userinfo_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='Customer',
        ),
    ]