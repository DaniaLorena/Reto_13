import requests
import json

# Función para imprimir los pares de llave: valor de un JSON
def print_key_value_pairs(data):
    for key, value in data.items():
        print(f'{key}: {value}')

# API 1: Datos meteorológicos (ejemplo de OpenWeatherMap)
url_1 = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m"
weather_response = requests.get(url_1)
weather_data = weather_response.json()
print("Datos meteorológicos:")
print_key_value_pairs(weather_data)
print("\n")

# API 2: Imágenes de perros
url_2= "https://dog.ceo/api/breeds/image/random"
dog_response = requests.get(url_2)
dog_data = dog_response.json()
print("Imagen de perro:")
print_key_value_pairs(dog_data)
print("\n")

# API 3: Feriados públicos (ejemplo de Nager.Date)
url_3 = "https://date.nager.at/api/v2/publicholidays/2024/US"
holidays_response = requests.get(url_3)
holidays_data = holidays_response.json()
print("Feriados públicos:")
for holiday in holidays_data:
    print_key_value_pairs(holiday)
    print("\n")
