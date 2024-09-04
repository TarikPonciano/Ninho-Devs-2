import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton

def main():
    def mudarNome():
        nome = inputNome.text()
        rotuloMensagem.setText(f"Hello\n {nome}!")
        rotuloMensagem.adjustSize()
        inputNome.setText("")
        print(nome)
        
        
    app = QApplication(sys.argv)
    janela = QWidget()
    janela.setWindowTitle("Primeira Janela")
    
    janela.setGeometry(300,100,400,300)
    
    #Criar os componentes
    rotuloMensagem = QLabel("Hello World", janela)
    
    rotuloMensagem.move(150,0)

    
    
    inputNome = QLineEdit(janela)
    inputNome.move(150,50)
    
    
    botaoEnviar = QPushButton("Enviar", janela)
    botaoEnviar.move(150, 100)
    
    botaoEnviar.clicked.connect(mudarNome)
    
    botaoNovo = QPushButton("Novo", janela)
    
    
    
    janela.show()
    sys.exit(app.exec())
    

#Utilizando o PyQT crie um formulário de cadastro de um filme de locadora

# O Filme deve ter: nome, duração e gênero

# Ao apertar o botão enviar, deve ser impresso na tela as informações do filme cadastrado e zerar os campos de preenchimento.
    
    
main()