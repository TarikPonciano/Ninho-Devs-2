import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from componentes.formularioEndereco import Ui_CadastroEndereco
import requests


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(800,600)
        
        self.contentPane = QWidget()
        self.construtorFormularioEndereco = Ui_CadastroEndereco()
        self.construtorFormularioEndereco.setupUi(self.contentPane)
        self.construtorFormularioEndereco.verticalLayout_2.setContentsMargins(100,100,100,100)
        
        
        self.construtorFormularioEndereco.campoCep.setMaxLength(8)
        self.construtorFormularioEndereco.campoNumero.setMaxLength(5)
        self.construtorFormularioEndereco.campoCep.setValidator(QIntValidator())    
        self.construtorFormularioEndereco.campoLogradouro.setEnabled(False)
        self.construtorFormularioEndereco.campoBairro.setEnabled(False)
        self.construtorFormularioEndereco.campoCidade.setEnabled(False)
        self.construtorFormularioEndereco.campoUF.setEnabled(False)
        
        self.construtorFormularioEndereco.botaoBuscarCep.clicked.connect(self.buscarCep)
        

        
        self.setCentralWidget(self.contentPane)
        
    def buscarCep(self):
        cep = self.construtorFormularioEndereco.campoCep.text()
        
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    
        dadosCep = resposta.json()
        
        self.construtorFormularioEndereco.campoLogradouro.setText(dadosCep["logradouro"])
        self.construtorFormularioEndereco.campoBairro.setText(dadosCep["bairro"])
        self.construtorFormularioEndereco.campoCidade.setText(dadosCep["localidade"])
        self.construtorFormularioEndereco.campoUF.setText(dadosCep["uf"])
        
        
def main():
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()