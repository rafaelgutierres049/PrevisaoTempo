from flask import render_template, request
from app import flask_app
from app.api_requests import get_weather_data

@flask_app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error_message = None
    background_class = "temperado"

    if request.method == 'POST':
        city_name = request.form.get('city_name')
        if city_name:
            weather_data = get_weather_data(city_name)
            if not weather_data:
                error_message = "Cidade não encontrada. Verifique o nome e tente novamente."
            else:
                temperatura = weather_data.get('temperatura', 20)  # Define um padrão
                if temperatura < 0:
                    background_class = "muito-frio"
                elif 0 <= temperatura < 10:
                    background_class = "frio"
                elif 10 <= temperatura < 20:
                    background_class = "temperado"
                elif 20 <= temperatura < 30:
                    background_class = "quente"
                else:
                    background_class = "muito-quente"

    return render_template('home.html', weather_data=weather_data, error_message=error_message, background_class=background_class)
