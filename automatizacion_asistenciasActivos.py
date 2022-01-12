import pandas as pd
import time
import requests

def descarga():
    salida = []
    for i in range(1,4):
        try:
            url = f"https://www.infolobby.cl/DatosAbiertos/Catalogos/VirtuosoLobby/Datasets/2021/{i}/asistenciasActivos/csv"
            dfOut = pd.read_csv(url)
            salida.append(dfOut.copy())
        except:
            print(url)
    dfFinal = pd.concat(salida)
    return dfFinal

def lecturaCsv():
    df2 = pd.read_csv(r"csvConsolidados/asistenciasActivos2.csv")
    df3 = pd.read_csv(r"csvConsolidados/asistenciasActivos1.csv")

    dfConcat = pd.concat ([df2, df3])
    return dfConcat


def concatenacion():
    dfFinal = descarga()
    dfConcat = lecturaCsv()

    dfConsolidado = pd.concat([dfConcat, dfFinal])
    with pd.ExcelWriter('InfoLobby/asistenciasActivos_consolidado.xlsx',options={'strings_to_urls': False}) as writer:
        dfConsolidado.to_excel(writer, index = False)

if __name__ == '__main__':
    concatenacion();