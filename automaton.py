from automaton_ui import *
import time
from scene import *
from state import *
from transition import *
from text import *
from stack import *

ACTUAL_STATE = 0
NEXT_STATE = 1
READ = 2
POP = 3
PUSH = 4

class Automaton(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.evaluate.clicked.connect(self.evaluateWord)
        self.transitionMatrix = []
        self.initializeMatrix()
        self.states = []
        self.transitions = []
        self.stack = Stack()
        self.actualState = "p"
        self.count = 0
        self.initializeAutomatom()

    def getTransition(self,start,end):
        for i in range(len(self.transitions)):
            if(self.transitions[i].start == start and self.transitions[i].end == end):
                return self.transitions[i]
        return False                

    def getText(self,texts,read,pop,push):
        for j in range(len(texts)):
            if(texts[j].read == read and texts[j].pop == pop and texts[j].push == push):
                return texts[j]
        return False                

    def getState(self,name):
        for i in range(len(self.states)):
            if(self.states[i].name == name):
                return self.states[i]
        return False                

    def activateColors(self,start,end,read,pop,push):#HERE
        transition = self.getTransition(start,end)
        text = self.getText(transition.transitionsTexts,read,pop,push)
        state = self.getState(end)
        
        text.activate()
        transition.activate()
        state.activate()

    '''def activateColors(self,start,end,read,pop,push):
        for i in range(len(self.transitions)):
            if(self.transitions[i].start == start and self.transitions[i].end == end):
                transition = self.transitions[i]
                for j in range(len(self.transitions[i].transitionsTexts)):
                    if(self.transitions[i].transitionsTexts[j].read == read and self.transitions[i].transitionsTexts[j].pop == pop and self.transitions[i].transitionsTexts[j].push == push):
                        self.transitions[i].transitionsTexts[j].activate()
                        break
                break                        
        transition.activate()'''
        
    def evaluateTransition(self,actualState,read,pop):
        row = []
        for i in range(12):
            for j in range(5):
                row.append(self.transitionMatrix[i][j])

            if(row[ACTUAL_STATE] == actualState and row[READ] == read and row[POP] == pop):
                self.count = self.count -1 
                print("actual: ",row[ACTUAL_STATE])
                print("siguiente: ",row[NEXT_STATE])
                print("lee: ",row[READ])
                print("saca: ",row[POP])
                print("mete: ",row[PUSH])
                self.actualState = row[NEXT_STATE]
                self.activateColors(row[ACTUAL_STATE],row[NEXT_STATE],row[READ],row[POP],row[PUSH])

                if(row[POP] != 'lambda'):
                    self.stack.elements.pop()
                push = row[PUSH]#Caracteres a meter en la pila
                
                if(row[PUSH] != 'lambda'):
                    for k in range(len(push)):
                        self.stack.elements.append(push[k])

                print("\npila (alreves):\n")
                for k in range(len(self.stack.elements)):#imprime los elementos de la pila
                    print("-",self.stack.elements[k])
                break                 
            else:
                row.clear()

    def restart(self):
        self.stack.restart()
        self.actualState = "p"
        self.count = 0

    def evaluateWord(self):
        self.restart()
        self.ui.evaluate.setEnabled(False)
        word = self.ui.input.toPlainText()
        if((len(word) % 2) == 0):
            print("La cantidad de caracteres debe ser impar")
        else:
            self.count = len(word)
            for i in range(len(word)):
                top = self.stack.elements.pop()
                print("\ntransicion:\n")
                print("tope:",top)
                self.stack.elements.append(top)
                character = word[i]
                self.evaluateTransition(self.actualState,character,top)

            top = self.stack.elements.pop()
            self.stack.elements.append(top)
            
            if(self.actualState == 'q' and top == '#'):
                if(self.count == 0):
                    print("\ntransicion:\n")
                    print("tope:",top)
                    self.evaluateTransition('q','lambda','#')
                    print("ES PALINDROMA")
                else:
                    print("NO ES")
            else:  
                print("NO ES")
        self.ui.evaluate.setEnabled(True)                                  

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
        transitionQR.transitionsTexts.append(text12)
        self.scene.addItem(text12)
        self.scene.addItem(transitionQR)
        self.transitions.append(transitionQR)

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
    widget.printMatrix()
    widget.show()
    sys.exit(app.exec_())
    #time.sleep(5)
    