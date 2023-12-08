# %matplotlib inline

from pathlib import Path

import pandas as pd
import numpy as np
from scipy.stats import trim_mean
import scipy

import seaborn as sns
import matplotlib.pylab as plt


try:
    import common
    DATA = common.dataDirectory()
except ImportError:
    DATA = Path().resolve() / 'data'


DEAD_FAT_CSV = DATA / 'number-of-deaths-by-risk-factor.csv'

MORTALITY_FROM_OBESITY_CSV = DATA / 'share-of-deaths-obesity.csv'


def showObesityDeath():
    state = pd.read_csv(DEAD_FAT_CSV)

    obesityDeads = state[state['Entity'] == 'Mexico'][state['Year'].between(1990, 2019)]['Deaths that are from all causes attributed to high body-mass index, in both sexes aged all ages']

    # # Crear un DataFrame de ejemplo
    data = {'Año': state[state['Year'].between(1990, 2019)]['Year'],
            'Obesity Death': obesityDeads}

    df = pd.DataFrame(data)

    # Crear el gráfico de líneas
    plt.plot(df['Año'], df['Obesity Death'], marker='o', linestyle='-', color='b', label='Obesity Death')

    # Configurar el título y las etiquetas de los ejes
    plt.title('Obesity Deads')
    plt.xlabel('Años (1990 - 2019)')
    plt.ylabel('Yearly Deaths')

    # Mostrar la leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show()


def showObesityMortality():
    state1 = pd.read_csv(MORTALITY_FROM_OBESITY_CSV)

    obesityDeads = state1[state1['Entity'] == 'Mexico'][state1['Year'].between(1990, 2019)]['Share of total deaths that are from all causes attributed to high body-mass index, in both sexes aged age-standardized']


    # # Crear un DataFrame de ejemplo
    data = {'Año': state1[state1['Year'].between(1990, 2019)]['Year'],
            'porsentage of death': obesityDeads}
    df = pd.DataFrame(data)

    # Crear el gráfico de líneas
    plt.plot(df['Año'], df['porsentage of death'], marker='o', linestyle='-', color='b', label='Porsentage of Death')

    # Configurar el título y las etiquetas de los ejes
    plt.title('Mortality from Obesity')
    plt.xlabel('Años (1990 - 2019)')
    plt.ylabel('Yearly Mortality (%)')

    # Mostrar la leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show()




"""
    Show the different tables for comparison in the report
"""
showObesityDeath()

showObesityMortality()