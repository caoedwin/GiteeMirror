# Generated by Django 2.1.7 on 2020-12-23 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LessonProjectME', '0003_auto_20201013_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testprojectll',
            name='Customer',
            field=models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(NB)-SMB', 'C38(NB)-SMB'), ('C38(AIO)', 'C38(AIO)'), ('T88(AIO)', 'T88(AIO)'), ('A39', 'A39'), ('Others', 'Others')], max_length=20, verbose_name='Customer'),
        ),
    ]
