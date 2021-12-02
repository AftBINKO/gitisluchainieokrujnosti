from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 240, 320)
        self.setWindowTitle('Git и случайные окружности')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(70, 280)
