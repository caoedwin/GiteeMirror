# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Excelmain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(834, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QFrame {    background-color: rgb(56, 58, 89);    \n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_3.setMinimumSize(QtCore.QSize(0, 80))
        self.radioButton_3.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_5.addWidget(self.radioButton_3, 0, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_4.setMinimumSize(QtCore.QSize(0, 80))
        self.radioButton_4.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_5.addWidget(self.radioButton_4, 0, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setMinimumSize(QtCore.QSize(0, 80))
        self.radioButton_2.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_5.addWidget(self.radioButton_2, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 5, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(180, 60))
        self.label_5.setMaximumSize(QtCore.QSize(180, 60))
        self.label_5.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(255, 255, 127);\n"
"font-weight:bold;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("font: 9pt \"楷体\";")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 7, 2, 1, 1, QtCore.Qt.AlignRight)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setMinimumSize(QtCore.QSize(0, 80))
        self.radioButton.setStyleSheet("font: 11pt \"楷体\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_6.addWidget(self.radioButton, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 3, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(0, 60))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_3.setStyleSheet("font: 14pt \"楷体\";\n"
"color: rgb(0, 255, 255);\n"
"font-weight:bold;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(0, 60))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_2.setStyleSheet("font: 14pt \"楷体\";\n"
"color: rgb(0, 255, 255);\n"
"font-weight:bold;")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 120))
        self.label.setStyleSheet("font: 28pt \"楷体\";\n"
"color: rgb(255, 170, 255);\n"
"font-weight:bold;\n"
"text-align:center;")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(60, 60))
        self.label_4.setMaximumSize(QtCore.QSize(100, 60))
        self.label_4.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(0, 255, 255);\n"
"font-weight:bold;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 8, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(0, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 9, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 26))
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_3.setText(_translate("MainWindow", "B(FVT)"))
        self.radioButton_4.setText(_translate("MainWindow", "C(SIT)"))
        self.radioButton_2.setText(_translate("MainWindow", "FFRT"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.radioButton.setText(_translate("MainWindow", "C38(NB)"))
        self.label_3.setText(_translate("MainWindow", "请选择Phase："))
        self.label_2.setText(_translate("MainWindow", "请选择客户别："))
        self.label.setText(_translate("MainWindow", "模板选择"))
        self.label_4.setText(_translate("MainWindow", "运行状态："))
        self.label_6.setText(_translate("MainWindow", "DDIS Ecel转换工具-NB 版本：V1.0 开发者：DQA Auto Team"))
        self.menu.setTitle(_translate("MainWindow", "选项"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
