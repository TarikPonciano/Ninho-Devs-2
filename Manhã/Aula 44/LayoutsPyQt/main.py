import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton #pip install pyqt6


class JanelaPrincipal(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema RH")
        self.setGeometry(400,100, 600,400)
        
        self.contentPane = QWidget()
        self.setCentralWidget(self.contentPane)
        self.contentPane.setStyleSheet('''
        QWidget {
            background-color: #f0f0f0;
        }
        QPushButton{
            background-color: #4CAF50;
            font: 16px;
            font-weight: bold;
            border-radius:10px;
        }
        QPushButton:hover{
            background-color: #5674a3
        }
                                       
                                       ''')
                
        self.rotuloJanela = QLabel("Sistema RH XYZ", self.contentPane)
        self.rotuloJanela.move(150,50)
        self.rotuloJanela.setStyleSheet('''font: 32px; color: blue; font-family: "Segoe UI"; font-weight:bold''')
        
        self.botaoVerFuncionarios = QPushButton("Ver Funcionarios", self.contentPane)
        self.botaoVerFuncionarios.setGeometry(200,150,175,50)
        self.botaoVerFuncionarios.clicked.connect(self.exibirVerFuncionarios)
        
        self.botaoInserirFuncionarios = QPushButton("Inserir Funcionarios", self.contentPane)
        self.botaoInserirFuncionarios.setGeometry(200,200,175,50)
        self.botaoInserirFuncionarios.clicked.connect(self.exibirInserirFuncionarios)
        
        self.botaoAlterarFuncionarios = QPushButton("Alterar Funcionarios", self.contentPane)
        self.botaoAlterarFuncionarios.setGeometry(200,250,175,50)
        # self.botaoAlterarFuncionarios.clicked.connect()
        
        self.botaoRemoverFuncionarios = QPushButton("Remover Funcionarios", self.contentPane)
        self.botaoRemoverFuncionarios.setGeometry(200,300,175,50)
        # self.botaoRemoverFuncionarios.clicked.connect()
        
    def exibirVerFuncionarios(self):
        self.janelaVerFuncionarios = QWidget()
        self.janelaVerFuncionarios.setWindowTitle("Ver Funcionários")
        self.janelaVerFuncionarios.setGeometry(200,200, 400,300)
        
        self.botaoJanelaVerFuncionariosVoltar = QPushButton("Voltar", self.janelaVerFuncionarios)
        self.botaoJanelaVerFuncionariosVoltar.clicked.connect(lambda: self.voltarParaJanelaPrincipal(self.janelaVerFuncionarios))
        
    
        self.janelaVerFuncionarios.show()
        self.hide()
    
    def exibirInserirFuncionarios(self):
        self.janelaInserirFuncionarios = QWidget()
        self.janelaInserirFuncionarios.setWindowTitle("Inserir Funcionarios")
        self.janelaInserirFuncionarios.setGeometry(200,200,400,300)
        
        self.janelaInserirFuncionariosBotaoVoltar = QPushButton("Voltar", self.janelaInserirFuncionarios)
        self.janelaInserirFuncionariosBotaoVoltar.clicked.connect(lambda: self.voltarParaJanelaPrincipal(self.janelaInserirFuncionarios))
        
        self.janelaInserirFuncionarios.show()
        self.hide()
    def voltarParaJanelaPrincipal(self, janelaAtual):
        janelaAtual.close()
        self.show()
        

        
        
    
        

def main():
    app = QApplication(sys.argv)
    
    janela = JanelaPrincipal()
    
    janela.show()
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()