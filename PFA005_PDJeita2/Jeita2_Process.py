from PyQt5 import QtCore, QtGui, QtWidgets
from tishi import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtGui import *
import os, sys, subprocess, time, shutil, glob, pprint
# import win32api,win32con,KB_input

import warnings

from configparser import ConfigParser
class Readini(ConfigParser):
    def __init__(self, filename):
        #对父类进行初始化
        super().__init__()
        #读取配置文件，并设置编码格式
        self.read(filename)

class MainFunc(QMainWindow, Ui_MainWindow):
    def __init__(self, str, str2="即将开始：", str3="""提示：\n请确认电量是100%，点击开始后，拔除电源！""",butname="开始"):

        super(MainFunc, self).__init__()
        self.setupUi(self)
        self.label_4.setText(str)
        self.label_3.setText(str2)
        self.label.setText(str3)
        self.pushButton.setText(butname)
        self.pushButton.clicked.connect(self.close)


def mymovefile(srcfile, dstpath):  # 移动函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.move(srcfile, dstpath + fname)  # 移动文件
        # print("move %s -> %s" % (srcfile, dstpath + fname))

import pandas as pd
import matplotlib.pyplot as plt
def column_chart(excel_path, sheet_name = 0):
    """
    柱状图
    :param excel_path:
    :param sheet_name:
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    # print(df)
    # 接下来我们通过pandas库下面的bar来设置柱形图的X，Y坐标轴
    df.plot.area(x="Date and Time", y="Current Capacity")#生成的是png图片没有组合图表
    # 然后通过pyplot的show方法将柱形图进行展示出来
    plt.show()#没有保存到excel中

import xlsxwriter
#缺点：xlsxwriter不能对已存在的Excel进行编辑插入图标
def XlsxWriterCombo(excel_path,type1="column", type2="line"):
    df = pd.read_excel(excel_path)
    # print(type(df))
    # print(df.shape)  # 获取行数列数
    AllData = parsedata(df)
    # pprint.pprint(AllData)
    # print(type(AllData))
    categories = '=Sheet1!$B$2:$B$%s' % (df.shape[0] + 2)
    name1 = '=Sheet1!$D$1'
    name2 = '=Sheet1!$F$1'
    values1 = '=Sheet1!$D$2:$D$%s' % (df.shape[0] + 2)
    values2 = '=Sheet1!$F$2:$F$%s' % (df.shape[0] + 2)
    # print(categories, values1, values2)

    # Workbook() takes one, non-optional, argument which is the filename #that we want to create.
    Chart_path = excel_path.replace("LOG", "Chart")
    workbook = xlsxwriter.Workbook(Chart_path)
    # The workbook object is then used to add new worksheet via the #add_worksheet() method.
    worksheet = workbook.add_worksheet()
    # Create a new Format object to formats cells in worksheets using #add_format() method .
    # here we create bold format object .
    bold = workbook.add_format({'bold': True})
    # Add the worksheet data that the charts will refer to.
    # headings = ['Number', 'Batch 1', 'Batch 2']
    headings = AllData[0]
    # data = [
    #    [2, 3, 4, 5, 6, 7],
    #    [10, 40, 50, 20, 10, 50],
    #    [30, 60, 70, 50, 40, 30],
    # ]
    data = AllData[1:]
    # Write a row of data starting from 'A1' with bold format .
    worksheet.write_row('A1', headings, bold)
    # Write a column of data starting from 'A2', 'B2', 'C2' respectively .
    worksheet.write_column('A2', data[0])
    # print(type(data[1]), type(data[3]), type(data[5]), )
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])
    worksheet.write_column('D2', data[3])
    worksheet.write_column('E2', data[4])
    worksheet.write_column('F2', data[5])
    worksheet.write_column('G2', data[6])
    # Create a chart object that can be added to a worksheet using #add_chart() method.
    #here we create a column chart object.This will use as the primary #chart.
    column_chart1 = workbook.add_chart({'type': type1})
    # Add a data series to a chart using add_series method.
    # Configure the first series.
    # = Sheet1 !$A$1 is equivalent to ['Sheet1', 0, 0].
    # note : spaces is not inserted in b/w = and Sheet1, Sheet1 and !
    # if space is inserted it throws warning.
    column_chart1.add_series({
        # 'name': '=Sheet1!$B$1',
       'name':       name1,
       # 'categories': '=Sheet1!$A$2:$A$7',#[=sheetnameA1(起始单元格标识)F1(结束单元格标识)last_col]或者用第二种添加方式：[sheetname, first_row, first_col, last_row, last_col]['Sheet1', 0, 0, 4, 0]
       'categories': categories,
       # 'values':     '=Sheet1!$B$2:$B$7',
       'values':     values1,
    })
    # Create a new line chart.This will use as the secondary chart.
    line_chart1 = workbook.add_chart({'type': type2})
    # Configure the data series for the secondary chart.
    line_chart1.add_series({
        # 'name': '=Sheet1!$C$1',
       'name':       name2,
       # 'categories': '=Sheet1!$A$2:$A$7',
       'categories': categories,
        # 'values': '=Sheet1!$C$2:$C$7',
       'values':     values2,
        "y2_axis": True,
    })
    line_chart1.set_y2_axis({
        'name': 'Rate',
    })
    # column_chart1.set_y2_axis({'name': 'Rate',})
    # Combine both column and line chatrs together.
    column_chart1.combine(line_chart1)
    # Add a chart title
    column_chart1.set_title({'name': '图表标题'})
    # Add x-axis label
    # column_chart1.set_x_axis({'name': 'Test number'})
    # Add y-axis label
    column_chart1.set_y_axis({'name': 'Current Capacity'})
    column_chart1.set_legend({"position": "bottom"})

    # add chart to the worksheet with given offset values at the top-left #corner of a chart is anchored to cell D2
    worksheet.insert_chart('J2', column_chart1)
    # Finally, close the Excel file via the close() method.
    workbook.close()
def parsedata(dictdata, columns=[]):
    result = []
    if columns == []:
        keys = dictdata.keys()
    else:
        keys = columns
    result.append([key for key in keys])
    # pprint.pprint(result)
    # values = []
    # for key in keys:
    #     print(dictdata[key],'111')
    #     values.append(dictdata[key])
    # print(values,'222')
    # values = zip(*values)
    # for value in values:
    #     result.append(list(value))
    for key in keys:
        # print(dictdata[key],'111')
        result.append(list(dictdata[key]))
    return result
from PyQt5.QtCore import Qt
try:
    if __name__ == '__main__':
        ######使用下面的方式一定程度上可以解决界面模糊问题--解决电脑缩放比例问题
        QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        # QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        # 在主函数入口之前加入上面的设置即可解决


        # path1 = os.path.dirname(__file__)  # 当前文件所在的目录
        # os.path.abspath('.')
        path1 = os.path.dirname(os.path.realpath(sys.executable))
        startup_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
        startup_file = startup_path + "\Jeita2_Startup.exe"
        ini_file = path1 + "\Times.ini"
        settings_file = path1 + "\setting.exe"
        TimeA_file = path1 + "\BatteryMonitorA.exe"
        TimeB_file = path1 + "\BatteryMonitorB.exe"
        # setlog_file1 = path1 + "\SysSettingsModifier_V4.2022\*.txt"
        # setlog_file2 = path1 + "\*.txt"
        # print(ini_file)
        with open('dataPropath1.txt', 'w') as f:  # 设置文件对象
            print(path1,ini_file, os.path.exists(ini_file),file=f)
        if os.path.exists(ini_file):
            ini_contend =Readini(ini_file)
            restartcycles = ini_contend.get('section1', 'Restart')
            # print(restartcycle
            #
            # s)
            if restartcycles == '1':
                # subprocess.call(TimeA_file)

                # os.system('start "C:\Program Files\WindowsApps\Microsoft.ZuneVideo_10.22041.10091.0_x64__8wekyb3d8bbwe\Video.UI.exe" "C:/PythonProject/PFA005_PDJeita2\JB2_0.mp4"')
                # time.sleep(4)
                # KB_input.press('tab', 'tab', 'tab', 'tab', 'tab')
                # time.sleep(1)
                # KB_input.press('enter')
                # time.sleep(1)
                # KB_input.press('tab', 'tab')
                # time.sleep(1)
                # KB_input.press('enter')
                # time.sleep(1)
                # KB_input.press('esc')
                # time.sleep(2)
                # app = QApplication(sys.argv)
                # C = MainFunc("TimeA")
                # C.show()
                # # QtWidgets.QMessageBox.information(None, 'TimeA：准备测试', '%s' % "确保电量是100%后，点击OK，拔除AC，开始测试")
                # time.sleep(1)
                # # print(1)
                # KB_input.pressHoldRelease('alt', 'enter')
                #
                #
                # sys.exit(app.exec())
                VideoRootpath = "C:/Program Files/WindowsApps/"
                files = [f for f in glob.glob('C:/Program Files/WindowsApps/**/Video.UI.exe')]
                if files:
                    os.environ['VideoUIPath'] = files[0]
                    os.putenv('VideoUIPath', files[0])
                    command = r"setx 'VideoUIPath' '%s' /m" % files[0]
                    os.system(command)
                    # print(files[0])
                # for f in files:
                #     os.environ['VideoUIPath'] = f
                #     print(f)


                app = QApplication(sys.argv)
                C = MainFunc(str="TimeA", str3="""提示：\n确认电量是100%，再点击开始.\n等到全屏播放视频后，拔除电源！""")
                C.show()
                if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
                    QtWidgets.QApplication.instance().exec_()
                subprocess.call(TimeA_file, shell=True)
                # sys.exit(app._exec())

            elif restartcycles == '2':


                app = QApplication(sys.argv)
                C = MainFunc("TimeB")
                C.show()
                if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
                    QtWidgets.QApplication.instance().exec_()
                subprocess.call(TimeB_file, shell=True)
                # sys.exit(app.exec_())
            elif restartcycles == '3':#所有测试都做完了，删除_startup文件， ini文件
                # if os.path.exists(ini_file):
                #     os.remove(ini_file)
                os.chdir(startup_path)
                if os.path.isfile('Jeita2_Startup.exee'):
                    os.remove('Jeita2_Startup.exe')
                # if os.path.exists(startup_file):
                #     os.remove(startup_file)
                os.chdir(path1)

                src_dir = path1 + '/'
                # src_dir = './'

                # src_dir = './'
                # dst_dir = './oldlogs/'  # 目的路径记得加斜杠
                dst_dir = path1 + '/oldlogs/'  # 目的路径记得加斜杠
                if not os.path.exists(dst_dir):
                    os.mkdir(dst_dir)
                src_file_list = glob.glob(src_dir + '*.csv')  # glob获得路径下所有文件，可根据需要修改
                src_file_list_txt = glob.glob(src_dir + '*.txt')  # glob获得路径下所有文件，可根据需要修改
                src_file_list_ini = glob.glob(src_dir + '*.ini')  # glob获得路径下所有文件，可根据需要修改
                # print(src_dir)
                # print(src_file_list)
                for srcfile in src_file_list:
                    # print(srcfile)
                    # 读取csv文件
                    df = pd.read_csv(srcfile, encoding="gb2312")
                    df["Charge Rate"] = df['Charge Rate'].apply(
                        lambda x: str(float(x) * (-1)) if x else x
                    )
                    # 转存excel文件，index参数为False，不将index列存到excel文件里
                    xlsx_srcfile = str(srcfile).replace('csv', 'xlsx')
                    df.to_excel(xlsx_srcfile, sheet_name='Sheet1', index=False)

                    mymovefile(srcfile, dst_dir)

                for srcfile in src_file_list_txt:
                    if "requirements" not in str(srcfile):
                        mymovefile(srcfile, dst_dir)
                for srcfile in src_file_list_ini:
                    mymovefile(srcfile, dst_dir)
                src_file_list_xlsx = glob.glob(src_dir + '*.xlsx')  # glob获得路径下所有文件，可根据需要修改
                for srcfile in src_file_list_xlsx:
                    # column_chart(srcfile)
                    df = pd.read_excel(srcfile)
                    # print(df)
                    # print(df.shape)  # 获取行数列数
                    categories = '= Sheet1 !$B$2:$B$%s' % (df.shape[1]+2)
                    name1 = '= Sheet1 !$D$1'
                    name2 = '= Sheet1 !$F$1'
                    values1 = '= Sheet1 !$D$2:$D$%s' % (df.shape[1]+2)
                    values2 = '= Sheet1 !$F$2:$F$%s' % (df.shape[1]+2)
                    XlsxWriterCombo(srcfile, type1="area", type2="line")
                    os.system('del "%s"' % srcfile)
                    # mymovefile(srcfile, dst_dir)

                src_file_list_xlsx = glob.glob(src_dir + '*.xlsx')
                for srcfile in src_file_list_xlsx:
                    mymovefile(srcfile, dst_dir)

                # os.system('del "%s"' % setlog_file1)#刚开始也要执行一遍伤处txt log
                # os.system('del "%s"' % setlog_file2)
                # if os.path.exists(startup_file):
                #     os.system('del "%s"' % startup_file)

                # print(os.listdir(path1 + "\SysSettingsModifier_V4.2022"))
                app = QApplication(sys.argv)
                # QtWidgets.QMessageBox.information(None, '测试完成', '%s' % "所有测试都已完成，点击OK退出程序")
                C = MainFunc("所有测试都已完成，点击OK退出程序", "完成", "所有测试都已完成，点击OK退出", "OK")
                C.show()
                # sys.exit(app.exec())#不加_的程式不结束

                sys.exit(app.exec())
            else:
                pass
        else:
            # pass
            app = QApplication(sys.argv)
            C = MainFunc(str="SysSettingsModifier", str3="""提示：
            自动化工具测试前需要设置亮度为150nits，
            SysSettingsModifier工具无法设定的也需要手动设定，
            再运行该工具!!!""")
            C.show()
            # print(sys.flags.interactive, hasattr(QtCore, 'PYQT_VERSION'))
            if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
                QtWidgets.QApplication.instance().exec_()
                # print(sys.flags.interactive, hasattr(QtCore, 'PYQT_VERSION'))
                # print('ssss')
            subprocess.call(settings_file, shell=True)#WindowsError: [Error 740]
            while 1:
                if "_APSLog" in str(os.listdir(path1)):
                    os.system('shutdown -r')
                    break

except Exception as e:
    with open('errorProcess.txt', 'w') as f:  # 设置文件对象
        print(e, file=f)