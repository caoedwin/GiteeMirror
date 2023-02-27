# Generated by Django 2.1.7 on 2019-09-06 03:01

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='视频内容')),
                ('single', models.CharField(blank=True, max_length=20, null=True, verbose_name='视频名称')),
            ],
        ),
        migrations.CreateModel(
            name='Imgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/test/', verbose_name='图片地址')),
                ('single', models.CharField(blank=True, max_length=20, null=True, verbose_name='图片名称')),
            ],
        ),
        migrations.CreateModel(
            name='lesson_learn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Object', models.CharField(max_length=100, unique=True)),
                ('Symptom', models.CharField(max_length=100, unique=True)),
                ('Root_Cause', DjangoUeditor.models.UEditorField(verbose_name='Root_Cause')),
                ('Solution', DjangoUeditor.models.UEditorField(verbose_name='Solution/Action')),
                ('editor', models.CharField(max_length=100)),
                ('edit_time', models.CharField(blank=True, max_length=26, verbose_name='edit_time')),
                ('Photo', models.ManyToManyField(related_name='imgs', to='app01.Imgs', verbose_name='图片表')),
                ('video', models.ManyToManyField(related_name='video', to='app01.files', verbose_name='视频表')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=True, to='app01.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Menu_title', models.CharField(max_length=32, unique=True)),
                ('url', models.CharField(max_length=128, unique=True)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=True, to='app01.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('perms', models.ManyToManyField(to='app01.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.ManyToManyField(to='app01.Role')),
            ],
            options={
                'verbose_name': 'UserInfo',
                'verbose_name_plural': 'UserInfo',
            },
        ),
    ]
