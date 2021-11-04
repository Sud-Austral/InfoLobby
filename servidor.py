import pandas as pd
import time
import requests

def descarga():
    salida11 = []
    for i in (2022):
        for j in range(1,5):
            try:
                url = f"https://www.infolobby.cl/DatosAbiertos/Catalogos/VirtuosoLobby/Datasets/{i}/{j}/donativos/csv"
                dfOut = pd.read_csv(url)
                #dfOut.to_excel(f"activos_{i}_{j}.xlsx", index = False)
                salida11.append(dfOut.copy())
            except:
                print(url)
    dfFinal = pd.concat(salida11)
    dfFinal.to_csv("donativos_consolidado.csv", index = False)


if __name__ == '__main__':
    descarga()