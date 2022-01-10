import pandas as pd
import time
import requests

def descarga():
    salida = []
    for i in range(1,4):
        try:
            url = f"https://www.infolobby.cl/DatosAbiertos/Catalogos/VirtuosoLobby/Datasets/2021/{i}/pasivos/csv"
            dfOut = pd.read_csv(url)
            salida.append(dfOut.copy())
        except:
            print(url)
    dfFinal = pd.concat(salida)
    dfFinal["Año"] = dfFinal["inicioPasivo"].apply(lambda x: str(x)[0:4])
    return dfFinal

def lecturaCsv():
    df2 = pd.read_csv(r"csvConsolidados/pasivos_consolidado.csv")
    df2["Año"] = df2["inicioPasivo"].apply(lambda x: str(x)[0:4])
    return df2

def extraccionAños():
    df2 = lecturaCsv();
    dfFinal = descarga();

    df2 = df2[df2["Año"] != 2021]
    dfUpdate = dfFinal[dfFinal["Año"]==2021]
    return df2, dfUpdate

def concatenacion():
    df2,dfUpdate = extraccionAños();

    dfConsolidado = pd.concat([df2, dfUpdate])
    with pd.ExcelWriter('InfoLobby/pasivos_consolidado.xlsx',options={'strings_to_urls': False}) as writer:
        dfConsolidado.to_excel(writer, index = False)


if __name__ == '__main__':
    concatenacion();