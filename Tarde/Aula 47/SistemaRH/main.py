import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from telaPrincipal import Ui_TelaPrincipal
from telaVerFuncionarios import Ui_TelaVerFuncionarios
from Conexao import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "sistemarh")

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(800,600)
        
        self.telaPrincipal = QWidget()
        self.construtorTelaPrincipal = Ui_TelaPrincipal()
        self.construtorTelaPrincipal.setupUi(self.telaPrincipal)
        
        self.layoutCaixaConteudo = QStackedLayout()
        
        self.construtorTelaPrincipal.CaixaConteudo.setLayout(self.layoutCaixaConteudo,)
        
        self.conteudoInicial = QWidget()
        self.conteudoInicialLayout = QVBoxLayout()
        self.conteudoInicial.setLayout(self.conteudoInicialLayout)
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap("logo-removebg-preview.png"))
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.conteudoInicialLayout.addWidget(self.logo)
        
        self.layoutCaixaConteudo.addWidget(self.conteudoInicial)
        
        self.telaVerFuncionarios = QWidget()
        self.construtorTelaVerFuncionarios = Ui_TelaVerFuncionarios()
        self.construtorTelaVerFuncionarios.setupUi(self.telaVerFuncionarios)
        
        self.layoutCaixaConteudo.addWidget(self.telaVerFuncionarios)
        
        
        self.construtorTelaPrincipal.botaoVerFuncionarios.clicked.connect(self.exibirTelaVerFuncionarios)
        
        self.setCentralWidget(self.telaPrincipal) 
        
    def exibirTelaVerFuncionarios(self):
        funcionarios = conexaoBD.consultar("SELECT * FROM funcionarios;")
     
        self.construtorTelaVerFuncionarios.tabelaFuncionarios.setRowCount(len(funcionarios))
        
        
        
        for linhaAtual, funcionario in enumerate(funcionarios):
            id = QTableWidgetItem(str(funcionario[0]))
            id.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            nome = QTableWidgetItem(funcionario[1])
            nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            cargo = QTableWidgetItem(funcionario[2])
            cargo.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            salario = QTableWidgetItem(f"R$ {funcionario[3]}")
            salario.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            self.construtorTelaVerFuncionarios.tabelaFuncionarios.setItem(linhaAtual, 0, id)
            self.construtorTelaVerFuncionarios.tabelaFuncionarios.setItem(linhaAtual, 1, nome)
            self.construtorTelaVerFuncionarios.tabelaFuncionarios.setItem(linhaAtual, 2, cargo)
            self.construtorTelaVerFuncionarios.tabelaFuncionarios.setItem(linhaAtual, 3, salario)
            
            
        
        self.layoutCaixaConteudo.setCurrentIndex(1)

        
def main():
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()