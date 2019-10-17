from automaton_ui import *
from scene import *
from state import *
from transition import *
from text import *

class Automaton(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.transitionMatrix = []
        self.states = []
        self.transitions = []
        self.initializeAutomatom()

    def initializeAutomatom(self):
        self.scene = Scene()

        #AGRAGANDO LOS ESTADOS A LA ESCENA
        stateP = State("p")
        stateP.setPos(130,300)
        self.states.append(stateP)
        self.scene.addItem(stateP)

        stateQ = State("q")
        stateQ.setPos(491,300)
        self.states.append(stateQ)
        self.scene.addItem(stateQ)

        stateR = State("r")
        stateR.setPos(852,300)
        stateR.acceptanceStatus = True
        self.states.append(stateR)
        self.scene.addItem(stateR)

        #AGREGANDO LAS TRANSICIONES A LA ESCENA
        transitionPP = Transition("p","p")
        transitionPP.setPos(130,205)
        transitionPP.arc = True
        text1 = Text("a","#","#a")
        text1.setPos(15,280)
        self.scene.addItem(text1)
        transitionPP.transitionsTexts.append(text1)
        text2 = Text("b","#","#b")
        text2.setPos(15,235)
        self.scene.addItem(text2)
        transitionPP.transitionsTexts.append(text2)
        text3 = Text("a","a","aa")
        text3.setPos(15,190)
        self.scene.addItem(text3)
        transitionPP.transitionsTexts.append(text3)
        text4 = Text("b","a","ab")
        text4.setPos(15,145)
        self.scene.addItem(text4)
        transitionPP.transitionsTexts.append(text4)
        text5 = Text("a","b","ba")
        text5.setPos(15,100)
        self.scene.addItem(text5)
        transitionPP.transitionsTexts.append(text5)
        text6 = Text("b","b","bb")
        text6.setPos(15,55)
        self.scene.addItem(text6)
        transitionPP.transitionsTexts.append(text6)
        self.scene.addItem(transitionPP)
        self.transitions.append(transitionPP)

        transitionPQ = Transition("p","q")
        transitionPQ.setPos(235,325)
        text7 = Text("c","a","a")
        text7.setPos(310,295)
        self.scene.addItem(text7)
        transitionPQ.transitionsTexts.append(text7)
        text8 = Text("c","b","b")
        text8.setPos(310,250)
        self.scene.addItem(text8)
        transitionPQ.transitionsTexts.append(text8)
        text9 = Text("c","#","#")
        text9.setPos(310,205)
        self.scene.addItem(text9)
        transitionPQ.transitionsTexts.append(text9)
        self.scene.addItem(transitionPQ)
        self.transitions.append(transitionPQ)

        transitionQQ = Transition("q","q")
        transitionQQ.setPos(491,205)
        transitionQQ.arc = True
        text10 = Text("a","a","lambda")
        text10.setPos(490,150)
        self.scene.addItem(text10)
        transitionQQ.transitionsTexts.append(text10)
        text11 = Text("b","b","lambda")
        text11.setPos(490,105)
        self.scene.addItem(text11)
        transitionQQ.transitionsTexts.append(text11)
        self.scene.addItem(transitionQQ)
        self.transitions.append(transitionQQ)

        transitionQR = Transition("q","r")
        transitionQR.setPos(596,325)
        text12 = Text("lambda","#","#")
        text12.setPos(650,295)
        self.scene.addItem(text12)
        self.scene.addItem(transitionQR)
        transitionQR.transitionsTexts.append(text12)

        self.ui.graphicsView.setScene(self.scene)

    def printMatrix(self):
        for i in range(12):
            for j in range(5):
                print("[",self.transitionMatrix[i][j],"]",end="")
            print("")

    def initializeMatrix(self):
        for i in range(12):
            a=[""]*5
            self.transitionMatrix.append(a)

        self.transitionMatrix[0][0] = "p"
        self.transitionMatrix[0][1] = "p"
        self.transitionMatrix[0][2] = "b"
        self.transitionMatrix[0][3] = "b"
        self.transitionMatrix[0][4] = "bb"

        self.transitionMatrix[1][0] = "p"
        self.transitionMatrix[1][1] = "p"
        self.transitionMatrix[1][2] = "a"
        self.transitionMatrix[1][3] = "b"
        self.transitionMatrix[1][4] = "ba"

        self.transitionMatrix[2][0] = "p"
        self.transitionMatrix[2][1] = "p"
        self.transitionMatrix[2][2] = "b"
        self.transitionMatrix[2][3] = "a"
        self.transitionMatrix[2][4] = "ab"

        self.transitionMatrix[3][0] = "p"
        self.transitionMatrix[3][1] = "p"
        self.transitionMatrix[3][2] = "a"
        self.transitionMatrix[3][3] = "a"
        self.transitionMatrix[3][4] = "aa"

        self.transitionMatrix[4][0] = "p"
        self.transitionMatrix[4][1] = "p"
        self.transitionMatrix[4][2] = "b"
        self.transitionMatrix[4][3] = "#"
        self.transitionMatrix[4][4] = "#b"

        self.transitionMatrix[5][0] = "p"
        self.transitionMatrix[5][1] = "p"
        self.transitionMatrix[5][2] = "a"
        self.transitionMatrix[5][3] = "#"
        self.transitionMatrix[5][4] = "#a"

        self.transitionMatrix[6][0] = "p"
        self.transitionMatrix[6][1] = "q"
        self.transitionMatrix[6][2] = "c"
        self.transitionMatrix[6][3] = "#"
        self.transitionMatrix[6][4] = "#"

        self.transitionMatrix[7][0] = "p"
        self.transitionMatrix[7][1] = "q"
        self.transitionMatrix[7][2] = "c"
        self.transitionMatrix[7][3] = "b"
        self.transitionMatrix[7][4] = "b"

        self.transitionMatrix[8][0] = "p"
        self.transitionMatrix[8][1] = "q"
        self.transitionMatrix[8][2] = "c"
        self.transitionMatrix[8][3] = "a"
        self.transitionMatrix[8][4] = "a"

        self.transitionMatrix[9][0] = "q"
        self.transitionMatrix[9][1] = "q"
        self.transitionMatrix[9][2] = "b"
        self.transitionMatrix[9][3] = "b"
        self.transitionMatrix[9][4] = "lambda"

        self.transitionMatrix[10][0] = "q"
        self.transitionMatrix[10][1] = "q"
        self.transitionMatrix[10][2] = "a"
        self.transitionMatrix[10][3] = "a"
        self.transitionMatrix[10][4] = "lambda"

        self.transitionMatrix[11][0] = "q"
        self.transitionMatrix[11][1] = "r"
        self.transitionMatrix[11][2] = "lambda"
        self.transitionMatrix[11][3] = "#"
        self.transitionMatrix[11][4] = "#"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Automaton()
    widget.initializeMatrix()
    #widget.printMatrix()
    widget.show()
    sys.exit(app.exec_())