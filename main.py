import pandas as pd
import os
from sqlalchemy import create_engine

# Crear un dataframe vacío para almacener todos las facturas
df = pd.DataFrame()

# Recorrer todos carpetas dentro de la carpeta "Facturas"
for carpeta in sorted(os.listdir("./Facturas")):
    ruta_carpeta = os.path.join("./Facturas", carpeta)

    # Recorrer todos los archivos dentro de la carpeta
    for archivo in os.listdir(ruta_carpeta):
        ruta_pdf = os.path.join(ruta_carpeta, archivo)
        
        print(f"Procesando {ruta_pdf}")

print("finalizado")