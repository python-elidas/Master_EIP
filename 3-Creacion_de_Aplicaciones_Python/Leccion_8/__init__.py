'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Date: 25/05/2021
'''
# __LIBRARIES__ #
from flask import Flask, request
import pandas as pd
import json
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import io
from flask import Response

# __MAIN CODE__ #
# Se crea la aplicacion llamada 'app'
app = Flask(__name__)

# se define el home


@app.route('/')
def home():
    return 'Welcome to Flask API REST'

# Se establace la ruta y el metodo permitido


@app.route('/irisGet/', methods=['GET'])
def irisGet():
    # cargamos el Data Frame
    X_df = pd.read_csv('iris.csv')  # Nota1
    # pasamos el data Frame a json
    describe = X_df.describe().to_json(orient="index")
    # cargamos los datos relevantes del csv; mas, min, avg...
    describe = json.loads(describe)
    return describe


@app.route('/irisPost/', methods=['POST'])
def irisPost():
    data = request.data
    data = json.loads(data)
    # se gusrada en el csv
    with open('iris.csv', 'a', newline='') as csv_a:
        fieldnames = [
            'sepal_length', 'sepal_width',
            'petal_length', 'petal_width',
            'species'
        ]
        writer = csv.DictWriter(csv_a, fieldnames=fieldnames)
        writer.writerow({
            'sepal_length': data['sepal_length'],
            'sepal_width': data['sepal_width'],
            'petal_length': data['petal_length'],
            'petal_width': data['petal_width'],
            'species': data['species']
        })
        print('writing complete!')
    return data


@app.route('/irisPut/', methods=['PUT'])
def irisPut():
    data = request.data
    data = json.loads(data)
    # leemos el csv
    df = pd.read_csv('iris.csv')
    # Nota 2
    # cargamos la infromacion del dato que nos interesa
    df.loc[df.index[-1], 'sepal_length'] = data['sepal_length']
    df.loc[df.index[-1], 'sepal_width'] = data['sepal_width']
    df.loc[df.index[-1], 'petal_length'] = data['petal_length']
    df.loc[df.index[-1], 'petal_width'] = data['petal_width']
    df.loc[df.index[-1], 'species'] = data['species']
    # convertimos a csv y guardamos los cambios
    df.to_csv('iris.csv', index=False)
    result = df.iloc[-1].to_json(orient="index")
    return result


@app.route('/irisDelete/', methods=['DELETE'])
def irisDelete():
    df = pd.read_csv('iris.csv')
    # eliminamos la ultima fila creada
    df.drop(df.index[-1], inplace=True)
    # convertir a csv y guardar cambios
    df.to_csv('iris.csv', index=False)
    result = df.iloc[-1].to_json(orient="index")
    return result


@app.route('/irisGraph/', methods=['GET'])
def irisGraph():
    # leemos el data frame
    df = pd.read_csv('2_IrisSpecies.csv')
    # quitamos la primera columna
    df = df.drop('Id', axis=1)
    plot = sns.FacetGrid(df, hue='Species', height=5.2)\
        .map(plt.scatter, 'PetalLengthCm', 'PetalWidthCm')\
        .add_legend()
    # plt.title('Especies en funcion del Petalo')
    #  MODIFICADO PARA VISUALIZAR BIEN EL TITULO
    plot.fig.suptitle('Especies en función del Pétalo')
    # plt.show()
    # AÑADIDO PARA PODER VISUALIZAR EL GRÁFICO
    # IMPORTAMOS LAS LIBRERIAS io y RESPONSE:
    output = io.BytesIO()
    plot.savefig(output, format='png')
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)

# __NOTES__ #
'''
    Nota1:
        El iris.csv tiene que estar en la carpeta raiz del proyecto

    Nota 2:
        Para hacer mas practico el PUT se debería combinar con una funcion
        find para hallar el indice del dato del que se quiere cambiar la
        informacion.
        Hay que tener cuidado con los nombres de las columnas
        '''
# __BIBLIOGRAPHY__ #
'''

'''
