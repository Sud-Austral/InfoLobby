import pandas as pd
import time
import requests

def dataSinModificacion(url, ruta):
    try:
        dfDato = pd.read_csv(url, encoding = "ISO-8859-1", sep = ";")
        dfDato.to_excel(ruta, index=False)
    except Exception as e: 
        print (f"Hubo un error en: {url}")
        print ("Código error: "+str(e))

def lecturaArchivos():
    try:
        df = pd.read_excel(r"http://www.cplt.cl/transparencia_activa/datoabierto/archivos/Tipologias%20y%20Asignaciones%20Especiales.xlsx")
        df.to_excel("Asignaciones_Especiales")
    except Exception as e:
        print ("Código error: "+str(e))

def fuente():
    fuente = pd.read_excel(r"Descargas_1.xlsx")
    return fuente

def cargarDatos():
    referencia = fuente()

    for i in range (len(referencia)):
        dataSinModificacion(referencia["URL"][i],referencia["ruta"][i])
        print("Archivo actualizado con éxito")


if __name__ == '__main__':
    #dataSinModificacion(url = '', ruta = '')
    lecturaArchivos()
    cargarDatos()