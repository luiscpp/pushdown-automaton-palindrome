from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor,QBrush,QPen,QFont

class Stack():
    def __init__(self):
        self.elements = []
        self.elements.append('#')

    def restart(self):
        self.elements.clear()
        self.elements.append('#')
