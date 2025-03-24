import pandas as pd
import os
from sqlalchemy import create_engine
import funciones

# Crear un dataframe vacío para almacener todos las facturas
df = pd.DataFrame()

# Recorrer todos carpetas dentro de la carpeta "Facturas"
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
print("finalizado")