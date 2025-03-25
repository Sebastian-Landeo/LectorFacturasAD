import pandas as pd
import os
import pymysql
import funciones
from dotenv import load_dotenv
# Cargar variables de entorno desde .env
load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = int(os.getenv('DB_PORT'))
# Crear la conexión a MySQL
conn = pymysql.connect(
    host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT
)
cursor = conn.cursor()

# Adaptando para keys de uso gratuito
meses = {
    1: "01-Enero", 2: "02-Febrero", 3: "03-Marzo", 4: "04-Abril",
    5: "05-Mayo", 6: "06-Junio", 7: "07-Julio", 8: "08-Agosto",
    9: "09-Setiembre", 10: "10-Octubre", 11: "11-Noviembre", 12: "12-Diciembre"
}

def obtener_dataframes(mes):
    df = pd.DataFrame()
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

        # Convertir el texto estructurado en un DataFrame
        df_factura = funciones.csv_a_dataframe(texto_estructurado, archivo)
        print(df_factura["numero_factura"])

        # Anexar el dataframe de la factura al dataframe general
        df = pd.concat([df, df_factura], ignore_index=True)
        
       
        # Incrementar el contador
        contador += 1
        # Exportar a CSV
        df.to_csv(f"{mes}.csv", index=False)

    return df

# Obtner el DataFrame de un mes específico
df = obtener_dataframes(meses[8])

# Función para insertar valores en otras tablas
def insertar_datos(tabla, columnas):
    valores = df[list(columnas)].copy()  # Copia para evitar modificar el DataFrame original

    # Convertir la fecha al formato correcto (YYYY-MM-DD)
    if 'fecha_factura' in valores.columns:
        valores['fecha_factura'] = pd.to_datetime(valores['fecha_factura'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    placeholders = ', '.join(['%s'] * len(columnas))
    sql = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({placeholders})"

    for _, row in valores.iterrows():
        cursor.execute(sql, tuple(row))


# Insertar datos en la tabla 'factura'
insertar_datos('factura', ['numero_factura', 'fecha_factura', 'cantidad', 'descripcion', 'valor_unitario', 'descuento', 'proveedor'])

# Confirmar cambios y cerrar conexión
conn.commit()
cursor.close()
conn.close()

print("finalizado")