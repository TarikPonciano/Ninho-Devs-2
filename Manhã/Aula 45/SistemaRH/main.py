import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QStackedLayout, QPushButton, QMainWindow, QSizePolicy, QFormLayout, QLineEdit, QComboBox
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
        
        self.conteudoPrincipal = self.criarConteudoPrincipal()
    
        self.layoutJanela.addWidget(self.conteudoPrincipal,3)
        
        
        self.contentPane.setLayout(self.layoutJanela)
        
    def criarMenuLateral(self):
        menuLateral = QWidget()
        menuLateral.setStyleSheet('''QWidget {background-color:#1f2124; border:3px solid black;} 
                                  
        QPushButton {background-color: #252680; color: white; border: 2px outset gray; border-top-left-radius: 20px; border-bottom-left-radius: 20px;}
        QPushButton:hover {background-color: #1d1e63; 
        }
        QPushButton:pressed {background-color: #080bbf; border-style:inset;}
        
        QPushButton#Sair {background-color: rgb(150,20,20);}
        QPushButton#Sair:hover{background-color: rgb(120,0,0)}
        ''')
        layoutMenuLateral = QVBoxLayout()
        layoutMenuLateral.setSpacing(30)
        layoutMenuLateral.setContentsMargins(40, 100, 0, 150)
        
        botaoVerFuncionarios = QPushButton("Ver Funcionarios")
        botaoVerFuncionarios.setFont(QFont("Segoe UI", 16,  QFont.Weight.Bold))
        botaoVerFuncionarios.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        botaoVerFuncionarios.clicked.connect(lambda: self.mudarJanela(0))
        
        layoutMenuLateral.addWidget(botaoVerFuncionarios)
        
        botaoInserirFuncionario = QPushButton("Inserir Funcionario")
        botaoInserirFuncionario.setFont(QFont("Segoe UI", 16,  QFont.Weight.Bold))
        botaoInserirFuncionario.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        botaoInserirFuncionario.clicked.connect(lambda: self.mudarJanela(1))
        
        layoutMenuLateral.addWidget(botaoInserirFuncionario)
        
        botaoAlterarFuncionario = QPushButton("Alterar Funcionario")
        botaoAlterarFuncionario.setFont(QFont("Segoe UI", 16,  QFont.Weight.Bold))
        botaoAlterarFuncionario.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        
        layoutMenuLateral.addWidget(botaoAlterarFuncionario)
        
        botaoRemoverFuncionario = QPushButton("Remover Funcionario")
        botaoRemoverFuncionario.setFont(QFont("Segoe UI", 16,  QFont.Weight.Bold))
        botaoRemoverFuncionario.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        
        layoutMenuLateral.addWidget(botaoRemoverFuncionario)
        
        botaoSair = QPushButton("Sair")
        botaoSair.setFont(QFont("Segoe UI", 16,  QFont.Weight.Bold))
        botaoSair.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        botaoSair.setObjectName("Sair")
        botaoSair.clicked.connect(lambda:self.close())
        
        layoutMenuLateral.addWidget(botaoSair)
        
        menuLateral.setLayout(layoutMenuLateral)
        return menuLateral
    
    def mudarJanela(self, numeroJanela):
        if numeroJanela == 0:
            self.layoutCaixaDeConteudo.setCurrentIndex(0)
            self.rotuloTitulo.setText( "Ver Funcionários")
            
            
        if numeroJanela == 1:
            self.layoutCaixaDeConteudo.setCurrentIndex(1)
            self.rotuloTitulo.setText("Inserir Funcionário")
            
        
    
    def criarConteudoPrincipal (self):
        conteudoPrincipal = QWidget()
        conteudoPrincipal.setStyleSheet("QWidget {background-color:#2f2b30;}")
        
        layoutConteudoPrincipal = QVBoxLayout()
        layoutConteudoPrincipal.setSpacing(30)
        layoutConteudoPrincipal.setContentsMargins(50,20,50,50)
        
        self.rotuloTitulo = QLabel("Tela Teste")
        self.rotuloTitulo.setStyleSheet("color:white;")
        self.rotuloTitulo.setFont(QFont("Segoe UI", 32,  QFont.Weight.Bold))
        self.rotuloTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layoutConteudoPrincipal.addWidget(self.rotuloTitulo,1)
        
        caixaDeConteudo = QWidget()
        caixaDeConteudo.setStyleSheet("background-color: magenta;")
        self.layoutCaixaDeConteudo = QStackedLayout()
        
        
        
        telaVerFuncionarios = self.criarTelaVerFuncionarios()
        self.layoutCaixaDeConteudo.addWidget(telaVerFuncionarios)
        
        telaInserirFuncionario = self.criarTelaInserirFuncionario()
        self.layoutCaixaDeConteudo.addWidget(telaInserirFuncionario)
        
        telaInicial = QWidget()
        self.layoutCaixaDeConteudo.addWidget(telaInicial)
        self.layoutCaixaDeConteudo.setCurrentIndex(2)
        
        
        caixaDeConteudo.setLayout(self.layoutCaixaDeConteudo)
        
        
        layoutConteudoPrincipal.addWidget(caixaDeConteudo,4)
        
        conteudoPrincipal.setLayout(layoutConteudoPrincipal)
        
        return conteudoPrincipal
    
    def criarTelaVerFuncionarios(self):
        telaVerFuncionarios = QWidget()
        layoutTelaVerFuncionarios  = QVBoxLayout()
        telaVerFuncionarios.setStyleSheet("QWidget {background-color:#2f2b30;} QPushButton{background-color: rgb(200,200,200)}")
        
        for i in range(10):
            
            botaoFuncionario = QPushButton(f"Funcionario {i+1}")
            layoutTelaVerFuncionarios.addWidget(botaoFuncionario)
        
        telaVerFuncionarios.setLayout(layoutTelaVerFuncionarios)
        
        return telaVerFuncionarios
    
    def criarTelaInserirFuncionario(self):
        telaInserirFuncionario = QWidget()
        telaInserirFuncionario.setStyleSheet('''QWidget {background-color:#2f2b30;} QPushButton{background-color: rgb(200,200,200)} QLabel{color:white;  font-size: 16px;} QLineEdit{background-color:#f0f0f0; font:16px} QComboBox {background-color:#f0f0f0}''')

        
        layoutTelaInserirFuncionario = QFormLayout()
        layoutTelaInserirFuncionario.setSpacing(20)
        layoutTelaInserirFuncionario.setContentsMargins(20,20,20,20)
        
        inputNome = QLineEdit()
        layoutTelaInserirFuncionario.addRow("Nome:", inputNome)
        
        listaCargos = QComboBox()
        listaCargos.addItems(["Vendedor", "Gerente", "Repositor"])
        layoutTelaInserirFuncionario.addRow("Cargo:", listaCargos)
        
        inputSalario = QLineEdit()
        layoutTelaInserirFuncionario.addRow("Salario:", inputSalario)
        
        telaInserirFuncionario.setLayout(layoutTelaInserirFuncionario)
        
        return telaInserirFuncionario
        
        
def main():
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()