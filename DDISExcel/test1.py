"""
多线程更新UI数据(在两个线程中传递函数)
"""
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
import time
import sys


class BackendThread(QThread):
    update_date = pyqtSignal(str)

    # 在子线程start以后, 自动调用
    # 主要功能是发送当前的时间
    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currentTime))
            time.sleep(1)


class ThreadUpdate(QDialog):
    def __init__(self):
        super(ThreadUpdate, self).__init__()
        self.setWindowTitle("多线程更新UI数据")
        self.resize(400, 100)
        self.input = QLineEdit(self)
        self.input.resize(400, 100)

        self.initUI()

    def initUI(self):
        # 构造子线程
        self.backbend = BackendThread()
        # 在主线程定义, 子线程的信号槽函数
        self.backbend.update_date.connect(self.handleDisplay)
        # start以后会调用run函数
        self.backbend.start()

    def handleDisplay(self, data):
        self.input.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = ThreadUpdate()
    main.show()

    sys.exit(app.exec_())