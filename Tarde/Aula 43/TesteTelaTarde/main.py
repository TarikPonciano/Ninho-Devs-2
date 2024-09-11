import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(200,200,400,300)
        
        self.rotulo = QLabel("Hello World", self)
        self.rotulo.move(150,100)
        
        self.botao = QPushButton("Apertar", self)
        self.botao.move(150,150)
        self.botao.clicked.connect(self.apertarBotao)
        
    def apertarBotao(self):
        self.novaJanela = QWidget()
        self.novaJanela.setWindowTitle("Nova Janela")
        self.novaJanela.setGeometry(600,200,400,300)
        self.novaJanela.setStyleSheet("background-color:green")
        self.novaJanela.show()
        self.close()
def main():
    
    app = QApplication(sys.argv)
    
    window = JanelaPrincipal()
    
    
    
    window.show()
    sys.exit(app.exec())
    
main()