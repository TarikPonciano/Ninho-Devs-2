import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout, QSizePolicy, QComboBox, QStackedLayout
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

class JanelaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema RH")
        self.setFixedSize(800,600)
        
        self.contentPane = QWidget()
        self.contentPane.setStyleSheet("QWidget { background-color: rgb(125,125,125);}")
        
        self.layoutJanela = QHBoxLayout()
        self.layoutJanela.setContentsMargins(1,1,1,1)
        self.layoutJanela.setSpacing(1)
        
        self.menuLateral = QWidget()
        self.menuLateral.setStyleSheet("background-color: rgb(150,0,0);")
        
        self.layoutJanela.addWidget(self.menuLateral,1)    
        
        self.conteudoPrincipal = QWidget()
        self.conteudoPrincipal.setStyleSheet("background-color:rgb(150,150,0)")
        
        self.layoutJanela.addWidget(self.conteudoPrincipal,3)
        
        
        self.contentPane.setLayout(self.layoutJanela)
        self.setCentralWidget(self.contentPane)

        
        
def main():
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    sys.exit(app.exec())

main()

