# Generated by Django 2.1.7 on 2023-01-31 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MQM', '0006_auto_20230131_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mqm',
            name='Name',
            field=models.CharField(max_length=300, verbose_name='Name'),
        ),
    ]