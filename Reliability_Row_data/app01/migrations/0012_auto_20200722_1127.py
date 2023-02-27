# Generated by Django 2.1.7 on 2020-07-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_auto_20200504_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson_learn',
            name='Category',
            field=models.CharField(choices=[('', ''), ('Reliability', 'Reliability'), ('Compatibility', 'Compatibility')], default='Reliability', max_length=100),
        ),
        migrations.AddField(
            model_name='lesson_learn',
            name='Reproduce_Steps',
            field=models.CharField(default='', max_length=1000, verbose_name='Reproduce_Steps'),
        ),
    ]
