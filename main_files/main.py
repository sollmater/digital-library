import sys
import sqlite3

from qt_design.python_design.main_window_design import Ui_MainWindow_Design
from qt_design.python_design.authorization import Ui_Authorization_Design
from qt_design.python_design.registration_design import Ui_Registration_Design
from qt_design.python_design.profile_information_design import Ui_Profile_Information_Design
from qt_design.python_design.delete_item_form_design import Ui_Delete_Item_Form_Design
from qt_design.python_design.insert_item_form_design import Ui_Insert_Item_Form_Design
from qt_design.python_design.update_item_form_design import Ui_Update_Item_Form_Design

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

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
            if self.check_name(help[0]):
                req = """INSERT INTO peoples(name, age, password, role, mail) VALUES(?, ?, ?, ?, ?)"""
                cur = connection.cursor()
                result = cur.execute(req, (help[0], help[1], help[2], help[3], help[4],))
                if result:
                    connection.commit()
                    valid = QMessageBox.warning(self, 'Проверка регистрации!',
                                                'Поздравляю! Вы успешно зарегестрировались')
                    self.close()
                    self.main_window.get_profile_information(help[0], help[1], help[2], help[3], help[4])
                    self.main_window.show()
                else:
                    valid = QMessageBox.warning(self, 'Ошибка при регистрации!',
                                                'Что-то пошло не так')
            else:
                valid = QMessageBox.warning(self, 'Ошибка при регистрации!',
                                            'Такое имя уже есть!')
        else:
            valid = QMessageBox.warning(self, 'Ошибка при регистрации!',
                                        'Нужно заполнить все графы при регистрации. Пожалуйста, повторите попытку')

    def check_name(self, name):
        req = """SELECT * FROM peoples WHERE name = ?"""
        cur = connection.cursor()
        result = cur.execute(req, (name,))
        if len(list(result)) > 0:
            return False
        else:
            return True

    def come_back(self):
        self.authorization = Authorization(self)
        self.close()
        self.authorization.show()


