# Generated by Django 2.1.7 on 2020-03-04 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MQM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(AIO)', 'C38(AIO)'), ('A39', 'A39'), ('Others', 'Others')], default='', max_length=10, verbose_name='Customer')),
                ('Project', models.CharField(max_length=20, verbose_name='Project')),
                ('Category', models.CharField(max_length=300, verbose_name='Catefory')),
                ('Vendor', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Vender')),
                ('SourcePriority', models.CharField(max_length=10, verbose_name='SourcePriority')),
                ('CompalPN', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='CompalPN')),
                ('VendorPN', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='VendorPN')),
                ('Status', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Status')),
                ('Description', models.CharField(default='', max_length=500, verbose_name='Description')),
                ('Qty', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Qty')),
                ('Location', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Location')),
                ('B_DQA_DataCode', models.CharField(blank=True, max_length=100, null=True, verbose_name='B_DQA_DataCode')),
                ('B_DQA_Reliability', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='B_DQA_Reliability')),
                ('B_DQA_Compatibility', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='B_DQA_Compatibility')),
                ('B_DQA_Result', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='B_DQA_Result')),
                ('B_RD_ESD', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='B_RD_ESD')),
                ('B_RD_EMI', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='B_RD_EMI')),
                ('B_RD_RF', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='B_RD_RF')),
                ('B_RD_1', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='B_RD_1')),
                ('B_RD_2', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='B_RD_2')),
                ('B_RD_3', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='B_RD_3')),
                ('B_RD_4', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='B_RD_4')),
                ('B_RD_5', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='B_RD_5')),
                ('C_DQA_DataCode', models.CharField(blank=True, max_length=100, null=True, verbose_name='C_DQA_DataCode')),
                ('C_DQA_Reliability', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='C_DQA_Reliability')),
                ('C_DQA_Compatibility', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='C_DQA_Compatibility')),
                ('C_DQA_Result', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='C_DQA_Result')),
                ('C_RD_ESD', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='C_RD_ESD')),
                ('C_RD_EMI', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='C_RD_EMI')),
                ('C_RD_RF', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='C_RD_RF')),
                ('C_RD_1', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='C_RD_1')),
                ('C_RD_2', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='C_RD_2')),
                ('C_RD_3', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='C_RD_3')),
                ('C_RD_4', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='C_RD_4')),
                ('C_RD_5', models.CharField(blank=True, choices=[('', ''), ('QS', 'QS'), ('Qd_L', 'Qd_L'), ('Qd_C', 'Qd_C'), ('QT', 'QT'), ('QF', 'QF'), ('DisQ', 'DisQ'), ('Drop', 'Drop'), ('Not Build', 'Not Build')], default='', max_length=10, null=True, verbose_name='C_RD_5')),
                ('Control_run', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Control_run')),
                ('Comments', models.CharField(blank=True, default='', max_length=4000, null=True, verbose_name='Comments')),
                ('editor', models.CharField(default='', max_length=100, verbose_name='editor')),
                ('edit_time', models.CharField(blank=True, default='', max_length=26, verbose_name='edit_time')),
            ],
            options={
                'verbose_name': 'MQM',
                'verbose_name_plural': 'MQM',
            },
        ),
    ]
