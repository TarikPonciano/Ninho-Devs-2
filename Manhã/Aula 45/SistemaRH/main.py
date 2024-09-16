import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QStackedLayout, QPushButton, QMainWindow, QSizePolicy
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema RH")
        self.setFixedSize(800,600)
        self.contentPane = QWidget()
        self.contentPane.setStyleSheet("QWidget {background-color: rgb(125,125,125)}")
        self.setCentralWidget(self.contentPane)
        
        self.layoutJanela = QHBoxLayout()
        self.layoutJanela.setContentsMargins(1,1,1,1)
        self.layoutJanela.setSpacing(1)
        
        self.menuLateral = self.criarMenuLateral()
        self.layoutJanela.addWidget(self.menuLateral,1)
        
        self.conteudoPrincipal = QWidget()
        self.conteudoPrincipal.setStyleSheet("QWidget {background-color:rgb(0,180,0)}")
        self.layoutJanela.addWidget(self.conteudoPrincipal,3)
        
        
        self.contentPane.setLayout(self.layoutJanela)
        
    def criarMenuLateral(self):
        menuLateral = QWidget()
        menuLateral.setStyleSheet('''QWidget {background-color:rgb(180,0,0); border:3px solid black;} 
        QPushButton {background-color: rgb(0,0,150); color: white; border: 2px outset black; border-radius:30px; height: 100%;}
        ''')
        layoutMenuLateral = QVBoxLayout()
        layoutMenuLateral.setSpacing(25)
        layoutMenuLateral.setContentsMargins(50, 100, 0, 200)
        
        botaoVerFuncionarios = QPushButton("Ver Funcionarios")
        
        layoutMenuLateral.addWidget(botaoVerFuncionarios)
        
        botaoInserirFuncionario = QPushButton("Inserir Funcionario")
        
        layoutMenuLateral.addWidget(botaoInserirFuncionario)
        
        botaoAlterarFuncionario = QPushButton("Alterar Funcionario")
        layoutMenuLateral.addWidget(botaoAlterarFuncionario)
        
        botaoRemoverFuncionario = QPushButton("Remover Funcionario")
        layoutMenuLateral.addWidget(botaoRemoverFuncionario)
        
        botaoSair = QPushButton("Sair")
        layoutMenuLateral.addWidget(botaoSair)
        
        menuLateral.setLayout(layoutMenuLateral)
        return menuLateral

        
def main():
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()