class MyMainWindow(QMainWindow, Ui_MainWindow_Design):
    def __init__(self, parent=Authorization):
        super().__init__()
        self.setupUi(self)

        self.delete_form = DeleteItemForm(self)
        self.add_form = AddItemForm(self)
        self.update_form = UpdateItemForm(self)
        self.add_to_bookmarks_form = AddBookmarksItemForm(self)

        self.pushButton.clicked.connect(self.show_profile_information)
        self.pushButton_2.clicked.connect(self.show_delete)
        self.pushButton_3.clicked.connect(self.show_update)
        self.pushButton_4.clicked.connect(self.show_add_book)
        self.pushButton_5.clicked.connect(self.show_add_bookmarks)

        self.redraw_table_1()
        self.redraw_table_2()

        self.create_piechart_1()
        self.create_piechart_2()
        self.create_piechart_3()
        self.create_piechart_4()

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
        req = """SELECT * FROM bookmarks"""
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

    def show_delete(self):
        if self.role == 'Библиотекарь':
            self.delete_form.show()
        else:
            valid = QMessageBox.warning(self, 'Проверка системных прав!',
                                        'Только пользователь с должностью "Библиотекарь" может редактировать каталог книг')

    def delete_item_book(self, id):
        # запрос на удаление элементов
        try:
            req = """DELETE from books WHERE id = ?"""
            connection.execute(req, (id,))
            # сохраняем изменения
            connection.commit()
            # перерисовываем таблицу
            self.redraw_table_1()
        except:
            valid = QMessageBox.warning(self, 'Ошибка при работе с базой книг',
                                        'Произошла ошибка при удалении книг!')

    def show_update(self):
        if self.role == 'Библиотекарь':
            row = list([i.row() for i in self.tableWidget.selectedItems()])
            if not len(row):
                valid = QMessageBox.warning(self, 'Проверка ввода!',
                                            'Вы не выбрали строку для измененния')
            else:
                row = row[0]
                info = []
                for i in range(self.tableWidget.columnCount()):
                    info.append(self.tableWidget.item(row, i).text())
                self.update_form.set_info(*info)
                self.update_form.show()
        else:
            valid = QMessageBox.warning(self, 'Проверка системных прав!',
                                        'Только пользователь с должностью "Библиотекарь" может редактировать каталог книг')

    def show_add_book(self):
        if self.role == 'Библиотекарь':
            self.add_form.show()
        else:
            valid = QMessageBox.warning(self, 'Проверка системных прав!',
                                        'Только пользователь с должностью "Библиотекарь" может редактировать каталог книг')

    def show_add_bookmarks(self):
        row = list([i.row() for i in self.tableWidget.selectedItems()])
        if not len(row):
            valid = QMessageBox.warning(self, 'Проверка ввода!',
                                        'Вы не выбрали строку для измененния')
        else:
            row = row[0]
            info = []
            for i in range(self.tableWidget.columnCount()):
                info.append(self.tableWidget.item(row, i).text())
            self.add_to_bookmarks_form.get_id(info[0])
            self.add_to_bookmarks_form.save_item()

    def update_books(self, id, name, author, year, publisher, translator, genre):
        try:
            req = """UPDATE books SET name = ? , author = ? , year = ? , publisher = ? , translator = ? , genre = ? WHERE id = ?"""
            connection.execute(req, (name, author, year, publisher, translator, genre, id))
            # сохраняем изменения
            connection.commit()
            # перерисовываем таблицу
            self.redraw_table_1()
        except:
            valid = QMessageBox.warning(self, 'Ошибка при работе с базой книг',
                                        'Произошла ошибка при изменении книг!')

    def add_to_books(self, name, author, year, publisher, translator, genre):
        try:
            req = """INSERT INTO books(name, author, year, publisher, translator, genre) VALUES(?, ?, ?, ?, ?, ?)"""
            connection.execute(req, (name, author, year, publisher, translator, genre))
            connection.commit()
            self.redraw_table_1()
        except:
            valid = QMessageBox.warning(self, 'Ошибка при работе с базой книг',
                                        'Произошла ошибка при удалении книг!')

    def add_to_bookmarks(self, id):
        try:
            req = """SELECT * FROM books WHERE id = ?"""
            cur = connection.cursor()
            result = cur.execute(req, (id,)).fetchone()
            req_2 = """INSERT INTO bookmarks VALUES(?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(req_2, (result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
            self.redraw_table_2()
            connection.commit()
            valid = QMessageBox.warning(self, 'Добавление в список для чтения',
                                        'Книга успешно добавлена в список для чтения')
        except:
            valid = QMessageBox.warning(self, 'Ошибка при работе с базой книг',
                                        'Произошла ошибка при добавлении книги в список для чтения!')



    def get_profile_information(self, name, age, role, password, mail):
        self.name = name
        self.age = age
        self.role = role
        self.password = password
        self.mail = mail

    def show_profile_information(self):
        self.profile_information = Profile_Information(self.name, self.age, self.role, self.password, self.mail)
        self.profile_information.show()

    def create_piechart_1(self):
        series = QPieSeries()
        series.append("Фантастика", 80)
        series.append("Детектив", 70)
        series.append("Вестерн", 50)
        series.append("Роман", 40)
        series.append("Приключения", 30)

        slice = QPieSlice()
        slice = series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 0.5))
        slice.setBrush(Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Топ любимых жанров")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.gridLayout.addWidget(chartview)

    def create_piechart_2(self):
        series = QPieSeries()
        series.append("Фантастика", 80)
        series.append("Детектив", 70)
        series.append("Вестерн", 50)
        series.append("Роман", 40)
        series.append("Приключения", 30)

        # adding slice
        slice = QPieSlice()
        slice = series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 0.5))
        slice.setBrush(Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Топ любимых жанров")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.gridLayout_2.addWidget(chartview)

    def create_piechart_3(self):
        series = QPieSeries()
        series.append("Фантастика", 80)
        series.append("Детектив", 70)
        series.append("Вестерн", 50)
        series.append("Роман", 40)
        series.append("Приключения", 30)

        # adding slice
        slice = QPieSlice()
        slice = series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 0.5))
        slice.setBrush(Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Топ любимых жанров")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.gridLayout_3.addWidget(chartview)

    def create_piechart_4(self):
        series = QPieSeries()
        series.append("Фантастика", 80)
        series.append("Детектив", 70)
        series.append("Вестерн", 50)
        series.append("Роман", 40)
        series.append("Приключения", 30)

        # adding slice
        slice = QPieSlice()
        slice = series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 0.5))
        slice.setBrush(Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Топ любимых жанров")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.gridLayout_4.addWidget(chartview)


# Класс формы добавления, со всеми методами
class AddItemForm(QMainWindow, Ui_Insert_Item_Form_Design):
    def __init__(self, parent=None):
        super(AddItemForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.save_item)

    def save_item(self):
        name = self.lineEdit_4.text()
        author = self.lineEdit_5.text()
        year = self.lineEdit_6.text()
        publisher = self.lineEdit_7.text()
        translator = self.lineEdit_8.text()
        genre = self.lineEdit_9.text()
        # отправляем родительскому окну информацию для добавления
        self.parent().add_to_books(name, author, year, publisher, translator, genre)
        self.close()


# Класс формы удаления, со всеми методами
class AddBookmarksItemForm(QMainWindow):
    def __init__(self, parent=None):
        super(AddBookmarksItemForm, self).__init__(parent)

    def get_id(self, id):
        self.id = id

    def save_item(self):
        valid = QMessageBox.question(
            self, 'Подтверждение действий', "Действительно добавить элемент в список для чтения?",
            QMessageBox.Yes, QMessageBox.No)
        # Если пользователь ответил утвердительно,
        # переходим в функцию удаления элементов
        if valid == QMessageBox.Yes:
            self.parent().add_to_bookmarks(self.id)
        self.close()


# Класс формы удаления, со всеми методами
class DeleteItemForm(QMainWindow, Ui_Delete_Item_Form_Design):
    def __init__(self, parent=None):
        super(DeleteItemForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.save_delete_item)

    def save_delete_item(self):
        id = self.lineEdit.text()
        valid = QMessageBox.question(
            self, 'Подтверждение действий', "Действительно удалить элемент с id: " + str(id),
            QMessageBox.Yes, QMessageBox.No)
        # Если пользователь ответил утвердительно,
        # переходим в функцию удаления элементов
        if valid == QMessageBox.Yes:
            self.parent().delete_item_book(id)
        self.close()


# Класс формы обновления, со всеми методами
class UpdateItemForm(QMainWindow, Ui_Update_Item_Form_Design):
    def __init__(self, parent=None):
        super(UpdateItemForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.save_update_item)

    def set_info(self, id, name, author, year, publisher, translator, genre):
        self.id = id
        self.name = name
        self.author = author
        self.year = year
        self.publisher = publisher
        self.translator = translator
        self.genre = genre
        self.lineEdit_4.setText(self.name)
        self.lineEdit_5.setText(self.author)
        self.lineEdit_6.setText(self.year)
        self.lineEdit_7.setText(self.publisher)
        self.lineEdit_8.setText(self.translator)
        self.lineEdit_9.setText(self.genre)

    def save_update_item(self):
        name = self.lineEdit_4.text()
        author = self.lineEdit_5.text()
        year = self.lineEdit_6.text()
        publisher = self.lineEdit_7.text()
        translator = self.lineEdit_8.text()
        genre = self.lineEdit_9.text()

        self.parent().update_books(self.id, name, author, year, publisher, translator, genre)
        self.close()


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
