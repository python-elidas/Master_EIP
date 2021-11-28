'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Python Version: 3.6.9
Version: 0.0.1
'''
# __LIBRARIES__ #
import pandas as pd
import plotly.graph_objects as go


# __MAIN CODE__ #
class CSV:
    def __init__(self, file):
        self.df = pd.read_csv(file, delimiter='\t')
        self.verify()
        self.clean()
        self.get_month_spend()
        self.get_month_income()
        self.get_month_save()

    def verify(self):
        year = [
            'Enero', 'Febrero', 'Marzo',
            'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre',
            'Octubre', 'Noviembre', 'Diciembre']
        values = [0 for i in range(100)]
        for month in year:
            try:
                if self.df[month].dropna().empty:
                    raise Exception
            except KeyError:
                print(f'Falta {month}, se tomará como nulo.')
                self.df.insert(
                    year.index(month),
                    month,
                    values
                )
            except Exception:
                print(f'Faltan valores en {month}, se tomara como nulo.')

    def clean(self):
        for col in self.df.columns:
            for item in self.df[col]:
                # n += 1
                if type(item) is str:
                    # print(f'Elemto {n}: {item}, Type: {type(item)}')
                    if item.startswith('\''):
                        self.df[col] = self.df[col].replace(
                            [item], int(item[1:-1]))
                    else:
                        try:
                            self.df[col] = self.df[col].replace(
                                [item], int(item))
                        except ValueError:
                            self.df[col] = self.df[col].replace([item], 0)
                elif item is None:
                    self.df[col] = self.df[col].replace([item], 0)

    def get_month_spend(self):
        self.spend = dict()  # Guarda el gasto de cada mes
        self.sp_t = 0  # guarda el gasto total a lo largo del año
        for col in self.df.columns:
            spend = 0
            for item in self.df[col]:
                if item < 0:
                    spend += item
            self.spend[col] = spend
            self.sp_t += spend
        self.sp_avg = round(self.sp_t / 12, 2)  # Guarda la media de gasto
        return (self.sp_t, self.spend)

    def get_month_income(self):
        self.income = dict()
        self.ic_t = 0  # guarda el ingreso total a lo largo del año.
        for col in self.df.columns:
            save = 0
            for item in self.df[col]:
                if item > 0:
                    save += item
            self.income[col] = save
            self.ic_t += save
        return (self.ic_t, self.income)

    def get_month_save(self):
        self.save = dict()
        for col in self.df.columns:
            self.save[col] = self.income[col] + self.spend[col]
        return self.save

    def gen_graph(self):
        while True:
            try:
                show = int(input(
                    '\nIntroduzca la grafica a mostrar(1, 2, 3):\
                    \n\t1) Evolución de los ingresos.\
                    \n\t2) Evolución de los gastos.\
                    \n\t3) Evolucion de los ahorros.\
                    \n>>>'
                ))
                if 1 > show or show > 3:
                    raise ValueError
                break
            except ValueError:
                print('Caracter no valido.')

        fig = go.Figure()
        fig.update_layout(
            title=self.select_tittle(show),
            xaxis_title='Mes',
            yaxis_title='Valor'
        )
        fig.add_trace(self.select_case(show))
        fig.show()

    def select_case(self, case):
        cases = {
            1: go.Scatter(
                x=list(self.income.keys()),
                y=list(self.income.values()),
                mode='lines',
                name='Ingreso'
            ),
            2: go.Scatter(
                x=list(self.spend.keys()),
                y=list(self.spend.values()),
                mode='lines',
                name='Gasto'
            ),
            3: go.Scatter(
                x=list(self.save.keys()),
                y=list(self.save.values()),
                mode='lines',
                name='Ahorro'
            )
        }
        return cases[case]

    def select_tittle(self, case):
        title = {
            1: 'Evolución de los ingresos',
            2: 'Evolución de los gastos.',
            3: 'Evolucion de los ahorros.'
        }
        return title[case]

    def print_info(self):
        print('\nGASTO \nMensual:')
        max = 0
        month = str()
        for i in self.spend:
            if self.spend[i] < max:
                max = self.spend[i]
                month = i
            print(f'\t{i}: {self.spend[i]}')
        print(
            f'\nMes con mayor gasto: {month}({max})\
            \nLa media de gasto Mensual ha sido: {self.sp_avg}\
            \nEl gasto total a lo largo del año ha sido: {self.sp_t}')

        print(f'\nEl ingreso total a lo largo del año ha sido: {self.ic_t}')

        print('\nAHORRO \nMensual:')
        max = 0
        month = str()
        for i in self.save:
            if self.save[i] > max:
                max = self.save[i]
                month = i
            print(f'\t{i}: {self.save[i]}')
        print(f'\nMes con mayor ahorro: {month}({max})')

        print(f'\nEl valance al finalizar el año es: {self.ic_t - self.sp_t}\n')


def run():
    file = CSV('finanzas2020.csv')
    file.print_info()
    input('Presione Enter... \n>>> ')
    file.gen_graph()


if __name__ == '__main__':
    run()
# __NOTES__ #
'''


'''
# __BIBLIOGRAPHY__ #
'''

'''
