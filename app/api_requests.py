import sys
import os
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.config import CONFIG

def build_url_request(city_name: str):
    base_url = CONFIG['api_url']
    api_key = CONFIG['secrets']['api_key']
    url = f'{base_url}?q={city_name}&appid={api_key}&units=metric&lang=pt_br'
    return url

def get_weather_data(city_name: str):
    url = build_url_request(city_name)
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        main_data = weather_data.get('main', {})

        print(main_data)  # Verifique o que está sendo retornado

        temp = round((main_data.get('temp')), 2) if main_data.get('temp') else 'Não disponível'
        temp_feels_like = round((main_data.get('feels_like')), 2) if main_data.get('feels_like') else 'Não disponível'
        max_temp = round((main_data.get('temp_max')), 2) if main_data.get('temp_max') else 'Não disponível'
        min_temp = round((main_data.get('temp_min')), 2) if main_data.get('temp_min') else 'Não disponível'
        humidity = main_data.get('humidity', 'Não disponível')
        description = weather_data.get('weather', [{}])[0].get('description', 'Não disponível')
        clouds = weather_data.get('clouds', {}).get('all', 'Não disponível')

        data = {
            'cidade': weather_data.get('name'),
            'temperatura': temp,
            'sensacao': temp_feels_like,
            'maxima': max_temp,
            'minima': min_temp,
            'umidade': humidity,
            'condicao': description,
            'nuvens': clouds
        }

        return data
    else:
        print(f'Erro ao buscar os dados: {response.status_code}')
        return None
