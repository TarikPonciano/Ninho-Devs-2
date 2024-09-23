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
        self.setWindowTitle("Sistema RH")
        self.setFixedSize(800,600)
        
        self.telaPrincipal = QWidget()
        self.construtorTelaPrincipal = Ui_TelaPrincipal()
        self.construtorTelaPrincipal.setupUi(self.telaPrincipal)
        self.layoutCaixaConteudo = QStackedLayout()
        
        self.construtorTelaPrincipal.CaixaConteudo.setLayout(self.layoutCaixaConteudo)
        
        self.layoutCaixaConteudo.addWidget(QWidget())
        
        self.telaVerFuncionarios = QWidget()
        self.construtorTelaVerFuncionarios = Ui_TelaVerFuncionarios()
        self.construtorTelaVerFuncionarios.setupUi(self.telaVerFuncionarios)
        
        self.layoutCaixaConteudo.addWidget(self.telaVerFuncionarios)
        
        self.construtorTelaPrincipal.botaoVerFuncionarios.clicked.connect(self.mostrarVerFuncionarios)
        
        self.construtorTelaPrincipal.botaoSair.clicked.connect(lambda:self.close())
              
        self.setCentralWidget(self.telaPrincipal)
        
    def mostrarVerFuncionarios(self):
        funcionarios = conexaoBD.consultar("Select * from funcionarios")
        self.construtorTelaVerFuncionarios.tabelaVerFuncionarios.setRowCount(len(funcionarios))
        linhaAtual = 0
        for funcionario in funcionarios:
            print(funcionario[0])
            self.construtorTelaVerFuncionarios.tabelaVerFuncionarios.setItem(linhaAtual, 0, QTableWidgetItem(str(funcionario[0])))
            
            self.construtorTelaVerFuncionarios.tabelaVerFuncionarios.setItem(linhaAtual, 1, QTableWidgetItem(funcionario[1]))
            
            self.construtorTelaVerFuncionarios.tabelaVerFuncionarios.setItem(linhaAtual, 2, QTableWidgetItem(funcionario[2]))
            
            self.construtorTelaVerFuncionarios.tabelaVerFuncionarios.setItem(linhaAtual, 3, QTableWidgetItem(f"R$ {funcionario[3]}"))
            
            linhaAtual += 1
        self.layoutCaixaConteudo.setCurrentIndex(1)
        
def main():
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()