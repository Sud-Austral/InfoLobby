import pandas as pd
import time
import requests

def descarga():
    salida = []
    for i in range(1,4):
        try:
            url = f"https://www.infolobby.cl/DatosAbiertos/Catalogos/VirtuosoLobby/Datasets/2021/{i}/viajes/csv"
            dfOut = pd.read_csv(url)
            salida.append(dfOut.copy())
        except:
            print(url)
    dfFinal = pd.concat(salida)
    dfFinal["Año"] = dfFinal["fechaInicio"].apply(lambda x: str(x)[0:4])

    return dfFinal

def lecturaCsv():
    df2 = pd.read_csv(r"csvConsolidados/viajes2.csv")
    df3 = pd.read_csv(r"csvConsolidados/viajes1.csv")

    dfConcat = pd.concat ([df2, df3])
    dfConcat["Año"] = dfConcat["fechaInicio"].apply(lambda x: str(x)[0:4])
    return dfConcat

def extraccionAños():
    dfConcat = lecturaCsv();
    dfFinal = descarga();

    dfConcat = dfConcat[dfConcat["Año"] != 2021]
    dfUpdate = dfFinal[dfFinal["Año"]==2021]
    return dfConcat, dfUpdate

def concatenacion():
    dfConcat,dfUpdate = extraccionAños();

    dfConsolidado = pd.concat([dfConcat, dfUpdate])
    with pd.ExcelWriter('InfoLobby/viajes_consolidado.xlsx',options={'strings_to_urls': False}) as writer:
        dfConsolidado.to_excel(writer, index = False)


if __name__ == '__main__':
    concatenacion();