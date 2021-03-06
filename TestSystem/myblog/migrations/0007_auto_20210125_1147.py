# Generated by Django 2.1.7 on 2021-01-25 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_remove_article_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': '状态',
                'verbose_name_plural': '状态',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='myblog.Status', verbose_name='状态'),
        ),
    ]
