from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QStandardItemModel

from design import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from app import run as run_server, stop
import threading
import sqlite3


class MyThread(QThread):
    def __init__(self):
        super().__init__()
        self.ip = ""
        self.port = ""

    def add(self, ip, port):
        self.ip = ip
        self.port = port

    def __del__(self):
        self.wait()

    def run(self):
        run_server(ip=self.ip, port=self.port)


# Controller
class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.runButton.clicked.connect(
            lambda: self.start_server(self.ui.ipAddress.text(), self.ui.portNumber.text()))
        self.conn = sqlite3.connect('mock_Wechat.db')
        self.c = self.conn.cursor()
        self.thread = MyThread()
        self.server_status = "stop"
        self.ui.loadBtn.clicked.connect(self.show_table)
        self.show()

    def start_server(self, ip, port):
        if self.server_status == "run":
            self.stop_server()
        else:
            self.thread.add(self.ui.ipAddress.text(), self.ui.portNumber.text())
            self.ui.textEdit.append("Start server at {} port: {}".format(ip, port))
            self.thread.start()
            self.server_status = "run"
            self.ui.runButton.setText("Stop")

    def stop_server(self):
        self.ui.textEdit.append("Stop server")
        self.thread.terminate()
        sys.exit(app.exec_())

    def show_table(self):
        if self.ui.user_btn.isChecked():
            self.show_user_table()
        elif self.ui.contact_btn.isChecked():
            self.show_contact_table()
        elif self.ui.message_btn.isChecked():
            self.show_message_table()

    def show_user_table(self):
        data = self.c.execute("SELECT * FROM user").fetchall()
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(3)
        header = ['user_id', 'image_url', 'password']
        self.ui.tableWidget.setHorizontalHeaderLabels(header)
        for i, j in enumerate(data):
            user_id, img_url, password = j
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(user_id))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(img_url))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(password))

    def show_contact_table(self):
        data = self.c.execute("SELECT * FROM contact").fetchall()
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(6)
        header = ['room_id', 'name', 'room_owner', "friend", "last_message", "number_of_unread"]
        self.ui.tableWidget.setHorizontalHeaderLabels(header)
        for i, j in enumerate(data):
            room_id, name, room_owner, friend, last_message, number_of_unread = j
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(room_id))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(name))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(room_owner))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(friend))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(last_message))
            self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(number_of_unread))

    def show_message_table(self):
        data = self.c.execute("SELECT * FROM message").fetchall()
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(6)
        header = ['room_id', 'time', 'sender', "receiver", "content", "read"]
        self.ui.tableWidget.setHorizontalHeaderLabels(header)
        for i, j in enumerate(data):
            room_id, time, sender, receiver, content, read = j
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(room_id))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(time))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(sender))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(receiver))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(content))
            self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(read))


app = QApplication(sys.argv)
w = AppWindow()
try:
    sys.exit(app.exec_())
except Exception as e:
    print(e)
