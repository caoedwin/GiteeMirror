# Generated by Django 2.1.7 on 2020-10-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Issue_Notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue_notes_m',
            name='测试',
            field=models.CharField(default='', max_length=20, verbose_name='ceshi'),
        ),
    ]
