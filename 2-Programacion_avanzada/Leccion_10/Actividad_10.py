'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Date: 2021-04-28
'''
# __LIBRARIES__ #
from flask import Flask


# __MAIN CODE__ #
app = Flask(__name__)  # se arranca la pagina web


@app.route('/')
def hola_mundo():
    return '<h1> Hola Mundo con Flask <h1>'


if __name__ == '__main__':
    app.run(debug=True)
# __NOTES__ #
'''
    En este caso se ha reducido el codigo a realizar la tarea es decir,
    unicamente se ha creado una funcio que imprima el testo 'Hola Mundo con
    Flask'
'''
# __BIBLIOGRAPHY__ #
'''

'''
