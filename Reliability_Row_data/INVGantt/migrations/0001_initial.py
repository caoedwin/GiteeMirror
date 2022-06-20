# Generated by Django 2.1.7 on 2020-10-08 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='INVGantt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.CharField(choices=[('', ''), ('C38(NB)', 'C38(NB)'), ('C38(AIO)', 'C38(AIO)'), ('A39', 'A39'), ('Others', 'Others')], max_length=100, verbose_name='Customer')),
                ('INV_Number', models.CharField(max_length=100, verbose_name='INV_Number')),
                ('INV_Model', models.CharField(max_length=100, verbose_name='INV_Model')),
                ('Project_Name', models.CharField(max_length=100, verbose_name='Project_Name')),
                ('Year', models.CharField(max_length=100, verbose_name='Year')),
                ('Unit_Qty', models.CharField(max_length=100, verbose_name='Unit_Qty')),
                ('TP_Kinds', models.CharField(max_length=100, verbose_name='TP_Kinds')),
                ('Qualify_Cycles', models.CharField(choices=[('', ''), ('New-Qualify', 'New-Qualify'), ('Re-Qualify', 'Re-Qualify')], max_length=100, verbose_name='Qualify_Cycles')),
                ('Status', models.CharField(choices=[('', ''), ('Pass', 'Pass'), ('Conditional Pass', 'Conditional Pass'), ('Fail', 'Fail'), ('Planning', 'Planning'), ('Pending', 'Pending'), ('Testing', 'Testing')], max_length=100, verbose_name='Status')),
                ('TP_Cat', models.CharField(choices=[('', ''), ('adapter', 'adapter'), ('Battery', 'Battery'), ('BIOS ROM', 'BIOS ROM'), ('Camera', 'Camera'), ('Connector', 'Connector'), ('CPU', 'CPU'), ('EE', 'EE'), ('FAN', 'FAN'), ('Finger Print', 'Finger Print'), ('HDD', 'HDD'), ('KB/Mouse', 'KB/Mouse'), ('Keyborad', 'Keyborad'), ('ME', 'ME'), ('package', 'package'), ('Panel', 'Panel'), ('RAM', 'RAM'), ('SSD', 'SSD'), ('SSD+Opante', 'SSD+Opante'), ('Thermal Module', 'Thermal Module'), ('Touch Panel', 'Touch Panel'), ('TPM', 'TPM'), ('VRAM', 'VRAM'), ('WLAN', 'WLAN')], max_length=100, verbose_name='TP_Cat')),
                ('Trial_Run_Type', models.CharField(max_length=100, verbose_name='Trial_Run_Type')),
                ('TP_Vendor', models.CharField(max_length=100, verbose_name='TP_Vendor')),
                ('TP_Key_Parameter', models.CharField(max_length=500, verbose_name='TP_Key_Parameter')),
                ('Lenovo_TP_PN', models.CharField(max_length=100, verbose_name='Lenovo_TP_PN')),
                ('Compal_TP_PN', models.CharField(max_length=100, verbose_name='Compal_TP_PN')),
                ('Issue_Link', models.CharField(max_length=100, verbose_name='Issue_Link')),
                ('Remark', models.CharField(max_length=1000, verbose_name='Remark')),
                ('Attend_Time', models.CharField(max_length=100, verbose_name='Attend_Time')),
                ('Get_INV', models.CharField(max_length=100, verbose_name='Get_INV')),
                ('Month', models.CharField(choices=[('', ''), ('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], max_length=100, verbose_name='Month')),
                ('Test_Start', models.DateField(verbose_name='Test_Start')),
                ('Test_End', models.DateField(verbose_name='Test_End')),
                ('Editor', models.CharField(max_length=20, verbose_name='Editor')),
                ('Edittime', models.DateTimeField(max_length=20, verbose_name='Edittime')),
            ],
        ),
    ]
