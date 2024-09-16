import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout, QSizePolicy, QComboBox, QStackedLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class JanelaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        
def main():
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    sys.exit(app.exec())

main()

