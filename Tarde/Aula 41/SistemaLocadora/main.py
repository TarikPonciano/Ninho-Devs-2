import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

def main():
    def enviarInformacoes():
        nome = campoNome.text()
        duracao = campoDuracao.text()
        genero = campoGenero.text()
        
        campoNome.setEnabled(False)
        campoDuracao.setEnabled(False)
        campoGenero.setEnabled(False)
        botaoEnviar.setEnabled(False)
        
        popup = QMessageBox(janela)
        popup.setWindowTitle("Confirmação de Cadastro")
        
        popup.setText(f'''
CADASTRADO COM SUCESSO
Nome - {nome}
Duração - {duracao}
Gênero - {genero}              
              ''')
        
        
        resultado = popup.exec()
        
        
    
    app = QApplication(sys.argv)
    
    janela = QWidget()
    janela.setWindowTitle("Locadora Asa Vídeos")
    janela.setGeometry(400,200, 400,300)
    
    # janela.setStyleSheet("QWidget{background-color:black}")
    
    #Construção dos componentes
    #Titulo da aplicação
    rotuloTitulo = QLabel(janela)
    rotuloTitulo.setText("Seja bem vindo à Locadora Asa Vídeos")
    rotuloTitulo.move(100,20)
    
    # rotuloTitulo.setStyleSheet("QLabel{font-size:24px; font-weight:bold; color:red}")
    #Criar formulário com Nome, Duração, Gênero e botões Enviar e Limpar
    
    # Linha Nome
    
    rotuloNome = QLabel("Nome:",janela)
    rotuloNome.setGeometry(80, 80, 80, 20)
    
    campoNome = QLineEdit(janela)
    campoNome.setGeometry(80+rotuloNome.width()+20, 80, 150, 20)
    
    #Linha Duração
    
    rotuloDuracao = QLabel("Duração:",janela)
    rotuloDuracao.setGeometry(80,120,80,20)
    
    campoDuracao = QLineEdit(janela)
    campoDuracao.setGeometry(80+rotuloDuracao.width()+20, 120, 150, 20)
    
    #Linha Genero
    
    rotuloGenero = QLabel("Gênero:",janela)
    rotuloGenero.setGeometry(80,160,80,20)
    
    campoGenero = QLineEdit(janela)
    campoGenero.setGeometry(80+rotuloGenero.width()+20, 160, 150, 20)
    
    #Criar botões Enviar e Limpar
    
    #O botão enviar deverá capturar todas as informações e exibir as informações do livro cadastrado em um popup. Após o envio os campos deverão ser desativados, incluindo o próprio botão enviar.
    
    botaoEnviar = QPushButton("Enviar",janela)
    botaoEnviar.setGeometry(240, 200 , 80, 40)
    botaoEnviar.clicked.connect(enviarInformacoes)
    
    #O botão limpar deverá limpar todos os campos do formulário e reativar a edição e o botão enviar, caso estejam desativados
    
    janela.show()
    sys.exit(app.exec())
    
    

main()

