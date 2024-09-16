import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout, QSizePolicy, QComboBox, QStackedLayout
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

class JanelaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema RH")
        self.setFixedSize(800,600)
        
        self.contentPane = QWidget()
        self.contentPane.setStyleSheet("QWidget { background-color: rgb(125,125,125);}")
        
        self.layoutJanela = QHBoxLayout()
        self.layoutJanela.setContentsMargins(1,1,1,1)
        self.layoutJanela.setSpacing(1)
        
        self.menuLateral = self.criarMenuLateral()    
        self.layoutJanela.addWidget(self.menuLateral,1)    
        
        self.conteudoPrincipal = QWidget()
        self.conteudoPrincipal.setStyleSheet("background-color:rgb(150,150,0)")
        
        self.layoutJanela.addWidget(self.conteudoPrincipal,3)
        
        
        self.contentPane.setLayout(self.layoutJanela)
        self.setCentralWidget(self.contentPane)
        
    def criarMenuLateral(self):
        menuLateral = QWidget()
        

        menuLateral.setStyleSheet('''
        QWidget{
            background-color: rgb(120,0,0);
            border: 3px solid black;}
        QPushButton {
            background-color: rgb(0,0,150);
            color: white;
            font: 16px;
            font-weight: bold;
            font-family: "Segoe UI";
            border: 1px outset #f0f0f0;
            border-top-left-radius: 20px;
            border-bottom-left-radius: 20px;
            }
        QPushButton:hover{
            background-color:rgb(0,0,120);
        }
        QPushButton:pressed{
            background-color:rgb(0,0,170);
            border-style: inset;
        }
            ''')
        
        layoutMenuLateral = QVBoxLayout()
        layoutMenuLateral.setContentsMargins(40,100,0,150)
        layoutMenuLateral.setSpacing(15)
        
        botaoVerFuncionarios = QPushButton("Ver Funcionarios")
        botaoVerFuncionarios.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        
        layoutMenuLateral.addWidget(botaoVerFuncionarios)
        
        botaoInserirFuncionario = QPushButton("Inserir Funcionario")
        botaoInserirFuncionario.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        
        layoutMenuLateral.addWidget(botaoInserirFuncionario)
        
        botaoAlterarFuncionario = QPushButton("Alterar Funcionario")
        botaoAlterarFuncionario.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        
        layoutMenuLateral.addWidget(botaoAlterarFuncionario)
        
        botaoRemoverFuncionario = QPushButton("Remover Funcionario")
        botaoRemoverFuncionario.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        
        layoutMenuLateral.addWidget(botaoRemoverFuncionario)
        
        botaoSair = QPushButton("Sair")
        botaoSair.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        
        layoutMenuLateral.addWidget(botaoSair)
        
        menuLateral.setLayout(layoutMenuLateral)
        
        return menuLateral

        
        
def main():
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    sys.exit(app.exec())

main()

