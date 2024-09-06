import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

def main():

    filmes = ["Star Wars", "Reino do Planeta dos Macacos", "Star Trek", "Senhor dos Anéis", "Duro de Matar"]
    rotulosFilme = []
    app = QApplication(sys.argv)
    janela = QWidget()
    janela.setGeometry(0,0,600,400)
    
    estiloTexto = "QLabel{font-size:24px; color:red}"
    for i, filme in enumerate(filmes):
        novoLabel = QLabel(filme, janela)
        novoLabel.move(50, 20 + (20*i))
        novoLabel.setStyleSheet(estiloTexto)
        rotulosFilme.append(novoLabel)
        
    
    rotulosFilme[3].setText("Removido")
        
    
    janela.show()
    
    sys.exit(app.exec())




main()