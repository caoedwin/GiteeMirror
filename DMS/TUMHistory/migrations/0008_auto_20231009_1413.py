# Generated by Django 2.1.7 on 2023-10-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUMHistory', '0007_unitbudget_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitbudget',
            name='Apr',
            field=models.IntegerField(blank=True, null=True, verbose_name='Apr'),
        ),
        migrations.AlterField(
            model_name='unitbudget',
            name='Aug',
            field=models.IntegerField(blank=True, null=True, verbose_name='Aug'),
        ),
        migrations.AlterField(
            model_name='unitbudget',
            name='Dec',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dec'),
        ),
        migrations.AlterField(
            model_name='unitbudget',
            name='Feb',
            field=models.IntegerField(blank=True, null=True, verbose_name='Feb'),
        ),
        migrations.AlterField(
            model_name='unitbudget',
            name='Jan',
            field=models.IntegerField(blank=True, null=True, verbose_name='Jan'),
        ),
        migrations.AlterField(
            model_name='unitbudget',
            name='Jul',
            field=models.IntegerField(blank=True, null=True, verbose_name='Jul'),
        ),
        migrations.AlterField(
            model_name='unitbudget',
            name='Jun',
            field=models.IntegerField(blank=True, null=True, verbose_name='Jun'),
        ),
        migrations.AlterField(
            model_name='unitbudget',
            name='Mar',
            field=models.IntegerField(blank=True, null=True, verbose_name='Mar'),
        ),
        migrations.AlterField(
            model_name='unitbudget',
            name='May',
            field=models.IntegerField(blank=True, null=True, verbose_name='May'),
        ),
        migrations.AlterField(
            model_name='unitbudget',
            name='Nov',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nov'),
        ),
        migrations.AlterField(
            model_name='unitbudget',
            name='Oct',
            field=models.IntegerField(blank=True, null=True, verbose_name='Oct'),
        ),
        migrations.AlterField(
            model_name='unitbudget',
            name='Sep',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sep'),
        ),
    ]
