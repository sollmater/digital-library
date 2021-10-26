import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('authorization.ui', self)
        self.pushButton.clicked.connect(self.password)
        self.pushButton_2.clicked.connect(self.registr)

    def password(self):
        uic.loadUi('main_window.ui', self)

    def registr(self):
        uic.loadUi('registration.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
