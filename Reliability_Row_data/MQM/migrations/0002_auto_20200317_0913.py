# Generated by Django 2.1.7 on 2020-03-17 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MQM', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mqm',
            old_name='Category',
            new_name='Name',
        ),
    ]
