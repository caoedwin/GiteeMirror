# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Excel_InputAIO.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_MainWindow(QWidget):
    # button_clicked_signal = pyqtSignal()
    # enable_button_signal = pyqtSignal()
    # disable_button_signal = pyqtSignal()
    # close_signal = pyqtSignal()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -30, 811, 581))
        self.frame.setStyleSheet("QFrame {    background-color: rgb(56, 58, 89);    \n"
                                 "    color: rgb(220, 220, 220);\n"
                                 "    border-radius: 10px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(300, 60, 104, 87))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(270, 46, 431, 121))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(100, 140, 571, 61))
        self.textEdit_3.setStyleSheet(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiSu\'; font-size:16pt; color:#00ffff;\">请选择客户别：</span></p></body></html>")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_4.setGeometry(QtCore.QRect(100, 280, 571, 51))
        self.textEdit_4.setObjectName("textEdit_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 190, 561, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setStyleSheet("font: 9pt \"楷体\";\n"
                                       "color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.horizontalLayout.addWidget(self.radioButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 330, 561, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_3.setStyleSheet("font: 9pt \"楷体\";\n"
                                         "color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_4.setStyleSheet("font: 9pt \"楷体\";\n"
                                         "color: rgb(255, 255, 255);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_2.setStyleSheet("font: 9pt \"楷体\";\n"
                                         "color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(580, 460, 93, 28))
        self.pushButton.setStyleSheet("font: 9pt \"楷体\";")
        self.pushButton.setObjectName("pushButton")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_5.setGeometry(QtCore.QRect(110, 450, 131, 51))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_7 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_7.setGeometry(QtCore.QRect(260, 450, 191, 61))
        self.textEdit_7.setObjectName("textEdit_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())

        # self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.action = QAction('退出(&X)')  # 定义一个Action即动作
        self.action.setStatusTip('Exit application')  # 状态栏信息
        self.action.triggered.connect(MainWindow.close)  # 触发事件动作为"关闭窗口"
        self.action.setShortcut('Ctrl+Q')  # 快捷键设置
        # self.statusBar()  # 状态栏信

        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit_2.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiSu\'; font-size:36pt; color:#fe79c7;\">模板选择</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiSu\'; font-size:16pt; color:#00ffff;\">请选择客户别：</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiSu\'; font-size:16pt; color:#00ffff;\">请选择Phase：</span></p></body></html>"))
        self.radioButton.setText(_translate("MainWindow", "C38(NB)"))
        self.radioButton_3.setText(_translate("MainWindow", "B(FVT)"))
        self.radioButton_4.setText(_translate("MainWindow", "C(SIT)"))
        self.radioButton_2.setText(_translate("MainWindow", "FFRT"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.textEdit_5.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:12px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiSu\'; font-size:8pt; color:#00ffff;\">运行状态：</span></p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:12px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiSu\'; font-size:8pt; color:#e0feff;\"> </span></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "选项"))
        self.actionexit.setText(_translate("MainWindow", "exit"))




