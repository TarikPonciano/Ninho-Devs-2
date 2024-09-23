import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from telaPrincipal import Ui_TelaPrincipal
from telaVerFuncionarios import Ui_TelaVerFuncionarios

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema RH")
        self.setFixedSize(800,600)
        
        self.telaPrincipal = QWidget()
        self.construtorTelaPrincipal = Ui_TelaPrincipal()
        self.construtorTelaPrincipal.setupUi(self.telaPrincipal)
        
        self.construtorTelaVerFuncionarios = Ui_TelaVerFuncionarios()
        self.construtorTelaVerFuncionarios.setupUi(self.construtorTelaPrincipal.CaixaConteudo)
        
        
        
        self.setCentralWidget(self.telaPrincipal)
        
        
def main():
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()