# Generated by Django 2.1.7 on 2024-03-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ABOProjectLessonL', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABOQIL_M',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(max_length=100, verbose_name='Product')),
                ('Customer', models.CharField(choices=[('', ''), ('T88(NB)', 'T88(NB)'), ('ABO', 'ABO'), ('Others', 'Others')], max_length=20, verbose_name='Customer')),
                ('ABOQIL_No', models.CharField(max_length=100, unique=True, verbose_name='ABOQIL_No')),
                ('Issue_Description', models.CharField(max_length=3000, verbose_name='Issue_Description')),
                ('Root_Cause', models.CharField(max_length=3000, verbose_name='Root_Cause')),
                ('Status', models.CharField(choices=[('', ''), ('Closed', 'Closed'), ('Deleted', 'Deleted'), ('In Process', 'In Process'), ('Lesson Learn', 'Lesson Learn'), ('Open', 'Open')], max_length=100, verbose_name='Status')),
                ('Creator', models.CharField(default='', max_length=100)),
                ('Created_On', models.CharField(default='', max_length=26, verbose_name='Created_On')),
                ('editor', models.CharField(max_length=100)),
                ('edit_time', models.CharField(blank=True, max_length=26, verbose_name='edit_time')),
            ],
            options={
                'verbose_name': 'ABOQIL_M',
                'verbose_name_plural': 'ABOQIL_M',
            },
        ),
        migrations.CreateModel(
            name='ABOQIL_Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('', ''), ('Pass', 'Pass'), ('Fail', 'Fail'), ('N/S', 'N/S'), ('N/A', 'N/A')], max_length=20)),
                ('Comment', models.CharField(max_length=1000)),
                ('editor', models.CharField(default='', max_length=100)),
                ('edit_time', models.CharField(blank=True, default='', max_length=26, verbose_name='edit_time')),
                ('ABOQIL', models.ForeignKey(on_delete=True, to='ABOQIL.ABOQIL_M')),
                ('Projectinfo', models.ForeignKey(on_delete=True, to='ABOProjectLessonL.ABOTestProjectLL')),
            ],
        ),
        migrations.CreateModel(
            name='files_ABOQIL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='files_aboqil/', verbose_name='文件内容')),
                ('single', models.CharField(blank=True, max_length=100, null=True, verbose_name='文件名称')),
            ],
        ),
        migrations.AddField(
            model_name='aboqil_m',
            name='files_ABOQIL',
            field=models.ManyToManyField(blank=True, related_name='files_ABOQIL', to='ABOQIL.files_ABOQIL', verbose_name='图文件表'),
        ),
    ]