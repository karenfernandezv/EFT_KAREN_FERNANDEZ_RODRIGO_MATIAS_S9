def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    return {"total_carrito": total}

import requests

def exchange_rate(request):
    api_url = 'https://api.exchangeratesapi.io/latest?base=USD'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        rate = data.get('rates', {}).get('CLP', None)
        return {'exchange_rate': rate}
    else:
        return {'exchange_rate': None}



def weather(request):
    api_key = 'bb508796929ab11bb8f94743705fc38b' 
    city = 'santiago'  
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return {'weather_data': weather_data}
    else:
        return {'weather_data': None}
