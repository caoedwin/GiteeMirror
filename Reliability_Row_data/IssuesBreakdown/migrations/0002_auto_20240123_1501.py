# Generated by Django 2.1.7 on 2024-01-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IssuesBreakdown', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuesbreakdown',
            name='Description',
            field=models.TextField(blank=True, max_length=6000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='issuesbreakdown',
            name='Reproduce_steps',
            field=models.TextField(blank=True, max_length=6000, null=True, verbose_name='Reproduce_steps'),
        ),
    ]
