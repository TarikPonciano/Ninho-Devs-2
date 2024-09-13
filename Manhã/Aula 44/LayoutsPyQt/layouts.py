import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QSizePolicy

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
    
        self.botao1.setSizePolicy(QSizePolicy.)
        self.botao2 = QPushButton("Botao 2")
        self.botao2.setSizePolicy(QSizePolicy.expandingDirections)
        self.botao3 = QPushButton("Botao 3")
        self.botao3.setSizePolicy(QSizePolicy.expandingDirections)
        self.botao4 = QPushButton("Botao 4")
        self.botao4.setSizePolicy(QSizePolicy.expandingDirections)
        
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
