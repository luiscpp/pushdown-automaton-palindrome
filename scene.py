from PyQt5 import QtWidgets, QtCore
from state import *
from transition import *
from text import *

class Scene(QtWidgets.QGraphicsScene):
    def __init__(self):
        QtWidgets.QGraphicsScene.__init__(self)
        self.setSceneRect(0,0,990,690)

        self.top = QtCore.QLineF(self.sceneRect().topLeft(),self.sceneRect().topRight())
        self.bottom = QtCore.QLineF(self.sceneRect().bottomLeft(),self.sceneRect().bottomRight())
        self.left = QtCore.QLineF(self.sceneRect().topLeft(),self.sceneRect().bottomLeft())
        self.right = QtCore.QLineF(self.sceneRect().topRight(),self.sceneRect().bottomRight())

        self.addLine(self.top)
        self.addLine(self.bottom)
        self.addLine(self.left)
        self.addLine(self.right)