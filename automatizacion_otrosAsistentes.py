import pandas as pd
import time
import requests

def descarga():
    salida = []
    for i in range(1,4):
        try:
            url = f"https://www.infolobby.cl/DatosAbiertos/Catalogos/VirtuosoLobby/Datasets/2021/{i}/otrosAsistentes/csv"
            dfOut = pd.read_csv(url)
            salida.append(dfOut.copy())
        except:
            print(url)
    dfFinal = pd.concat(salida)
    return dfFinal

def csv():
    df2 = pd.read_csv(r"csvConsolidados/otrosAsistentes_consolidado.csv")
    return df2

def concatenacion():
    dfFinal = descarga()
    df2 = csv()

    dfConsolidado = pd.concat([df2, dfFinal])
    with pd.ExcelWriter('InfoLobby/otrosAsistentes_consolidado.xlsx',options={'strings_to_urls': False}) as writer:
        dfConsolidado.to_excel(writer, index = False)


if __name__ == '__main__':
    concatenacion();