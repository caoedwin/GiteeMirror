# Generated by Django 2.1.7 on 2020-10-19 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Issue_Notes', '0002_issue_notes_m_测试'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue_notes_m',
            name='测试',
            field=models.CharField(default='', max_length=20, verbose_name='测试'),
        ),
    ]
