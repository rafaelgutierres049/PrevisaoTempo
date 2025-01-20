import json
import os

SECRETS_FILE = os.path.join(os.path.dirname(__file__), "secrets.json")

def load_secrets():
    try:
        with open(SECRETS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{SECRETS_FILE}' não encontrado")
    except json.JSONDecodeError:
        raise ValueError(f"Erro ao decodificar o arquivo '{SECRETS_FILE}'")
    
CONFIG = {
    "api_url": "https://api.openweathermap.org/data/2.5/weather", # ?Q={city name}&appid={API key}
    "default_city": "São Paulo",
    "units": "metric",  
    "language": "pt_br",
    "secrets": load_secrets(),
}
#