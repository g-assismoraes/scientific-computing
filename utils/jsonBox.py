import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class JsonBox(QWidget):

    def __init__(self, model):
        super(JsonBox, self).__init__()
        self.setGeometry(800, 300, 200, 100)
        self.setWindowTitle("MyGLDrawer")
        self.okClicked = False
        self.model = model

        self.N = 600
        self.kspr = 210000000000.0
        self.mass = 7850
        self.h = 0.00004

        self.label = QLabel("Entre com os valores em caso de elementos discretos: ")
        self.N_label = QLabel("Digite N: ")
        self.mass_label = QLabel("Digite o valor de massa: ")
        self.kspr_label = QLabel("Digite o valor de kspr: ")
        self.h_label = QLabel("Digite o valor de h: ")

        self.boxN = QLineEdit() 
        self.boxMass = QLineEdit() 
        self.boxKSPR = QLineEdit() 
        self.boxH = QLineEdit()

        self.b1 = QPushButton("Confirmar")
        
        self.vbox = QVBoxLayout()

        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.N_label)
        self.vbox.addWidget(self.boxN)
        self.vbox.addWidget(self.mass_label)
        self.vbox.addWidget(self.boxMass)
        self.vbox.addWidget(self.kspr_label)
        self.vbox.addWidget(self.boxKSPR)
        self.vbox.addWidget(self.h_label)
        self.vbox.addWidget(self.boxH)
        self.vbox.addWidget(self.b1)

        self.setLayout(self.vbox)

        self.b1.clicked.connect(self.onConfClicked)
    
    def onConfClicked(self):
        try:
            self.N = int(self.boxN.text())
            self.mass = float(self.boxMass.text())
            self.kspr = float(self.boxKSPR.text())
            self.h = float(self.boxH.text())
        except:
            self.N = 600
            self.kspr = 210000000000.0
            self.mass = 7850
            self.h = 0.00004

        self.model.saveMesh(self.N, self.mass, self.kspr, self.h)
        self.close()
        

