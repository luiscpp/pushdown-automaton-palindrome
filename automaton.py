from automaton_ui import *
import time
from scene import *
from state import *
from transition import *
from text import *
from stack import *
from gtts import gTTS
import os 

ACTUAL_STATE = 0
NEXT_STATE = 1
READ = 2
POP = 3
PUSH = 4

LANGUAGE = 'es-es'

class Automaton(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.slowButton.clicked.connect(self.stepByStep)
        self.ui.fastButton.clicked.connect(self.fast)
        self.transitionMatrix = []
        self.initializeMatrix()
        self.states = []
        self.transitions = []
        self.stack = Stack()
        self.actualState = "p"
        self.count = 0
        self.initializeAutomatom()
        self.breakProcess = False

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


    def pushStack(self,element):
        rows = self.ui.tableWidget.rowCount()
        rows = rows+1
        self.ui.tableWidget.setRowCount(rows)

        item = QtWidgets.QTableWidgetItem()
        self.ui.tableWidget.setVerticalHeaderItem(rows-1, item) 

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.ui.tableWidget.setItem(rows-1, 0, item)

        _translate = QtCore.QCoreApplication.translate

        item = self.ui.tableWidget.item(rows-1, 0)
        item.setText(_translate("Widget", element))

        e=[]
        max = rows-1

        e.append(self.ui.tableWidget.item(max, 0).text())

        for i in range(max):
            e.append(self.ui.tableWidget.item(i, 0).text())

        for i in range(rows):
            item = self.ui.tableWidget.item(i, 0) 
            font = QtGui.QFont()
            font.setPointSize(23)
            item.setFont(font) 
            item.setText(_translate("Widget", e[i]))


    def popStack(self):        
        rowsBefore = self.ui.tableWidget.rowCount()
        rowAfter = rowsBefore-1
        e = []
        for i in range(1,rowsBefore):
            e.append(self.ui.tableWidget.item(i, 0).text())

        self.ui.tableWidget.setRowCount(rowAfter) 
        _translate = QtCore.QCoreApplication.translate

        for i in range(rowAfter):
            item = self.ui.tableWidget.item(i, 0)  
            font = QtGui.QFont()
            font.setPointSize(23)
            item.setFont(font)
            item.setText(_translate("Form", e[i]))

    def restart(self):
        self.breakProcess = False
        self.ui.tableWidget.setRowCount(1)
        _translate = QtCore.QCoreApplication.translate
        item = self.ui.tableWidget.item(0, 0)
        font = QtGui.QFont()
        font.setPointSize(23)
        item.setFont(font)
        item.setText(_translate("Widget", "#"))#SOLUCIONAR QUE SE VEA LA PILA CON SOLO EL #
    
        self.ui.arrowLabel.setGeometry(QtCore.QRect(146, 397, 71, 61))#Indica el estado P
        self.stack = Stack()
        self.actualState = "p"
        self.count = 0

    def fixTextSpeak(self,pushText):
        fixedText = pushText
        if(len(pushText)>1 and pushText != 'lambda'):
            fixedText = pushText[0] + " y "+pushText[1]
        return fixedText

    def speakTransition(self,read,pop,push):
        push = self.fixTextSpeak(push)           

        if(push == 'lambda'):
            myText = "lee "+read+", desapila "+pop+" y no apila nada"
        elif(read == 'lambda'):
            myText = "no lee nada, desapila "+pop+" y apila "+push
        else:            
            myText = "lee "+read+", desapila "+pop+" y apila "+push

        myobj = gTTS(text=myText, lang=LANGUAGE, slow=False) 
        myobj.save("transition.mp3") 
        os.system("mpg321 transition.mp3")

    def speakIsPalindrome(self):
        os.system("mpg321 palindrome.mp3")

    def speakNoPalindrome(self):
        os.system("mpg321 noPalindrome.mp3")

    def speakInvalidPairString(self):
        os.system("mpg321 invalidPair.mp3")
    
    def speakInvalidString(self):
        os.system("mpg321 invalidString.mp3")

    def speakNextState(self,start,end):
        if(start != end):
            myText = "pasa al siguiente estado "+end
            myobj = gTTS(text=myText, lang=LANGUAGE, slow=False) 
            myobj.save("state.mp3") 
            os.system("mpg321 state.mp3")
        else:
            myText = "se mantiene en el estado "+start
            myobj = gTTS(text=myText, lang=LANGUAGE, slow=False) 
            myobj.save("state.mp3") 
            os.system("mpg321 state.mp3")       

    def activateColorsSlow(self,start,end,read,pop,push):#HERE
        transition = self.getTransition(start,end)
        text = self.getText(transition.transitionsTexts,read,pop,push)
        state = self.getState(end)
        
        self.speakTransition(read,pop,push)
        text.activateSlow()       

        transition.activateSlow()
        self.speakNextState(start,end)

        if(self.actualState == 'p'):
            self.ui.arrowLabel.setGeometry(QtCore.QRect(146, 397, 71, 61))
        elif(self.actualState == 'q'):
            self.ui.arrowLabel.setGeometry(QtCore.QRect(507, 397, 71, 61))
        else:
            self.ui.arrowLabel.setGeometry(QtCore.QRect(868, 397, 71, 61))

        state.activateSlow()

    def evaluateTransitionSlow(self,actualState,read,pop):
        row = []
        self.breakProcess = True
        for i in range(12):
            for j in range(5):
                row.append(self.transitionMatrix[i][j])

            if(row[ACTUAL_STATE] == actualState and row[READ] == read and row[POP] == pop):
                self.breakProcess = False
                self.count = self.count -1 
                print("actual: ",row[ACTUAL_STATE])
                print("siguiente: ",row[NEXT_STATE])
                print("lee: ",row[READ])
                print("saca: ",row[POP])
                print("mete: ",row[PUSH])
                self.actualState = row[NEXT_STATE]

                if(row[POP] != 'lambda'):
                    self.stack.elements.pop()
                    self.popStack() #Sacar el tope de la pila grafica
                push = row[PUSH]#Caracteres a meter en la pila
                
                if(row[PUSH] != 'lambda'):
                    for k in range(len(push)):
                        self.stack.elements.append(push[k])
                        self.pushStack(push[k])                   

                self.activateColorsSlow(row[ACTUAL_STATE],row[NEXT_STATE],row[READ],row[POP],row[PUSH])                        

                print("\npila (alreves):\n")
                for k in range(len(self.stack.elements)):#imprime los elementos de la pila
                    print("-",self.stack.elements[k])
                break                 
            else:
                row.clear() 

    def isValidateString(self,word):
        for i in range(len(word)):
            if(word[i] != 'a' and word[i] != 'b' and word[i] != 'c'):
                return False
        return True   

    def speakNoTransitionsAvailable(self):
        os.system("mpg321 noTransitionsAvailable.mp3")

    def stepByStep(self):        
        self.restart()
        self.ui.slowButton.setEnabled(False)
        self.ui.fastButton.setEnabled(False) 

        word = self.ui.input.toPlainText()
        word = word.lower() #Para aceptar entradas en mayusculas

        if(self.isValidateString(word)):
            if((len(word) % 2) == 0):
                self.ui.resultLabel.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(120,0,0);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;")        
                self.ui.resultLabel.setText("Cadena par")
                self.ui.resultLabel.setVisible(True)
                self.speakInvalidPairString()
                QtCore.QTimer.singleShot(3000, self.ui.resultLabel.hide)
            else:
                self.count = len(word)
                i=0
                while(i<len(word) and self.breakProcess == False):
                    top = self.stack.elements.pop()
                    print("\ntransicion:\n")
                    print("tope:",top)
                    self.stack.elements.append(top)
                    character = word[i]
                    self.evaluateTransitionSlow(self.actualState,character,top)
                    i = i+1

                if(self.breakProcess == True):
                    self.speakNoTransitionsAvailable()

                top = self.stack.elements.pop()
                self.stack.elements.append(top)
                
                if(self.actualState == 'q' and top == '#'):
                    if(self.count == 0):
                        print("\ntransicion:\n")
                        print("tope:",top)
                        self.evaluateTransitionSlow('q','lambda','#')
                        self.ui.resultLabel.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(0,80,30);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;")        
                        self.ui.resultLabel.setText("Palindroma")
                        self.ui.resultLabel.setVisible(True)
                        self.speakIsPalindrome()
                        QtCore.QTimer.singleShot(3000, self.ui.resultLabel.hide)                        
                        print("ES PALINDROMA")
                    else:
                        self.ui.resultLabel.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(120,0,0);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;")        
                        self.ui.resultLabel.setText("No Palindroma")
                        self.ui.resultLabel.setVisible(True)
                        self.speakNoPalindrome()
                        QtCore.QTimer.singleShot(3000, self.ui.resultLabel.hide)
                else:  
                    self.ui.resultLabel.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(120,0,0);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;")        
                    self.ui.resultLabel.setText("No Palindroma")
                    self.ui.resultLabel.setVisible(True)
                    self.speakNoPalindrome()
                    QtCore.QTimer.singleShot(3000, self.ui.resultLabel.hide)
        else:
            self.ui.resultLabel.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(120,0,0);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;")        
            self.ui.resultLabel.setText("Invalido")
            self.ui.resultLabel.setVisible(True)
            self.speakInvalidString()
            QtCore.QTimer.singleShot(3000, self.ui.resultLabel.hide)
        self.ui.slowButton.setEnabled(True) 
        self.ui.fastButton.setEnabled(True) 


    def activateColorsFast(self,start,end,read,pop,push):#HERE
        transition = self.getTransition(start,end)
        text = self.getText(transition.transitionsTexts,read,pop,push)
        state = self.getState(end)
        
        text.activateFast()
        transition.activateFast()

        if(self.actualState == 'p'):
            self.ui.arrowLabel.setGeometry(QtCore.QRect(146, 397, 71, 61))
        elif(self.actualState == 'q'):
            self.ui.arrowLabel.setGeometry(QtCore.QRect(507, 397, 71, 61))
        else:
            self.ui.arrowLabel.setGeometry(QtCore.QRect(868, 397, 71, 61))

        state.activateFast()

    def evaluateTransitionFast(self,actualState,read,pop):
        self.breakProcess = True
        row = []
        for i in range(12):
            for j in range(5):
                row.append(self.transitionMatrix[i][j])

            if(row[ACTUAL_STATE] == actualState and row[READ] == read and row[POP] == pop):
                self.breakProcess = False
                self.count = self.count -1 
                print("actual: ",row[ACTUAL_STATE])
                print("siguiente: ",row[NEXT_STATE])
                print("lee: ",row[READ])
                print("saca: ",row[POP])
                print("mete: ",row[PUSH])
                self.actualState = row[NEXT_STATE]
                
                if(row[POP] != 'lambda'):
                    self.stack.elements.pop()
                    self.popStack() #Sacar el tope de la pila grafica
                push = row[PUSH]#Caracteres a meter en la pila
                
                if(row[PUSH] != 'lambda'):
                    for k in range(len(push)):
                        self.stack.elements.append(push[k])
                        self.pushStack(push[k])                   

                self.activateColorsFast(row[ACTUAL_STATE],row[NEXT_STATE],row[READ],row[POP],row[PUSH])                        

                print("\npila (alreves):\n")
                for k in range(len(self.stack.elements)):#imprime los elementos de la pila
                    print("-",self.stack.elements[k])
                break                 
            else:
                row.clear()           

    def fast(self):
        self.restart()
        self.ui.slowButton.setEnabled(False)
        self.ui.fastButton.setEnabled(False)
        word = self.ui.input.toPlainText()
        word = word.lower() #Para aceptar entradas en mayusculas

        if(self.isValidateString(word)):
            if((len(word) % 2) == 0):
                self.ui.resultLabel.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(120,0,0);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;")        
                self.ui.resultLabel.setText("Cadena par")
                self.ui.resultLabel.setVisible(True)
                QtCore.QTimer.singleShot(3000, self.ui.resultLabel.hide)
            else:                
                self.count = len(word)
                i=0
                while(i<len(word) and self.breakProcess == False):
                    top = self.stack.elements.pop()
                    print("\ntransicion:\n")
                    print("tope:",top)
                    self.stack.elements.append(top)
                    character = word[i]
                    self.evaluateTransitionFast(self.actualState,character,top)
                    i = i+1

                top = self.stack.elements.pop()
                self.stack.elements.append(top)
                
                if(self.actualState == 'q' and top == '#'):
                    if(self.count == 0):
                        print("\ntransicion:\n")
                        print("tope:",top)
                        self.evaluateTransitionFast('q','lambda','#')
                        self.ui.resultLabel.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(0,80,30);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;")        
                        self.ui.resultLabel.setText("Palindroma")
                        self.ui.resultLabel.setVisible(True)
                        QtCore.QTimer.singleShot(3000, self.ui.resultLabel.hide)#espera 1 seg para ejecutar el metodo changeColor
                        print("ES PALINDROMA")
                    else:
                        self.ui.resultLabel.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(120,0,0);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;")        
                        self.ui.resultLabel.setText("No Palindroma")
                        self.ui.resultLabel.setVisible(True)
                        QtCore.QTimer.singleShot(3000, self.ui.resultLabel.hide)
                        print("NO ES")
                else:  
                    self.ui.resultLabel.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(120,0,0);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;")        
                    self.ui.resultLabel.setText("No Palindroma")
                    self.ui.resultLabel.setVisible(True)
                    QtCore.QTimer.singleShot(3000, self.ui.resultLabel.hide)
                    print("NO ES")
        else:
            self.ui.resultLabel.setStyleSheet("border:1px solid;font-size:25px;font-style:italic;color:black;background-color:rgb(120,0,0);border-top-right-radius:20px;border-bottom-left-radius:20px;border-top-left-radius:4px;border-bottom-right-radius:4px;")        
            self.ui.resultLabel.setText("Invalido")
            self.ui.resultLabel.setVisible(True)
            QtCore.QTimer.singleShot(3000, self.ui.resultLabel.hide)

        self.ui.slowButton.setEnabled(True)  
        self.ui.fastButton.setEnabled(True)             


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