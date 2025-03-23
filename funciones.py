# gemini: pip install google-generativeai
import google.generativeai as genai
from dotenv import load_dotenv
import os
# pip install pymupdf
import fitz #PyMuPDF
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

