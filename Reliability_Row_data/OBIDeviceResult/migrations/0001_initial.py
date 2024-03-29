# Generated by Django 2.1.7 on 2021-12-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100, unique=True, verbose_name='Category')),
                ('editor', models.CharField(max_length=100, verbose_name='editor')),
                ('edit_time', models.CharField(max_length=26, verbose_name='edit_time')),
            ],
            options={
                'verbose_name': 'CategoryInfo',
                'verbose_name_plural': 'CategoryInfo',
            },
        ),
        migrations.CreateModel(
            name='OBIDeviceResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(NB)-SMB', 'C38(NB)-SMB'), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('A39', 'A39'), ('C85', 'C85'), ('Others', 'Others')], max_length=100, verbose_name='Customer')),
                ('Project', models.CharField(max_length=100, verbose_name='Project')),
                ('Platform', models.CharField(max_length=100, verbose_name='Platform')),
                ('Series', models.CharField(max_length=100, verbose_name='Series')),
                ('Category', models.CharField(max_length=100, verbose_name='Category')),
                ('DeviceNo', models.CharField(max_length=100, verbose_name='DeviceNo')),
                ('PN', models.CharField(max_length=100, verbose_name='PN')),
                ('Devicename', models.CharField(max_length=1000, verbose_name='Devicename')),
                ('Testresult', models.CharField(choices=[('', ''), ('Qd', 'Qd'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C')], max_length=10, verbose_name='Testresult')),
                ('FWversion', models.CharField(blank=True, max_length=100, null=True, verbose_name='FWversion')),
                ('Softwareversion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Softwareversion')),
                ('HWIDversion', models.CharField(blank=True, max_length=100, null=True, verbose_name='HWIDversion')),
                ('TestPhase', models.CharField(max_length=100, verbose_name='TestPhase')),
                ('Comments', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Comments')),
                ('editor', models.CharField(max_length=100, verbose_name='editor')),
                ('edit_time', models.CharField(max_length=26, verbose_name='edit_time')),
            ],
            options={
                'verbose_name': 'OBIDeviceResult',
                'verbose_name_plural': 'OBIDeviceResult',
            },
        ),
        migrations.CreateModel(
            name='SeriesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Series', models.CharField(max_length=100, unique=True, verbose_name='Series')),
                ('editor', models.CharField(max_length=100, verbose_name='editor')),
                ('edit_time', models.CharField(max_length=26, verbose_name='edit_time')),
            ],
            options={
                'verbose_name': 'SeriesInfo',
                'verbose_name_plural': 'SeriesInfo',
            },
        ),
    ]
