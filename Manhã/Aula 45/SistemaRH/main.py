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
        self.contentPane.setStyleSheet("QWidget {background-color: black;}")
        self.setCentralWidget(self.contentPane)
        
        self.layoutJanela = QHBoxLayout()
        self.layoutJanela.setContentsMargins(1,1,1,1)
        self.layoutJanela.setSpacing(1)
        
        self.menuLateral = self.criarMenuLateral()
        self.layoutJanela.addWidget(self.menuLateral,1)
        
        self.conteudoPrincipal = QWidget()
        self.conteudoPrincipal.setStyleSheet("QWidget {background-color:#2f2b30;}")
        self.layoutJanela.addWidget(self.conteudoPrincipal,3)
        
        
        self.contentPane.setLayout(self.layoutJanela)
        
    def criarMenuLateral(self):
        menuLateral = QWidget()
        menuLateral.setStyleSheet('''QWidget {background-color:#1f2124; border:3px solid black;} 
        QPushButton {background-color: #252680; color: white; border: 2px outset black; border-top-left-radius: 20px; border-bottom-left-radius: 20px; font: 16px;}
        QPushButton:hover {background-color: #1d1e63;
        }
        QPushButton:pressed {background-color: #080bbf;}
        ''')
        layoutMenuLateral = QVBoxLayout()
        layoutMenuLateral.setSpacing(30)
        layoutMenuLateral.setContentsMargins(40, 100, 0, 150)
        
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
    
if __name__ == "__main__":
    main()