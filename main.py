import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from UI import Ui_Form
import random


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Кружочки')
        self.paint = 0
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.paint = 1
        self.update()

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()

            qp.begin(self)
            self.draw(qp)

            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x, y = random.randint(20, 400), random.randint(20, 400)
        wh = random.randint(20, 400)
        qp.drawEllipse(x, y, wh, wh)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
