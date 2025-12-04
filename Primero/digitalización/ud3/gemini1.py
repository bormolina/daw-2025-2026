from google import genai
from api_key import get_api_key

client = genai.Client(api_key=get_api_key())

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Esto es una prueba de conexión a la API de Gemini desde Python. Dime que son las list comprehensions en Python.",
)

print(response.text)