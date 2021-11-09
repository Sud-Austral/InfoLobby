import pandas as pd
import time
import requests

def descarga():
    salida = []
    for i in range(1,4):
        try:
            url = f"https://www.infolobby.cl/DatosAbiertos/Catalogos/VirtuosoLobby/Datasets/2021/{i}/activos/csv"
            dfOut = pd.read_csv(url)
            salida.append(dfOut.copy())
        except:
            print(url)
    dfFinal = pd.concat(salida)
    return dfFinal

def lecturaCsv():
    df2 = pd.read_csv(r"csvConsolidados/activos_consolidado.csv")
    return df2

def concatenacion():
    df2 = extraccionAños();
    dfUpdate = extraccionAños();

    dfConsolidado = pd.concat([df2, dfUpdate])
    with pd.ExcelWriter('activos_consolidado.xlsx',options={'strings_to_urls': False}) as writer:
        dfConsolidado.to_excel(writer, index = False)

def extraccionAños():
    df2 = lecturaCsv();
    dfFinal = descarga();

    df2 = df2[df2["anio"] != 2021]
    dfUpdate = dfFinal[dfFinal["anio"]==2021]
    return df2, dfUpdate



if __name__ == '__main__':
    concatenacion();