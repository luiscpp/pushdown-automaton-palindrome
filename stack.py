from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor,QBrush,QPen,QFont

class Stack(QtWidgets.QGraphicsItem):
    def __init__(self):
        QtWidgets.QGraphicsItem.__init__(self)
        self.elements = []
        self.elements.append('#')
        self.color = QColor(40,20,90)
        #self.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable)

    def restart(self):
        self.elements.clear()
        self.elements.append('#')
        self.color = QColor(40,20,90)
