import pandas as pd
import os
from sqlalchemy import create_engine
import funciones

# Crear un dataframe vacío para almacener todos las facturas
df = pd.DataFrame()

# Recorrer todos carpetas dentro de la carpeta "Facturas"
"""
    for carpeta in sorted(os.listdir("./Facturas")):
        ruta_carpeta = os.path.join("./Facturas", carpeta)

        # Recorrer todos los archivos dentro de la carpeta
        for archivo in os.listdir(ruta_carpeta):
            ruta_pdf = os.path.join(ruta_carpeta, archivo)
            print("-" * 50)
            print(f"Procesando {ruta_pdf}")

            # Extraer el texto de la factura
            texto_no_estructurado = funciones.extraer_texto_pdf(ruta_pdf)
            # print("-" * 50)
            # print(texto_no_estructurado)

            # Estructurar el texto de la factura
            texto_estructurado = funciones.estructurar_texto(texto_no_estructurado)
            
            print(texto_estructurado)
"""

# Adaptando para keys de uso gratuito
meses = {
    1: "01-Enero", 2: "02-Febrero", 3: "03-Marzo", 4: "04-Abril",
    5: "05-Mayo", 6: "06-Junio", 7: "07-Julio", 8: "08-Agosto",
    9: "09-Setiembre", 10: "10-Octubre", 11: "11-Noviembre", 12: "12-Diciembre"
}

def obtener_dataframes(mes):
    ruta_carpeta = os.path.join("./Facturas", mes)

    # Contador para limitar a 15 archivos
    contador = 0

    # Recorrer todos los archivos dentro de la carpeta
    for archivo in os.listdir(ruta_carpeta):
        if contador >= 15:  # Detener después de 15 archivos
            break

        ruta_pdf = os.path.join(ruta_carpeta, archivo)
        print("-" * 50)
        print(contador+1)
        print(f"Procesando {ruta_pdf}")

        # Extraer el texto de la factura
        texto_no_estructurado = funciones.extraer_texto_pdf(ruta_pdf)
        # print("-" * 50)
        # print(texto_no_estructurado)

        # Estructurar el texto de la factura
        texto_estructurado = funciones.estructurar_texto(texto_no_estructurado)
        
        print(texto_estructurado)
        # Incrementar el contador
        contador += 1

obtener_dataframes(meses[3])

print("finalizado")