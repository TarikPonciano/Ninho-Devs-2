import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QSizePolicy
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

class JanelaPrincipal (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Teste de Layouts")
        self.setGeometry(200,50,800,600)
        self.contentPane = QWidget()
        self.setCentralWidget(self.contentPane)
        
        self.caixaMenuPrincipal = QWidget(self.contentPane)
        self.caixaMenuPrincipal.setGeometry(300, 150, 200,300)
        self.caixaMenuPrincipal.setStyleSheet("QWidget{ background-color: red;} QPushButton{background-color: #f0f0f0;}")
        
        self.layoutMenuPrincipal = QVBoxLayout()
        
        
        self.botao1 = QPushButton("Botao 1")
        self.botao1.setIcon(QIcon("images/instagram-logo.png"))
        self.botao1.setIconSize(QSize(32,32))
        self.botao1.setStyleSheet("background-color:white; border-radius: 16px; color:gray;")
        
        self.botao1.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        self.botao2 = QPushButton("Botao 2")
        self.botao2.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        self.botao3 = QPushButton("Botao 3")
        self.botao3.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        self.botao4 = QPushButton("Botao 4")
        self.botao4.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        
        self.layoutMenuPrincipal.addWidget(self.botao1)
        self.layoutMenuPrincipal.addWidget(self.botao2)
        self.layoutMenuPrincipal.addWidget(self.botao3)
        self.layoutMenuPrincipal.addWidget(self.botao4)
        
        self.caixaMenuPrincipal.setLayout(self.layoutMenuPrincipal)
    
        
        
        
def main():
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    sys.exit(app.exec())
    
if __name__  == "__main__":
    main()
