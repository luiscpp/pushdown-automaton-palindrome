# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automaton.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1200, 700)
        Widget.setMinimumSize(QtCore.QSize(1200, 700))
        Widget.setMaximumSize(QtCore.QSize(1200, 700))
        self.graphicsView = QtWidgets.QGraphicsView(Widget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.graphicsView.setObjectName("graphicsView")
        self.input = QtWidgets.QPlainTextEdit(Widget)
        self.input.setGeometry(QtCore.QRect(1020, 150, 161, 31))
        self.input.setObjectName("input")
        self.evaluate = QtWidgets.QPushButton(Widget)
        self.evaluate.setGeometry(QtCore.QRect(1060, 200, 87, 29))
        #self.evaluate.setCheckable(False)
        self.evaluate.setObjectName("evaluate")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "PushdownAutomaton"))
        self.evaluate.setText(_translate("Widget", "Evaluar"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())'''