# Generated by Django 2.1.7 on 2019-10-15 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190910_0853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menu'},
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'verbose_name': 'Permission', 'verbose_name_plural': 'Permission'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'Role', 'verbose_name_plural': 'Role'},
        ),
    ]
