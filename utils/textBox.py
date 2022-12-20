import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class TextBox(QWidget):

    def __init__(self):
        super(TextBox, self).__init__()
        self.setGeometry(800, 300, 200, 100)
        self.setWindowTitle("MyGLDrawer")
        self.d_value = 50.0
        self.okClicked = False
        self.r = QLabel("Insira o afastamento entre particulas:")

        self.boxR = QLineEdit() 

        self.b1 = QPushButton("Confirmar")
        
        self.vbox = QVBoxLayout()

        self.vbox.addWidget(self.r)
        self.vbox.addWidget(self.boxR)
        self.vbox.addWidget(self.b1)

        self.setLayout(self.vbox)

        self.boxR.setText(str(self.d_value))
        self.b1.clicked.connect(self.onConfClicked)
    
    def onConfClicked(self):
        try:
            self.d_value = float(self.boxR.text())
        except:
            self.d_value = 50.0
        self.okClicked = True
        self.boxR.setText(str(self.d_value))
        self.close()
        

