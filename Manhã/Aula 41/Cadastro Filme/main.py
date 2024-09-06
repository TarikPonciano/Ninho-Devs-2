import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox

def main():
    def enviarInformacoes():
        nome = campoNome.text()
        duracao =campoDuracao.text()
        genero = campoGenero.text()
        
        campoNome.setEnabled(False)
        campoDuracao.setEnabled(False)
        campoGenero.setEnabled(False)
        
        # popup = QMessageBox(janela)
        print(f'''
    Filme Cadastrado
    
Nome: {nome}
Duração: {duracao}
Gênero: {genero}
                      ''')
        
        
        
        
         
    app = QApplication(sys.argv)
    
    janela = QWidget()
    janela.setWindowTitle("Locadora de Filmes")
    janela.setGeometry(400,200, 400,300)
    
    #Criação de componentes
    rotuloMensagem = QLabel(janela)
    rotuloMensagem.setText("Bem vindo ao Sistema Locadora")
    rotuloMensagem.move(100, 20)
    # rotuloMensagem.setStyleSheet("QLabel {font-size: 16px; color: blue; border-width: 1px; border-color:black}")
    
    #Formulário
    # Nome, Duração, Gênero
    
    #Linha de preenchimento do Nome
    rotuloNome = QLabel("Nome:", janela)
    rotuloNome.setGeometry(70,80,80,20)
    
    campoNome = QLineEdit(janela)
    campoNome.setGeometry(70+rotuloNome.width()+20, 80, 150, 20)
    
    #Linha de preenchimento da duração
    rotuloDuracao = QLabel("Duração:", janela)
    rotuloDuracao.setGeometry(70, 120, 80, 20)
    
    campoDuracao = QLineEdit(janela)
    campoDuracao.setGeometry(70+rotuloDuracao.width()+20,120,150,20)
    
    #Linha de preenchimento de gênero
    
    rotuloGenero = QLabel("Gênero:", janela)
    rotuloGenero.setGeometry(70, 160, 80, 20)
    
    campoGenero = QLineEdit(janela)
    campoGenero.setGeometry(70+rotuloGenero.width()+20,160,150,20)
    
    #Criar botões de Enviar e Limpar
    #Enviar: Bloquear os campos para escrita, bloquear o próprio botão de enviar e vai imprimir no terminal as informações do filme
    
    
    botaoEnviar = QPushButton("Enviar", janela)
    botaoEnviar.setGeometry(220, 200, 80,40 )
    botaoEnviar.clicked.connect(enviarInformacoes)
    
    
    #Limpar: Desbloqueia o botão enviar e os campos para escrita, limpa os campos
    
    botaoLimpar = QPushButton("Limpar", janela)
    botaoLimpar.setGeometry(100, 200, 80,40 )
    
    
    janela.show()
    
    sys.exit(app.exec())
    
    
    
    
main()

