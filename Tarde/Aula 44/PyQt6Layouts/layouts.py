import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy

class JanelaPrincipal(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Menu Principal")
        self.move(200,50)
        self.setFixedSize(800,600)
        
        self.contentPane = QWidget()
        self.contentPane.setStyleSheet("QWidget  {background-color: #000000;}")
        
        self.caixaMenuPrincipal = QWidget(self.contentPane)
        self.caixaMenuPrincipal.setStyleSheet("QWidget{background-color:white;} QPushButton{background-color: #909090;}")
        self.caixaMenuPrincipal.setGeometry(300,200,200,300)
        
        self.layoutMenuPrincipal = QVBoxLayout()
        self.layoutMenuPrincipal.setSpacing(10)
        self.layoutMenuPrincipal.setContentsMargins(5,5,5,5)
        
        self.botao1 = QPushButton("Botão 1")
        self.botao1.setSizePolicy(QSizePolicy.Policy.Expanding,  QSizePolicy.Policy.Expanding)
        self.layoutMenuPrincipal.addWidget(self.botao1)
        
        
        self.botao2 = QPushButton("Botão 2")
        self.botao2.setSizePolicy(QSizePolicy.Policy.Expanding,  QSizePolicy.Policy.Expanding)
        self.layoutMenuPrincipal.addWidget(self.botao2)
        
        self.botao3 = QPushButton("Botão 3")
        self.botao3.setSizePolicy(QSizePolicy.Policy.Expanding,  QSizePolicy.Policy.Expanding)        
        self.layoutMenuPrincipal.addWidget(self.botao3)
        
        self.botao4 = QPushButton("Botão 4")
        self.botao4.setSizePolicy(QSizePolicy.Policy.Expanding,  QSizePolicy.Policy.Expanding)        
        self.layoutMenuPrincipal.addWidget(self.botao4)
        
        self.botao5 = QPushButton("Botão 5")
        self.botao5.setSizePolicy(QSizePolicy.Policy.Expanding,  QSizePolicy.Policy.Expanding)        
        self.layoutMenuPrincipal.addWidget(self.botao5)
        
        self.caixaMenuPrincipal.setLayout(self.layoutMenuPrincipal)
        

        self.setCentralWidget(self.contentPane)
        
def main():
    app = QApplication(sys.argv)
    
    janela = JanelaPrincipal()
    
    janela.show()
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()