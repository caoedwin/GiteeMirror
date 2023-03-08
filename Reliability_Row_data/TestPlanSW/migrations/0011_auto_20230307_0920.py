# Generated by Django 2.1.7 on 2023-03-07 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestPlanSW', '0010_auto_20230224_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testplanswaio',
            name='Phase',
            field=models.CharField(choices=[('', ''), ('B(SDV)', 'B(SDV)'), ('C(SIT)', 'C(SIT)'), ('Wave2', 'Wave2'), ('Wave3', 'Wave3'), ('EELP+', 'EELP+'), ('OOC', 'OOC'), ('OOC2', 'OOC2'), ('OOC3', 'OOC3'), ('Others', 'Others')], default='', max_length=20, verbose_name='Phase'),
        ),
        migrations.AlterField(
            model_name='testprojectswaio',
            name='Phase',
            field=models.CharField(choices=[('', ''), ('B(SDV)', 'B(SDV)'), ('C(SIT)', 'C(SIT)'), ('Wave2', 'Wave2'), ('Wave3', 'Wave3'), ('EELP+', 'EELP+'), ('OOC', 'OOC'), ('OOC2', 'OOC2'), ('OOC3', 'OOC3'), ('Others', 'Others')], max_length=20, verbose_name='Phase'),
        ),
    ]
