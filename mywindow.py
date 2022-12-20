from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from utils.textBox import TextBox
from utils.contornoBox import ContornoBox
from utils.jsonBox import JsonBox
from mycanvas import *
from mymodel import *
import sys

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(600,200,600,400)
        self.setWindowTitle("MyGLDrawer")
        self.textBox = TextBox()
        self.contornoBox = ContornoBox()
        self.canvas = MyCanvas(self.textBox, self.contornoBox)
        self.setCentralWidget(self.canvas)
        # create a model object and pass to canvas
        self.model = MyModel()
        self.canvas.setModel(self.model)
        self.jsonBox = JsonBox(self.canvas.model)

        # create a Toolbar
        tb = self.addToolBar("File")

        # add fit
        fit = QAction(QIcon(r"icons\fit.png"),"fit",self)
        tb.addAction(fit)

        # add pan
        pan = QAction(QIcon(r"icons\pan.png"),"pan",self)
        pan.setCheckable(True)
        tb.addAction(pan)

        # add insertText
        boxText = QAction(QIcon(r"icons\radius.png"),"particulas",self)
        tb.addAction(boxText)

        # add insertText
        fence = QAction(QIcon(r"icons\pontilhado.png"),"makeFence",self)
        fence.setCheckable(True)
        tb.addAction(fence)
        self.countFenceClick = 0

        # add insertText
        saveJson = QAction(QIcon(r"icons\json.png"),"saveJson",self)
        tb.addAction(saveJson)

        tb.actionTriggered[QAction].connect(self.tbpressed)


    def tbpressed(self,action):
        if action.text() == "fit":
            self.canvas.fitWorldToViewport()
        elif action.text() == "pan":
            self.canvas.isPanAllowed = not self.canvas.isPanAllowed
        elif action.text() == "particulas":
            self.textBox.show()
        elif action.text() == "makeFence":
            self.countFenceClick += 1
            self.canvas.isFenceColectorOn = not self.canvas.isFenceColectorOn

            if self.countFenceClick == 2:
                self.contornoBox.show()
                self.countFenceClick = 0

        elif action.text() == "saveJson":
            self.jsonBox.show()