# gemini: pip install google-generativeai
import google.generativeai as genai
from dotenv import load_dotenv
import os
# pip install pymupdf
import fitz #PyMuPDF
from prompt import prompt
import pandas as pd
from io import StringIO
# Cargar variables de entorno desde .env
load_dotenv()
# Obtener la clave de la API desde el archivo .env
api_key = os.getenv("GEMINI_API_KEY")


# print(f"API Key: {api_key}")
# genai.configure(api_key=api_key)
# model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# consulta = "Quien descubrio america"
# response = model.generate_content(consulta)
# print(response.text)

def extraer_texto_pdf(ruta_pdf):
    doc = fitz.open(ruta_pdf) #Abrir el archivo PDF
    texto = "\n".join([pagina.get_text() for pagina in doc]) #Extraer el texto de cada página
    return texto

# Configurar la clave de API
genai.configure(api_key=api_key)

def estructurar_texto(texto):
    """
    Envía el texto a Gemini para obtener una respuesta estructurada en CSV.
    Si no puede procesarlo, devuelve 'error'.
    """

    # Definir el modelo de Gemini
    model = genai.GenerativeModel("gemini-2.0-flash")  # Puedes probar otros modelos

    # Definir el mensaje en el formato correcto
    mensajes = [
        {
            "parts": [{"text": 
                "Eres un experto en extracción de datos de facturas. "
                "Devuelve solo el CSV sin explicaciones ni mensajes adicionales. "
                "Si no puedes extraer datos, devuelve exactamente la palabra 'error'.\n\n"
                f"{prompt} \nEste es el texto a parsear:\n{texto}"
            }]
        }
    ]

    # try:
    # Generar respuesta
    respuesta = model.generate_content(mensajes)

    # Obtener el contenido y eliminar espacios extra
    csv_respuesta = respuesta.text.strip()
    
    return csv_respuesta

    # except Exception as e:
    #     return e

def csv_a_dataframe(csv, archivo):
    """Convierte el texto CSV en un DataFrame de pandas"""

    # Definir el tipo de dato para cada columna
    dtype_cols = {
        # "archivo": str,
        "fecha_factura": str,
        "cantidad": float,
        "descripcion": str,
        "valor_unitario": float,
        "descuento": float,
    }

    # Leer el CSV en un DataFrame con los tipos especificados
    df_temp = pd.read_csv(StringIO(csv), delimiter=";", dtype=dtype_cols)

    return df_temp
