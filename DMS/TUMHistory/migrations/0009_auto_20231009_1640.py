# Generated by Django 2.1.7 on 2023-10-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUMHistory', '0008_auto_20231009_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitindqa_tum',
            name='QTY',
            field=models.IntegerField(blank=True, null=True, verbose_name='QTY'),
        ),
    ]