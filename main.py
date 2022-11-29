import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from random import randint


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Git')
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp, self.event)
            qp.end()
            self.do_paint = False
            self.keypr = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp, event):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(3):
            qp.drawEllipse(randint(0, 400), randint(0, 400), randint(10, 150), randint(10, 150))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
