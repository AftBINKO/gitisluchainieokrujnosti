import sys

from random import randrange
from ui import Example
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Window(Example):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        for i in range(randrange(10)):
            qp.setBrush(QColor(randrange(256), randrange(256), randrange(256)))
            a, b = randrange(240), randrange(320)
            qp.drawEllipse(a, a, b, b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
