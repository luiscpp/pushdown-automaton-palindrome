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

        self.label = QtWidgets.QLabel(Widget)
        self.label.setText("Pila")
        self.label.setGeometry(QtCore.QRect(1060, 647, 80, 30))
        self.label.setStyleSheet("border:1px solid;font-size:30px;font-style:italic;color:black;background-color:rgb(90,80,20);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;padding-left:9px;")


        self.label = QtWidgets.QLabel(Widget)
        self.label.setText("Entrada")
        self.label.setGeometry(QtCore.QRect(1046, 114, 110, 30))
        self.label.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(90,80,20);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;padding-left:6px;")

        self.resultLabel = QtWidgets.QLabel(Widget)
        self.resultLabel.setVisible(False)
        self.resultLabel.setText("")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setGeometry(QtCore.QRect(1005, 340, 190, 30))
        self.resultLabel.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(90,80,20);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;")        

        self.tableWidget = QtWidgets.QTableWidget(Widget)
        self.tableWidget.setGeometry(QtCore.QRect(1045, 390, 110, 250))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()#Agregando Item
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item) 

        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.input = QtWidgets.QPlainTextEdit(Widget)
        self.input.setGeometry(QtCore.QRect(1020, 150, 161, 31))
        self.input.setObjectName("input")
        self.slowButton = QtWidgets.QPushButton(Widget)
        self.slowButton.setGeometry(QtCore.QRect(1060, 188, 87, 29))
        self.slowButton.setObjectName("slowButton")

        self.fastButton = QtWidgets.QPushButton(Widget)
        self.fastButton.setGeometry(QtCore.QRect(1060, 223, 87, 29))
        self.fastButton.setObjectName("fastButton")

        self.arrowLabel = QtWidgets.QLabel(Widget)
        self.arrowLabel.setGeometry(QtCore.QRect(146, 397, 71, 61))#146 #507 #868
        self.arrowLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.arrowLabel.setText("")
        self.arrowLabel.setPixmap(QtGui.QPixmap("resources/arrow.png"))
        self.arrowLabel.setObjectName("arrowLabel")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "PushdownAutomaton"))

        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Widget", "f1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Widget", "c1"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        font = QtGui.QFont()
        font.setPointSize(23)
        item.setFont(font)
        item.setText(_translate("Widget", "#"))

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.slowButton.setText(_translate("Widget", "Paso a paso"))
        self.fastButton.setText(_translate("Widget", "Rápido"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())'''