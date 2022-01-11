import pandas as pd
import time
import requests

def descarga():
    salida = []
    for i in range(1,4):
        try:
            url = f"https://www.infolobby.cl/DatosAbiertos/Catalogos/VirtuosoLobby/Datasets/2021/{i}/asistenciasPasivos/csv"
            dfOut = pd.read_csv(url)
            salida.append(dfOut.copy())
        except:
            print(url)
    dfFinal = pd.concat(salida)
    return dfFinal

def concatenacion():
    dfFinal = descarga()

    with pd.ExcelWriter('InfoLobby/pasivos_consolidado.xlsx',options={'strings_to_urls': False}) as writer:
        dfFinal.to_excel(writer, index = False)


if __name__ == '__main__':
    concatenacion();