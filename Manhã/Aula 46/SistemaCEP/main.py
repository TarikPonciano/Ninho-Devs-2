import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from componentes.formularioEndereco import Ui_Formulario
import requests

class JanelaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(800,600)
        
        self.construtorFormulario = Ui_Formulario()
        self.contentPane = QWidget()
        self.construtorFormulario.setupUi(self.contentPane)
        self.construtorFormulario.corpoFormulario.setSpacing(20)
        self.construtorFormulario.linhaCep.setSpacing(50)
        self.construtorFormulario.campoCep.setMaxLength(8)
        self.construtorFormulario.campoLogradouro.setEnabled(False)
        self.construtorFormulario.campoCidade.setEnabled(False)
        self.construtorFormulario.campoPais.setEnabled(False)
        self.construtorFormulario.campoEstado.setEnabled(False)
        self.construtorFormulario.botaoBuscar.clicked.connect(self.buscarCep)
        self.contentPane.setStyleSheet("QLineEdit{font:16px; font-weight:bold;}QLineEdit:disabled{border: 5px dashed  black;} ")

        
        self.setCentralWidget(self.contentPane)
    def buscarCep(self):
        cep = self.construtorFormulario.campoCep.text()
        
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        
        detalhesCep = resposta.json()
        
        self.construtorFormulario.campoLogradouro.setText(detalhesCep["logradouro"])
        self.construtorFormulario.campoEstado.setText(detalhesCep["estado"])
        self.construtorFormulario.campoCidade.setText(detalhesCep["localidade"])
        self.construtorFormulario.campoPais.setText("Brasil")
        
        
def main():
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()