import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from title import *
from titleok import *
# from osgeo import gdal
import os
from PyQt5 import QtWidgets, QtCore

# 多线程
class Runthread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal(int)

    def __init__(self, main):
        super(Runthread, self).__init__()
        self.main = main

    # 计算函数
    def run(self):
        # 分块影像所在文件夹，不能有中文
        print(self.main)
        tifDir = self.main["tifDir"]
        # 输出的文件夹，不能有中文，如果文件夹不存在则会被创建
        outPath = self.main["outPath"]
        if not os.path.exists(outPath):
            os.makedirs(outPath)

        tifs = [i for i in os.listdir(tifDir) if i.endswith(".tif")]

        print("有 %s 个tif文件" % len(tifs))
        print("tifs", tifs)
        datelist1 = []
        for i in tifs:
            datelist1.append(i[:-4])
        datelist = list(set(datelist1))
        datelist.sort(key=datelist1.index)
        print("有 %s 个日期" % len(datelist))
        print("datelist", datelist)
        # 定义切图的大小（矩形框）
        size = 256
        # len(datelist)

        for img in range(3):
            print("正在分割：", tifs[img])
            in_ds = gdal.Open(tifDir + "\\" + tifs[img])  # 读取要切的原图

            width = in_ds.RasterXSize  # 获取数据宽度
            height = in_ds.RasterYSize  # 获取数据高度
            outbandsize = in_ds.RasterCount  # 获取数据波段数
            im_geotrans = in_ds.GetGeoTransform()  # 获取仿射矩阵信息
            im_proj = in_ds.GetProjection()  # 获取投影信息
            datatype = in_ds.GetRasterBand(1).DataType
            im_data = in_ds.ReadAsArray()  # 获取数据

            col_num = int(width / size)  # 宽度可以分成几块
            row_num = int(height / size)  # 高度可以分成几块
            if (width % size != 0):
                col_num += 1
            if (height % size != 0):
                row_num += 1

            # print("row_num:%d   col_num:%d" % (row_num, col_num))
            for i in range(row_num):  # 从高度下手！！！ 可以分成几块！
                for j in range(col_num):
                    offset_x = i * size
                    offset_y = j * size
                    ## 从每个波段中切需要的矩形框内的数据(注意读取的矩形框不能超过原图大小)
                    b_ysize = min(width - offset_y, size)
                    b_xsize = min(height - offset_x, size)

                    # print("width:%d     height:%d    offset_x:%d    offset_y:%d     b_xsize:%d     b_ysize:%d" % (width, height, offset_x, offset_y, b_xsize, b_ysize))
                    # print(im_data.shape)

                    out_allband = im_data[:, offset_x:offset_x + b_xsize, offset_y:offset_y + b_ysize]
                    # print(out_allband.shape)

                    # 获取Tif的驱动，为创建切出来的图文件做准备
                    gtif_driver = gdal.GetDriverByName("GTiff")
                    file = outPath + "\\" + tifs[img][:-4] + "-" + str(offset_x).zfill(10) + "-" + str(offset_y).zfill(
                        10) + ".tif"

                    # 创建切出来的要存的文件
                    out_ds = gtif_driver.Create(file, b_ysize, b_xsize, outbandsize, datatype)
                    # print("create new tif file succeed")

                    # 获取原图的原点坐标信息
                    ori_transform = in_ds.GetGeoTransform()
                    # if ori_transform:
                    # print(ori_transform)
                    # print("Origin = ({}, {})".format(ori_transform[0], ori_transform[3]))
                    # print("Pixel Size = ({}, {})".format(ori_transform[1], ori_transform[5]))

                    # 读取原图仿射变换参数值
                    top_left_x = ori_transform[0]  # 左上角x坐标
                    w_e_pixel_resolution = ori_transform[1]  # 东西方向像素分辨率
                    top_left_y = ori_transform[3]  # 左上角y坐标
                    n_s_pixel_resolution = ori_transform[5]  # 南北方向像素分辨率

                    # 根据反射变换参数计算新图的原点坐标
                    top_left_x = top_left_x + offset_y * w_e_pixel_resolution
                    top_left_y = top_left_y + offset_x * n_s_pixel_resolution

                    # 将计算后的值组装为一个元组，以方便设置
                    dst_transform = (
                        top_left_x, ori_transform[1], ori_transform[2], top_left_y, ori_transform[4], ori_transform[5])

                    # 设置裁剪出来图的原点坐标
                    out_ds.SetGeoTransform(dst_transform)

                    # 设置SRS属性（投影信息）
                    out_ds.SetProjection(in_ds.GetProjection())

                    # 写入目标文件
                    for ii in range(outbandsize):
                        out_ds.GetRasterBand(ii + 1).WriteArray(out_allband[ii])

                    # 将缓存写入磁盘
                    out_ds.FlushCache()
                    # print("FlushCache succeed")
                    del out_ds
                # print(i/row_num)
                # self.progressBar.setValue(int(100*(i+1)/row_num))
                # self._signal.emit(int(100*(i+1)/row_num))  # 注意这里与_signal = pyqtSignal(str)中的类型相同
                self._signal.emit(
                    int(100 * (img / 3 + (i + 1) / (row_num * 3))))  # 注意这里与_signal = pyqtSignal(str)中的类型相同


