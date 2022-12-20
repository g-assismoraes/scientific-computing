import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ContornoBox(QWidget):

    def __init__(self):
        super(ContornoBox, self).__init__()
        self.setGeometry(800, 300, 200, 100)
        self.setWindowTitle("MyGLDrawer")

        self.dir_value = None
        self.neu_value = None
        self.okClicked = False
        self.b2Clicked = False
        self.b3Clicked = False

        self.x_force = None
        self.y_force = None

        self.xFLabel = QLabel("Insira valor para força externa no eixo X:")
        self.yFLabel = QLabel("Insira valor para força externa no eixo y:")
        self.boxXF = QLineEdit() 
        self.boxYF = QLineEdit()

        self.dirLabel = QLabel("Insira valor para condição de Dirichlet:")
        self.neuLabel = QLabel("Insira valor para condição de Neumann:")

        self.boxD = QLineEdit() 
        self.boxN = QLineEdit()

        self.b1 = QPushButton("Confirmar")
        self.b2 = QPushButton("Confirmar")
        self.b3 = QPushButton("Bloquear partículas")
        
        self.vbox = QVBoxLayout()

        self.vbox.addWidget(QLabel("!!! UTILIZE SOMENTE UM DOS CAMPOS POR VEZ !!!"))
        self.vbox.addWidget(QLabel("----------------- MDF -----------------"),alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.dirLabel)
        self.vbox.addWidget(self.boxD)
        self.vbox.addWidget(self.neuLabel)
        self.vbox.addWidget(self.boxN)
        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(QLabel("----------------- MED -----------------"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.xFLabel)
        self.vbox.addWidget(self.boxXF)
        self.vbox.addWidget(self.yFLabel)
        self.vbox.addWidget(self.boxYF)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)

        self.setLayout(self.vbox)

        self.b1.clicked.connect(self.onConfClicked)
        self.b2.clicked.connect(self.forces)
        self.b3.clicked.connect(self.block)

    def block(self):
        self.b3Clicked = True
        self.close()
    
    def forces(self):
        try:
            self.x_force = float(self.boxXF.text())
        except:
            self.x_force = 0.0
        
        try:
            self.y_force = float(self.boxYF.text())
        except:
            self.y_force = 0.0
        
        self.b2Clicked = True

        self.boxXF.setText(str(""))
        self.boxYF.setText(str(""))
        self.close()
    
    def onConfClicked(self):
        try:
            if self.boxD.text() != "":
                self.dir_value = float(self.boxD.text())
                self.boxD.setText(str(self.dir_value))
                self.neu_value = None
            elif self.boxN.text() != "":
                self.neu_value = float(self.boxN.text())
                self.boxN.setText(str(self.neu_value))
                self.dir_value = None
 
        except:
            self.dir_value = None
            self.neu_value = None
        self.okClicked = True

        self.boxN.setText(str(""))
        self.boxD.setText(str(""))
        self.close()
        

