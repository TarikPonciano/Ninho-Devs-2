import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

def main():
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
    
    #Linha Genero
    
    
    janela.show()
    sys.exit(app.exec())
    
    

main()

