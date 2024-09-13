import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
def main():
    app = QApplication(sys.argv)
    
    janela = JanelaPrincipal()
    janela.show()
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()