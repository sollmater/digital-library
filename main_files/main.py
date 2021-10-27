import sys
import sqlite3

from qt_design.python_design.main_window_design import Ui_MainWindow_Design
from qt_design.python_design.authorization import Ui_Authorization_Design
from qt_design.python_design.registration_design import Ui_Registration_Design
from qt_design.python_design.profile_information_design import Ui_Profile_Information_Design

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox

connection = sqlite3.connect('digital_library.sqlite')


class Authorization(QMainWindow, Ui_Authorization_Design):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.main_window = MyMainWindow(self)
        self.registration = Registration(self)

        self.pushButton.clicked.connect(self.check_authorization)
        self.pushButton_2.clicked.connect(self.make_registration)

    def check_authorization(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        req = """SELECT * FROM peoples WHERE name = ?"""
        cur = connection.cursor()
        result = cur.execute(req, (name,)).fetchone()
        if result:
            if password in result:
                self.close()
                self.main_window.get_profile_information(result[1], result[2], result[4], result[3], result[5])
                self.main_window.show()
            else:
                valid = QMessageBox.warning(self, 'Ошибка при входе!',
                                            'К сожалению, пароль не пододит, пожалуйста, повторите попытку')
        else:
            valid = QMessageBox.warning(self, 'Ошибка при входе!',
                                        'К сожалению, мы не можем найти ваше имя в базе данных. Пожалуйста, повторите попыткую')

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
        help = []
        help.append(self.lineEdit.text())
        help.append(self.spinBox.text())
        help.append(self.lineEdit_3.text())
        help.append(self.comboBox.currentText())
        help.append(self.lineEdit_5.text())
        if '' not in help:
            print(help)
        else:
            valid = QMessageBox.warning(self, 'Ошибка при регистрации!',
                                        'Нужно заполнить все графы при регистрации. Пожалуйста, повторите попытку')

        # self.close()
        # self.main_window.show()

    def come_back(self):
        self.authorization = Authorization(self)
        self.close()
        self.authorization.show()


class MyMainWindow(QMainWindow, Ui_MainWindow_Design):
    def __init__(self, parent=Authorization):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.show_profile_information)

        self.redraw_table_1()
        self.redraw_table_2()

    def password(self):
        uic.loadUi('main_window.ui', self)

    def redraw_table_1(self):
        req = """SELECT * FROM books"""
        cur = connection.cursor()
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
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

    def redraw_table_2(self):
        req = """SELECT * FROM books"""
        cur = connection.cursor()
        result = cur.execute(req).fetchall()
        self.tableWidget_2.setRowCount(len(result))
        if len(result):
            self.tableWidget_2.setColumnCount(len(result[0]))
        # получение заголовков таблицы с помощью cur.description
        self.titles = [description[0] for description in cur.description]
        # установка заголовков в таблицу
        self.tableWidget_2.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(val)))
        header = self.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

    def get_profile_information(self, name, age, role, password, mail):
        self.name = name
        self.age = age
        self.role = role
        self.password = password
        self.mail = mail

    def show_profile_information(self):
        self.profile_information = Profile_Information(self.name, self.age, self.role, self.password, self.mail)
        self.profile_information.show()


class Profile_Information(QMainWindow, Ui_Profile_Information_Design):
    def __init__(self, name, age, password, role, mail, parent=None):
        super().__init__()
        self.setupUi(self)

        self.name = name
        self.age = age
        self.role = role
        self.password = password
        self.mail = mail

        self.set_information()

    def set_information(self):
        self.label_4.setText(self.name)
        self.label_10.setText(str(self.age))
        self.label_13.setText(self.role)
        self.label_14.setText(self.password)
        self.label_15.setText(self.mail)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Authorization()
    ex.show()
    sys.exit(app.exec_())
