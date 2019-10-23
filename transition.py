from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor,QBrush,QPen,QFont
import time

class Transition(QtWidgets.QGraphicsItem):
    def __init__(self,start,end):
        QtWidgets.QGraphicsItem.__init__(self)
        self.transitionsTexts = []
        self.start = start
        self.end = end
        self.arc = False
        self.color = QtCore.Qt.black
        #self.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable)

    def boundingRect(self):
        if(self.arc):
            return QtCore.QRectF(0,0,100,100)
        else:
            return QtCore.QRectF(0,0,250,50)

    def paint(self, painter, option, widget):
        pen = QPen(self.color)
        pen.setWidth(6)
        painter.setPen(pen)
        if(self.arc):
            painter.drawArc(0,0,100,100,-16*70,16*300)
            painter.drawLine(20,90,20,78)
            painter.drawLine(20,90,8,90)
        else:
            painter.drawLine(0,25,249,25)
            painter.drawLine(250,25,240,15)
            painter.drawLine(250,25,240,35)

    def changeColor(self):
        self.color = QtCore.Qt.black
        
    def activate(self):
        self.color = QColor(90,40,55)
        QtWidgets.QApplication.processEvents() #Para que los eventos tengan preferencia
        #time.sleep(1)
        self.color = QtCore.Qt.black     