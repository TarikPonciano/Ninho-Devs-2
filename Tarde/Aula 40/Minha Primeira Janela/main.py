import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


    
def main():
    
    def enviarNome():
        nome = campoNome.text()
        rotuloMensagem.setText(f"Hello {nome}!")
        rotuloMensagem.adjustSize()
        #campoNome.setEnabled(False) Desativa o campo de escrita
        campoNome.setText("")
        
    app = QApplication(sys.argv)
    
    janela = QWidget()
    janela.setWindowTitle("Primeira Janela")
    janela.setGeometry(400,150,400,300)
    
    #Criar os componentes
    rotuloMensagem = QLabel("Hello World", janela)
    rotuloMensagem.move(175,125)
    
    #Criar um campo para o usuário escrever seu nome
    rotuloNome = QLabel("Nome: ", janela)
    rotuloNome.move(125, 150)
    
    campoNome = QLineEdit(janela)
    campoNome.move(175, 150)
    
    
    #Criar um botão que ao apertado irá mudar a mensagem para "Hello <nome>!"
    botaoEnviar = QPushButton("Enviar", janela)
    botaoEnviar.move(175, 175)
    botaoEnviar.clicked.connect(enviarNome)
    
    janela.show()
    sys.exit(app.exec())


main()

#Criar uma janela de cadastro de filmes de locadora

#A janela deve conter um formulário com os campos Nome, Duração e Gênero

#Crie um botão que ao ser clicado lê as informações digitadas e imprime elas na tela no formato:

#Nome: <>
#Duração: <>
#Gênero: <>