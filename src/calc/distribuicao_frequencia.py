import pandas as pd
import numpy as np
from math import ceil


def ponto_medio(idade, h, k, ndf):
    series_pm = pd.Series(dtype=float)
    limites = [(idade.min() + i * h, idade.min() + (i + 1) * h) for i in range(k)]
    for limite_inf, limite_sup in limites:
        xi = (limite_inf+limite_sup)/2
        series_pm = pd.concat([series_pm, pd.Series([xi], dtype=float)], ignore_index=True)
    ndf["ponto_médio (xi)"] = series_pm
    return ndf

def filtragem(df):
    age = pd.Series(df.Idade)
    return age


def classes(n):
    cl = np.sqrt(n)  # Aqui tiramos a raíz quadrada de 'n'
    arredonda = round(cl)  # Arredondamos para o inteiro mais próximo
    return arredonda


def amplitude(idade, k):
    a = ceil((idade.max() - idade.min()) / k)  # 'ceil' arredonda (pra cima) para o maior inteiro do decimal
    return a


def tab_frequencia(idade, k, h):
    ndf = pd.DataFrame(columns=["classes", "frequencias (fi)"])

    limites = [(idade.min() + i * h, idade.min() + (i + 1) * h) for i in range(k)]

    for limite_inf, limite_sup in limites:
        freq = ((idade >= limite_inf) & (idade < limite_sup)).sum()
        ndf = pd.concat([ndf, pd.DataFrame({"classes": [f"{limite_inf} |- {limite_sup}"],
                                            "frequencias (fi)": [freq]})], ignore_index=True)

    return ndf


class Frequencia:

    def __init__(self):

        df = pd.DataFrame({
            "Nome": ['Alice', 'Bob', 'Carol', 'David', 'Eva', 'Frank', 'Gina', 'Hector', 'Irene', 'John',
                     'Karen', 'Leo', 'Maria', 'Nathan', 'Olivia', 'Paul', 'Quinn', 'Rachel', 'Steve', 'Tina',
                     'Uriel', 'Victoria', 'Walter', 'Xavier', 'Yvonne', 'Zach', 'Bella', 'Charlie', 'Diana',
                     'Ethan', 'Fiona', 'Greg', 'Hannah', 'Ian', 'Julia', 'Kevin', 'Linda', 'Mike', 'Nora',
                     'Oscar', 'Pam', 'Roger', 'Samantha', 'Tim', 'Ursula', 'Vanessa', 'Will', 'Yasmine', "Daniel",
                     "Victor"],

            "Idade": [25, 30, 35, 40, 45, 27, 32, 37, 42, 47,
                      29, 34, 39, 44, 26, 31, 36, 41, 46, 28,
                      33, 38, 43, 48, 24, 29, 34, 39, 44, 26,
                      31, 36, 41, 46, 28, 33, 38, 43, 48, 24,
                      29, 34, 39, 44, 26, 31, 36, 41, 46, 28]
        })

        idade = filtragem(df)
        n = idade.count()  # Em estatísitca, o número de amostras é dado como 'n'.

        k = classes(n)  # Em estatística, o número de classes é dado como 'k'.
        h = amplitude(idade, k)  # Em estatística, o número da amplitude entre a análise de amostras é dada por 'h'
        novo_dataframe = tab_frequencia(idade, k, h)
        df_df = ponto_medio(idade, h, k, novo_dataframe)

        print(df_df)


frequency = Frequencia()
