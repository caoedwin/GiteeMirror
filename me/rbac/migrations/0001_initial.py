# Generated by Django 2.1.7 on 2021-06-01 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item_Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cus_I', models.CharField(default='', max_length=32, verbose_name='Cus_I')),
                ('Item_I', models.CharField(default='', max_length=200, unique=True, verbose_name='Item_I')),
                ('Category', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Catgory')),
                ('Item_Description', models.CharField(default='', max_length=200, verbose_name='Item_Description')),
                ('Sample_Demand', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Sample_Demand')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('url', models.CharField(default='', max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cus_P', models.CharField(default='', max_length=32, verbose_name='Cus_P')),
                ('Project_P', models.CharField(default='', max_length=32, verbose_name='Project_P')),
                ('Phase_P', models.CharField(default='', max_length=20, verbose_name='Phase_P')),
                ('Item_P', models.ManyToManyField(to='rbac.Item_Spec')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('permissions', models.ManyToManyField(to='rbac.Permission')),
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
                ('perm', models.ManyToManyField(blank=True, to='rbac.Permission')),
                ('roles', models.ManyToManyField(blank=True, to='rbac.Role')),
            ],
            options={
                'verbose_name': 'UserInfo',
                'verbose_name_plural': 'UserInfo',
            },
        ),
        migrations.AddField(
            model_name='project_spec',
            name='Owner_P',
            field=models.ManyToManyField(to='rbac.UserInfo'),
        ),
        migrations.AddField(
            model_name='permission',
            name='Proj_perm',
            field=models.ManyToManyField(to='rbac.Project_Spec'),
        ),
        migrations.AddField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.Menu'),
        ),
    ]
