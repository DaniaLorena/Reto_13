import json

persona = {
    "jadiazcoronado": {
        "nombres": "Juan Antonio",
        "apellidos": "Díaz Coronado",
        "edad": 19,
        "colombiano": True,
        "deportes": ["Fútbol", "Ajedrez", "Gimnasia"]
    },
    "dmlunasol": {
        "nombres": "Dorotea Maritza",
        "apellidos": "Luna Sol",
        "edad": 25,
        "colombiano": False,
        "deportes": ["Baloncesto", "Ajedrez", "Gimnasia"]
    }
}

#Ingresa por teclado el deporte
deporte = input("Ingrese el deporte: ")

#Se recorre el JSON (llave, valor), si el deporte se encuentre el algun valor retorna el nombre
for k, v in persona.items():
    if deporte in v["deportes"]:
        print(f'{v["nombres"]} {v["apellidos"]} practica {deporte}')
        
# Imprimir los nombres completos de las personas dentro del rango de edades

#Se pide al usuario un rango de edad
edad_minima = int(input("Ingrese la edad mínima: "))
edad_maxima = int(input("Ingrese la edad máxima: "))

#Se recorre el JSON (llave, valor), si hay alguien entre el rango de edad retornara el nombre y el apellido
for k, v in persona.items():
    if edad_minima <= v["edad"] <= edad_maxima:
        print(f'{v["nombres"]} {v["apellidos"]}')