class MyWindow(QtWidgets.QMainWindow, Ui_tile):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.maindata = {}

        # 绑定事件
        self.pushButton.clicked.connect(self.start_cacu)
        # 打开文件夹
        self.menu.triggered[QAction].connect(self.wenjianjia)

        # 选择文件夹
        act = QAction(self)  # 定义一个行为
        act.setIcon(QIcon('image/select.png'))  # 设置行为icon，
        act.triggered.connect(self.outdir)  # 绑定行为槽函数，这里槽函数为一个QMessageBox信息弹窗
        self.lineEdit_2.addAction(act, QLineEdit.TrailingPosition)  # 将该行为添加到lineEdit最右端

        # 数据列表添加点击事件
        self.listWidget.itemClicked.connect(self.itemClick)

    def outdir(self):
        if not os.path.exists(r"E:\pyimg\tif2csv"):
            self.maindata["outPath"] = QFileDialog.getExistingDirectory(None, "输出文件夹", "C:/")  # 返回选中的文件夹路径
            # QFileDialog.getOpenFileName()  # 返回选中的文件路径
            # QFileDialog.getOpenFileNames()  # 返回选中的多个文件路径
            # QFileDialog.getSaveFileName()  # 存储文件
        else:
            self.maindata["outPath"] = QFileDialog.getExistingDirectory(None, "输出文件夹",
                                                                        "E:\\pyimg\\tif2csv")  # 返回选中的文件夹路径
        self.lineEdit_2.setText((QtCore.QCoreApplication.translate("tile", self.maindata["outPath"])))
        print(self.maindata)

    def wenjianjia(self):
        if not os.path.exists(r"E:\pyimg\tif2csv"):
            self.maindata["tifDir"] = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 返回选中的文件夹路径
        else:
            self.maindata["tifDir"] = QFileDialog.getExistingDirectory(None, "选取文件夹",
                                                                       "E:\\pyimg\\tif2csv")  # 返回选中的文件夹路径
        # self.maindata["tifDir"]=QFileDialog.getExistingDirectory(None,"选取文件夹","E:/")  # 返回选中的文件夹路径
        print(self.maindata)
        self.maindata["tifs"] = [i for i in os.listdir(self.maindata["tifDir"]) if i.endswith(".tif")]
        # 数据列表框添加内容
        for img in self.maindata["tifs"]:
            self.listWidget.addItem(str(img))

    # 数据列表框添加点击事件
    def itemClick(self, item):
        print(item.text() + " clicked!")
        QMessageBox.information(self, "ListWidget", "你选择了：" + item.text())

    # 计算函数
    def start_cacu(self):
        # 子窗体
        self.child = childWindow()
        self.child.pushButton.setVisible(False)
        self.child.show()

        self.maindata["分块大小"] = self.lineEdit.text()
        # 创建线程
        self.thread = Runthread(self.maindata)
        # 连接信号
        self.thread._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        self.child.stop_thread.connect(self.thread.terminate)
        # 开始线程
        self.thread.start()

    # 将线程的参数传入进度条事件
    def call_backlog(self, msg):
        self.child.progressBar.setValue(int(msg))
        if (msg == 100):
            self.child.pushButton.setVisible(True)

    # 重写closeEvent方法，关闭窗口时触发
    def closeEvent(self, QCloseEvent):
        reply = QtWidgets.QMessageBox.question(self, '分块程序', "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


class childWindow(QDialog, Ui_Dialog):
    stop_thread = pyqtSignal()  # 定义关闭子线程的信号

    def __init__(self):
        super(childWindow, self).__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.btn1)
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.accept)

    # 窗口关闭就关闭线程
    def closeEvent(self, event):
        self.stop_thread.emit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
