import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(200,200,400,300)
        
        self.rotuloHello = QLabel("Hello World", self)
        self.rotuloHello.move(150,100)
        
        self.botaoApertar = QPushButton("Apertar", self)
        self.botaoApertar.move(150, 150)
        
        self.botaoApertar.clicked.connect(self.botaoApertado)
    
    def botaoApertado(self):
        self.rotuloHello.setText("Botão clicado")

def main():
    app = QApplication(sys.argv)
    
    janela = JanelaPrincipal()
    
    janela.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()