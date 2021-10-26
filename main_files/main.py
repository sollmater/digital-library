import sys


from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('authorization.ui', self)
        self.pushButton.clicked.connect(self.check_password)
        self.pushButton_2.clicked.connect(self.check_password)

    def check_password(self):
        uic.loadUi('main_window.ui', self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())