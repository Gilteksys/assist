import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from cadastro_cliente import CadastroClienteWindow
from OrdemServico import OrdemServicoDialog
from django.core.management import execute_from_command_line
import subprocess

def initialize_django():
    # Configure as configurações do seu projeto Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agenda.settings')


    # Inicie o servidor Django
    execute_from_command_line(['manage.py', 'runserver'])

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Carregar o arquivo .ui
        script = os.path.dirname(os.path.abspath(__file__))
        arquivo_ui = os.path.join(script, 'main.ui')
        loadUi(arquivo_ui, self)

        self.setWindowTitle('ASSIST-3.0')
        self.setGeometry(200, 100, 700, 540)

        self.pushButton.clicked.connect(self.on_button_clientes_clicked)    
        self.pushButton_3.clicked.connect(self.on_ordem_servico_clicked)
        self.pushButton_5.clicked.connect(self.close)  # Conectar o botão "Sair" ao método close

    def on_button_clientes_clicked(self):
        self.cadastro_cliente_window = CadastroClienteWindow()
        self.cadastro_cliente_window.show()

    def on_ordem_servico_clicked(self):
        self.ordem_servico_window = OrdemServicoDialog()  
        self.ordem_servico_window.show()

if __name__ == '__main__':
    # Inicie o servidor Django em um processo separado
    django_process = subprocess.Popen(["python", "manage.py", "runserver"])

    # Inicie a aplicação PyQt5
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())







