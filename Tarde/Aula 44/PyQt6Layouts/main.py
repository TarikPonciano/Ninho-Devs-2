import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Título da Janela")
        self.move(200,50)
        self.setFixedSize(800,600)
        
        self.contentPane = QWidget()
        self.contentPane.setStyleSheet('''QWidget { background-color: black;}
        QPushButton {background-color: #f0f0f0;
        font-size: 16px;
        font-weight:bold;
        border-radius:10px;}
        QPushButton:hover{
            background-color: #153c7a;
            }
        QPushButton:pressed{
            background-color: #1a90c7;}''')
        
        self.rotuloTitulo = QLabel("Sistema de Gerenciamento RH", self.contentPane)
        self.rotuloTitulo.setStyleSheet("color:white; font-size: 32px ; font-family: 'Arial', sans-serif; font-weight: bold;")
        self.rotuloTitulo.move(150, 50)
        
        self.botaoVerFuncionarios = QPushButton("Ver Funcionarios", self.contentPane)
        self.botaoVerFuncionarios.setGeometry(300,150,  200, 50)
        self.botaoVerFuncionarios.clicked.connect(self.exibirVerFuncionarios)

        
        self.botaoInserirFuncionarios = QPushButton("Inserir Funcionarios", self.contentPane)
        self.botaoInserirFuncionarios.setGeometry(300,210,  200, 50)
        
        self.botaoAlterarFuncionarios = QPushButton("Alterar Funcionarios", self.contentPane)
        
        self.botaoAlterarFuncionarios.setGeometry(300,270,  200, 50)
        
        self.botaoRemoverFuncionarios = QPushButton("Remover Funcionarios", self.contentPane)
        self.botaoRemoverFuncionarios.setGeometry(300,330,  200, 50)
        
        self.botaoSair = QPushButton("Sair", self.contentPane)
        self.botaoSair.setGeometry(300,390,  200, 50)
        self.botaoSair.setStyleSheet("background-color: #952828;")
        

        self.setCentralWidget(self.contentPane)

    def exibirVerFuncionarios(self):
        self.janelaVerFuncionarios = QWidget()
        self.janelaVerFuncionarios.setStyleSheet("background-color:red;")
        self.janelaVerFuncionarios.setGeometry(200,50, self.contentPane.width(),  self.contentPane.height())
        self.rotuloVerFuncionarios = QLabel("Ver Funcionários",  self.janelaVerFuncionarios)
        self.rotuloVerFuncionarios.move(150, 50)
        self.rotuloVerFuncionarios.setStyleSheet("color:white; font-size: 32px ; font-family: 'Arial', sans-serif; font-weight: bold;")
        
        self.botaoVerFuncionariosVoltar = QPushButton("Voltar", self.janelaVerFuncionarios)
        self.botaoVerFuncionariosVoltar.move(400,200)
        self.botaoVerFuncionariosVoltar.setStyleSheet("background-color:  #f0f0f0;")
        self.botaoVerFuncionariosVoltar.clicked.connect(self.voltarMenuPrincipal)



        self.janelaVerFuncionarios.show()
        self.hide()
        
    def voltarMenuPrincipal(self):
        self.janelaVerFuncionarios.close()
        self.show()
        
def main():
    app = QApplication(sys.argv)
    
    janela = JanelaPrincipal()

    
    janela.show()
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()