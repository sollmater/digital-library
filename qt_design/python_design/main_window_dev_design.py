# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_dev.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Design_Dev(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1139, 782)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(111)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_2, 5, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_6.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 0, 4, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_6.addWidget(self.tableWidget, 7, 0, 1, 5)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_6.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_6.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_6.addWidget(self.lineEdit_2, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 3, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_6.addWidget(self.lineEdit_3, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 3, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_6.addWidget(self.pushButton_7, 6, 1, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.tab_2.setFont(font)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_8.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_8.addWidget(self.tableWidget_2, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(545, 23))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_8.addWidget(self.pushButton, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_5.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionuil = QtWidgets.QAction(MainWindow)
        self.actionuil.setObjectName("actionuil")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Электронная Библиотека"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Каталог</p></body></html>"))
        self.tab.setToolTip(_translate("MainWindow", "<html><head/><body><p>Каталог</p><p><br/></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "фантастика"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "детектив"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "роман"))
        self.label.setText(_translate("MainWindow", "Фильтры:"))
        self.pushButton_4.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_5.setText(_translate("MainWindow", "В закладки"))
        self.pushButton_3.setText(_translate("MainWindow", "Обновить"))
        self.label_2.setText(_translate("MainWindow", "Год"))
        self.label_4.setText(_translate("MainWindow", "Автор"))
        self.label_3.setText(_translate("MainWindow", "Жанр"))
        self.pushButton_7.setText(_translate("MainWindow", "Применить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Каталог"))
        self.pushButton_6.setText(_translate("MainWindow", "Удалить"))
        self.pushButton.setText(_translate("MainWindow", "Общая информация о профиле"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Список для чтения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Общая статистика библиотеки"))
        self.actionuil.setText(_translate("MainWindow", "uil"))
        self.action.setText(_translate("MainWindow", "помошь"))
        self.action_2.setText(_translate("MainWindow", "уцкакуап"))
        self.action_3.setText(_translate("MainWindow", "укпкупку"))
