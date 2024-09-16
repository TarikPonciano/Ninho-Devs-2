import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout, QSizePolicy, QComboBox, QStackedLayout, QLineEdit
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

class JanelaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema RH")
        self.setFixedSize(800,600)
        
        self.contentPane = QWidget()
        self.contentPane.setStyleSheet("QWidget { background-color: black;}")
        
        self.layoutJanela = QHBoxLayout()
        self.layoutJanela.setContentsMargins(1,1,1,1)
        self.layoutJanela.setSpacing(1)
        
        self.menuLateral = self.criarMenuLateral()    
        self.layoutJanela.addWidget(self.menuLateral,1)    
        
        self.conteudoPrincipal = self.criarConteudoPrincipal()
        
        self.layoutJanela.addWidget(self.conteudoPrincipal,3)
        
        
        self.contentPane.setLayout(self.layoutJanela)
        self.setCentralWidget(self.contentPane)
    
    def criarConteudoPrincipal(self):
        
        conteudoPrincipal = QWidget()
        conteudoPrincipal.setStyleSheet('''QWidget{background-color:#1c1c36}
        QLabel{
            font:32px;
            color:white;
            font-family: "Segoe UI";
            font-weight:bold;
        }''')
        
        layoutConteudoPrincipal = QVBoxLayout()
        layoutConteudoPrincipal.setContentsMargins(50,20,50,50)
        layoutConteudoPrincipal.setSpacing(20)
        
        self.rotuloTitulo = QLabel("Título Teste")
        self.rotuloTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layoutConteudoPrincipal.addWidget(self.rotuloTitulo,1)
        
        caixaDeConteudo = QWidget()
        caixaDeConteudo.setStyleSheet("background-color:magenta;")
        
        self.layoutCaixaDeConteudo = QStackedLayout()
        
        telaVerFuncionarios = self.criarTelaVerFuncionarios()
        
        self.layoutCaixaDeConteudo.addWidget(telaVerFuncionarios)
        
        telaInserirFuncionario = self.criarTelaInserirFuncionario()
        
        self.layoutCaixaDeConteudo.addWidget(telaInserirFuncionario)
        
        telaInicial = QWidget()
        
        self.layoutCaixaDeConteudo.addWidget(telaInicial)
        
        self.layoutCaixaDeConteudo.setCurrentIndex(2)
        
        caixaDeConteudo.setLayout(self.layoutCaixaDeConteudo)
        
        layoutConteudoPrincipal.addWidget(caixaDeConteudo,5)
        
        conteudoPrincipal.setLayout(layoutConteudoPrincipal)
        
        return conteudoPrincipal
    
    def criarTelaInserirFuncionario(self):
        telaInserirFuncionario = QWidget()
        telaInserirFuncionario.setStyleSheet('''QWidget{background-color:#1c1c36; border:5px outset white; }
        QPushButton {
            background-color: white;
        }
        QPushButton:hover{
            background-color: gray;
        }
        QLabel{
            font:24px;
            color:white;
            font-family:"Segoe UI";
            font-weight:bold;
        }
        QLineEdit{
            background-color: white;
            color:black;
            font:24px;
            font-family:"Segoe UI";
        }
        QComboBox {
            background-color:white;
        }
    
        ''')
        
        layoutTelaInserirFuncionario = QFormLayout()
        
        layoutTelaInserirFuncionario.setHorizontalSpacing(50)
        layoutTelaInserirFuncionario.setVerticalSpacing(50)
        
        campoNome = QLineEdit()
        layoutTelaInserirFuncionario.addRow("Nome:", campoNome)
        
        listaCargos = QComboBox()
        listaCargos.addItems(["Vendedor", "Gerente", "Repositor", "Motorista"])
        layoutTelaInserirFuncionario.addRow("Cargo:", listaCargos)
        
        campoSalario = QLineEdit()
        layoutTelaInserirFuncionario.addRow("Salário:", campoSalario)
        
        telaInserirFuncionario.setLayout(layoutTelaInserirFuncionario)
        
        return telaInserirFuncionario
        
        
    def criarTelaVerFuncionarios(self):
        telaVerFuncionarios = QWidget()
        telaVerFuncionarios.setStyleSheet('''QWidget{background-color:#1c1c36; border:5px outset white; }
        QPushButton {
            background-color: white;
        }
        QPushButton:hover{
            background-color: gray;
        }
        ''')
        layoutTelaVerFuncionarios = QVBoxLayout()
        layoutTelaVerFuncionarios.setContentsMargins(50,20,50,20)
        layoutTelaVerFuncionarios.setSpacing(20)  
               
        for i in range(10):
            botaoFuncionario  = QPushButton(f"Funcionário {i+1}")
            layoutTelaVerFuncionarios.addWidget(botaoFuncionario)

        telaVerFuncionarios.setLayout(layoutTelaVerFuncionarios)
        
        return telaVerFuncionarios
    def criarMenuLateral(self):
        menuLateral = QWidget()
        

        menuLateral.setStyleSheet('''
        QWidget{
            background-color: #0e0e1a;
            border: 3px solid black;}
        QPushButton {
            background-color: hsv(242, 57%, 51%);
            color: white;
            font: 16px;
            font-weight: bold;
            font-family: "Segoe UI";
            border: 1px outset #000000;
            border-top-left-radius: 20px;
            border-bottom-left-radius: 20px;
            }
        QPushButton:hover{
            background-color:hsv(242, 57%, 31%);
        }
        QPushButton:pressed{
            background-color:hsv(242, 57%, 71%);
            border-style: inset;
        }
        QPushButton#Sair{
            background-color: red;
        }
        QPushButton#Sair:hover{
            background-color: rgb(120,0,0)
        }
        QPushButton#Sair:pressed{
            background-color: rgb(150,0,0)
        }
            ''')
        
        layoutMenuLateral = QVBoxLayout()
        layoutMenuLateral.setContentsMargins(40,100,0,150)
        layoutMenuLateral.setSpacing(15)
        
        botaoVerFuncionarios = QPushButton("Ver Funcionarios")
        botaoVerFuncionarios.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        botaoVerFuncionarios.clicked.connect(lambda: self.mudarJanela(0))
        
        layoutMenuLateral.addWidget(botaoVerFuncionarios)
        
        botaoInserirFuncionario = QPushButton("Inserir Funcionario")
        botaoInserirFuncionario.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        botaoInserirFuncionario.clicked.connect(lambda: self.mudarJanela(1))

        
        layoutMenuLateral.addWidget(botaoInserirFuncionario)
        
        botaoAlterarFuncionario = QPushButton("Alterar Funcionario")
        botaoAlterarFuncionario.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        botaoAlterarFuncionario.clicked.connect(lambda:  self.mudarJanela(2))

        
        layoutMenuLateral.addWidget(botaoAlterarFuncionario)
        
        botaoRemoverFuncionario = QPushButton("Remover Funcionario")
        botaoRemoverFuncionario.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        
        layoutMenuLateral.addWidget(botaoRemoverFuncionario)
        
        botaoSair = QPushButton("Sair")
        botaoSair.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        botaoSair.setObjectName("Sair")
        botaoSair.clicked.connect(lambda: self.close())
        #Criar interação do botão sair para fechar a aplicação
        
        layoutMenuLateral.addWidget(botaoSair)
        
        menuLateral.setLayout(layoutMenuLateral)
        
        return menuLateral

    def mudarJanela(self, telaEscolhida):
        
        if telaEscolhida == 0:
            self.rotuloTitulo.setText("Ver Funcionários")
            self.layoutCaixaDeConteudo.setCurrentIndex(0)
            
        if telaEscolhida == 1:
            self.rotuloTitulo.setText("Inserir Funcionário")
            self.layoutCaixaDeConteudo.setCurrentIndex(1)
            
        if telaEscolhida == 2:
            self.rotuloTitulo.setText("Alterar Funcionário")
            self.layoutCaixaDeConteudo.setCurrentIndex(2)
        
def main():
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    sys.exit(app.exec())

main()

