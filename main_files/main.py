import sys
import sqlite3

from qt_design.python_design.main_window_design import Ui_MainWindow_Design
from qt_design.python_design.authorization import Ui_Authorization_Design
from qt_design.python_design.registration_design import Ui_Registration_Design

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Authorization(QMainWindow, Ui_Authorization_Design):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.main_window = MyMainWindow(self)
        self.registration = Registration(self)
        self.pushButton.clicked.connect(self.check_authorization)
        self.pushButton_2.clicked.connect(self.make_registration)

    def check_authorization(self):
        self.close()
        self.main_window.show()

    def make_registration(self):
        self.close()
        self.registration.show()


class Registration(QMainWindow, Ui_Registration_Design):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.main_window = MyMainWindow(self)

        self.pushButton.clicked.connect(self.check_registration)
        self.pushButton_2.clicked.connect(self.come_back)

    def check_registration(self):
        self.close()
        self.main_window.show()

    def come_back(self):
        self.authorization = Authorization(self)
        self.close()
        self.authorization.show()


class MyMainWindow(QMainWindow, Ui_MainWindow_Design):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.con = sqlite3.connect('digital_library.sqlite')

        self.redraw_table()

    def password(self):
        uic.loadUi('main_window.ui', self)

    def redraw_table(self):
        req = """SELECT * FROM books"""
        cur = self.con.cursor()
        result = cur.execute(req).fetchall()
        self.tableWidget.setRowCount(len(result))
        if len(result):
            self.tableWidget.setColumnCount(len(result[0]))
        # получение заголовков таблицы с помощью cur.description
        self.titles = [description[0] for description in cur.description]
        # установка заголовков в таблицу
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Authorization()
    ex.show()
    sys.exit(app.exec_())
