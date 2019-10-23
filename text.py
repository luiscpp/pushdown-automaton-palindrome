from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor,QBrush,QPen,QFont
import time

class Text(QtWidgets.QGraphicsItem):
    def __init__(self,read,pop,push):
        QtWidgets.QGraphicsItem.__init__(self)
        self.read = read
        self.pop = pop
        self.push = push
        self.color = QColor(90,80,20)
        #self.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable)

    def boundingRect(self):
        return QtCore.QRectF(0,0,100,40)

    def paint(self, painter, option, widget):
        pen = QPen(QtCore.Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)
        brush = QBrush(self.color)
        painter.setBrush(brush)
        font = QFont("Times New Roman",25)
        painter.setFont(font)
        painter.drawRect(0,0,100,40)
        if(self.read == 'lambda'):
            painter.drawText(10,30,'λ'+","+self.pop+"/"+self.push)
        elif(self.push == 'lambda'):
            painter.drawText(10,30,self.read+","+self.pop+"/"+'λ')
        else:    
            painter.drawText(10,30,self.read+","+self.pop+"/"+self.push)

    def changeColor(self):
        self.color = QColor(90,80,20)
        
    def activate(self):
        self.color = QColor(90,40,55)
        QtWidgets.QApplication.processEvents() #Para que los eventos tengan preferencia
        #time.sleep(1)
        self.color = QColor(90,80,20)