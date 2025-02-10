import requests

# Datos sensibles ficticios
API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
DB_PASSWORD = "supersecretpassword123"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxxxx"

# Función para mostrar los datos
def mostrar_datos():
    print(f"API Key: {API_KEY}")
    print(f"DB Password: {DB_PASSWORD}")
    print(f"AWS Access Key: {AWS_ACCESS_KEY}")
    print(f"GitHub Token: {GITHUB_TOKEN}")

# Simulando una llamada a una API con la clave
def llamada_api():
    url = "https://api.ejemplo.com/obtener_datos"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    mostrar_datos()
    llamada_api()
