import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

def main():
    filmes = ["Star Wars", "Kung fu Panda", "Shrek", "Finding Nemo", "The Lion King", "Toy Story"]
    rotulosFilmes = []

    app = QApplication(sys.argv)
    janela = QWidget()
    janela.setWindowTitle("Ver filmes")
    janela.setGeometry(100, 100, 600, 400)
    estiloTexto = "QLabel{color:blue; font-size:24px; font-weight:bold}"
    for i,filme in enumerate(filmes):
        
        novoLabel = QLabel(f"{i+1}. {filme}", janela)
        novoLabel.move(50, 20+(30*i))
        
        novoLabel.setStyleSheet(estiloTexto)
        
        novoLabel.adjustSize()
        
        botaoVer = QPushButton("Ver Filme",janela)
        botaoVer.move(50+novoLabel.width()+20, 20+(30*i) )
       
        rotulosFilmes.append(novoLabel)
        
    rotulosFilmes[3].setText(rotulosFilmes[3].text()+"(ESGOTADO)")
    rotulosFilmes[3].setStyleSheet("QLabel{color:red; font-size:24px; font-weight:bold}")
        
    
    
    
    janela.show()
    sys.exit(app.exec())
    
main()