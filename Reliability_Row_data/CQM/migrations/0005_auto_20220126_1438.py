# Generated by Django 2.1.7 on 2022-01-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CQM', '0004_auto_20220104_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cqm',
            name='Comments',
            field=models.CharField(blank=True, max_length=9000, null=True, verbose_name='Comments'),
        ),
    ]
