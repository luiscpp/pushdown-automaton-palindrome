from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor,QBrush,QPen,QFont

class State(QtWidgets.QGraphicsItem):
    def __init__(self,name):
        QtWidgets.QGraphicsItem.__init__(self)
        self.name = name
        self.acceptanceStatus = False
        self.color = QColor(40,20,90)
        #self.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable)

    def boundingRect(self):
        return QtCore.QRectF(0,0,100,100)

    def paint(self, painter, option, widget):
        pen = QPen(QtCore.Qt.black)
        pen.setWidth(4)
        painter.setPen(pen)
        brush = QBrush(self.color)
        painter.setBrush(brush)
        if(self.acceptanceStatus == True):
            painter.drawEllipse(0,0,100,100)
            painter.drawEllipse(15,15,70,70)
            font = QFont("Times New Roman",40)
            painter.setFont(font)
            painter.drawText(42, 63, self.name);
        else:
            painter.drawEllipse(0,0,100,100)
            font = QFont("Times New Roman",40)
            painter.setFont(font)
            painter.drawText(40, 55, self.name);
