import sys, os
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMainWindow
from principal import Ui_Buscardor
from resultado import *


class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_Buscardor()
        self.ui.setupUi(self)
        self.opened_file = None

    class Resultado(QMainWindow):
        def __init__(self):
            super(Resultado, self).__init__()
            self.ui = Ui_Resultado()
            self.ui.setupUi(self)

    @Slot()
    def func(self):
        pass

    @Slot()
    def buscar(self):

        self.nombre = self.ui.lblNombre.text()
        self.user = os.popen("whoami").read()
        self.user = self.user.rsplit()
        self.ruta = "/home/" + self.user[0]
        os.chdir(self.ruta)
        self.resultado = os.popen("find -not -path '*/\.*' | grep '" + self.nombre + "'")
        self.ventanita = Resultado()
        self.ventanita.ui.txtResultado.setText(self.resultado)
        self.ventanita.show()
        print(self.ruta)
    @Slot()
    def borrar(self):
        print("Tocaste borrar")
        self.ui.lblNombre.setText("")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec_())