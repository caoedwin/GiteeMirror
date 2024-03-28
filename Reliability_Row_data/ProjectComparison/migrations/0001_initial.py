# Generated by Django 2.1.7 on 2024-03-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(max_length=12, verbose_name='Year')),
                ('DataType', models.CharField(max_length=12, verbose_name='DataType')),
                ('CG', models.CharField(max_length=20, verbose_name='CG')),
                ('Compal_Model', models.CharField(max_length=8, verbose_name='Compal Model')),
                ('Customer_Model', models.CharField(max_length=50, verbose_name='Customer Model')),
                ('Marketing_type', models.CharField(max_length=50, verbose_name='Marketing type\n(Commercial / Consumer)')),
                ('Status', models.CharField(max_length=10, verbose_name='Status:\nPlanning  =P\nExecuting=E')),
                ('Customer', models.CharField(max_length=10, verbose_name='Customer')),
                ('Product_Type', models.CharField(max_length=20, verbose_name='Product Type\n(NB/PAD/AIO/IPC)')),
                ('Jan', models.CharField(blank=True, max_length=50, null=True, verbose_name='Jan')),
                ('Feb', models.CharField(blank=True, max_length=50, null=True, verbose_name='Feb')),
                ('Mar', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mar')),
                ('Apr', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apr')),
                ('May', models.CharField(blank=True, max_length=50, null=True, verbose_name='May')),
                ('Jun', models.CharField(blank=True, max_length=50, null=True, verbose_name='Jun')),
                ('Jul', models.CharField(blank=True, max_length=50, null=True, verbose_name='Jul')),
                ('Aug', models.CharField(blank=True, max_length=50, null=True, verbose_name='Aug')),
                ('Sep', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sep')),
                ('Oct', models.CharField(blank=True, max_length=50, null=True, verbose_name='Oct')),
                ('Nov', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nov')),
                ('Dec', models.CharField(blank=True, max_length=50, null=True, verbose_name='Dec')),
            ],
            options={
                'verbose_name': 'ProjectPlan',
                'verbose_name_plural': 'ProjectPlan',
            },
        ),
    ]