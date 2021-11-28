'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Date: 2021-04-28
'''

# __LIBRARIES__ #
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
import sys
from functools import partial


# __MAIN CODE__ #
class Calculator(QMainWindow):
    def __init__(self):

        super(__init__()).__init__()  # lo mismo que Frame.__init__()

        self.setWindowTitle('Calculadora')
        self.setFixedSize(235, 235)
        # Establecemos la plantilla general
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self.create_display()
        self.create_buttons()

    def create_display(self):
        # Creamos la pantalla
        self.display = QLineEdit()
        # Establecemos las propiedades
        self.display.setFixedHeight(35)  # Alto
        self.display.setAlignment(Qt.AlignRight)  # alineacion
        self.display.setReadOnly(True)  # no puede seleccionarse el texto

        self.generalLayout.addWidget(self.display)

    def create_buttons(self):
        self.buttons = {}
        # creamos el grid para los botones
        buttonsLayout = QGridLayout()
        # asignamos posiciones y texto mediante un diccionario
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3), 'C': (0, 4),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3), '(': (1, 4),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3), ')': (2, 4),
            '0': (3, 0), '.': (3, 1), '00': (3, 2), '+': (3, 3), '=': (3, 4),
        }
        # creamos y posicionamos los botones
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def set_display(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def get_display(self):
        # obtiene el texto del display
        return self.display.text()

    def clear_display(self):
        # haciendo uso de set_display escribimos en el display ''
        self.set_display('')


# Creamos el controlador para la calculadora:
class Controller:
    def __init__(self, calc, widget):
        self.widget = widget  # hace referencia al elemento a 'controlar'
        self.calc = calc  # hace referencia a la funcion de calculo.
        # obtenemos las pulsaciones
        self.get_puls()

    def calculate(self):
        # calculamos el resultado
        res = self.calc(self.widget.get_display())
        # imprimimos el resultado en el display
        self.widget.set_display(res)

    def build(self, txt):
        # si el calculo se evalua como erroneo, se limpia la pantalla
        if self.widget.get_display() == 'ERROR':
            self.widget.clear_display()
        # obtenemos el texto en el display y le damos el nuevo
        expression = self.widget.get_display() + txt
        # escribimos la nueva cadena de caracteres en la pantalla
        self.widget.set_display(expression)

    def get_puls(self):
        for txt, btn in self.widget.buttons.items():
            if txt not in {'=', 'C'}:
                # escribimos el caracter correspondiente a la pulsacion.
                btn.clicked.connect(partial(self.build, txt))  # nota1

        if self.widget.buttons['='].clicked:
            # en caso de pulsar '=' se retorna el resultado.
            self.widget.buttons['='].clicked.connect(self.calculate)
            self.widget.display.returnPressed.connect(self.calculate)
        if self.widget.buttons['C'].clicked:
            # en caso de pulsar 'C' se limpia la pantalla
            self.widget.buttons['C'].clicked.connect(self.widget.clear_display)


def calc(expression):
    # mediante eval() calcularemos el resultado de la expresion introducida
    try:
        res = str(eval(expression, {}, {}))
    except Exception:
        res = 'ERROR'

    return res


def run():
    # creamos la aplicacion
    calculator = QApplication(sys.argv)
    # Mostramos la aplicacion
    widget = Calculator()
    widget.show()
    # arrancamos el controlador
    Controller(calc, widget)
    # ejecutamos el main loop
    sys.exit(calculator.exec_())


if __name__ == '__main__':
    run()

# __pip__ #
'''
pip install PyQt5

'''

# __NOTES__ #
'''
    Nota 1:
        partial() toma la funcion build y txt y genera una llamada a la funcion
        build() empleando como argumento txt
'''
# __BIBLIOGRAPHY__ #
'''
Main proyect: https://realpython.com/python-pyqt-gui-calculator/
'''
