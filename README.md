# Reto_13
## Conociendo sobre JSON
##### Primer punto
Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
```python
#Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.

#Funcion para llenar un diccionarios
def llenar_diccionario(elementos):
    lista_lista : list= [] #Se incializa un alista vacía
    for i in range (elementos):
        elemento = []
        clave  = int (input("Ingrese su clave: "))
        valor = str (input("Ingrese el valor: "))
        elemento.append (clave)
        elemento.append (valor) #Se le asigna el valor a la clave
        lista_lista.append (elemento)  #Se va agregando la clave y el valor a la lista vacía
    return lista_lista

#Funcion para organizar los elementos ingresador
def ordenar (elementos):
    lista_lista = llenar_diccionario(elementos) #Se llama la funcion de llenar los diccionarios
    lista_lista.sort() # ordena en orden alfabetico
    diccionario = dict (lista_lista)
    print (diccionario)
    for k,v in diccionario.items(): # tuplas e impresion por consola
        print(k, "->", v)

if __name__ == "__main__":
   elementos: int = int (input("Cuantos elementos desea que tenga el diccionario: "))
   ordenar(elementos)
```
##### Segundo punto
Desarrollar una funci�on que reciba dos diccionarios como par�ametros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.
```python
#Funcion para llenar un diccionarios
def llenar_diccionario(dicc : dict):
    elementos = int (input("¿Cuantos elemento dese que tenga el diccionario?: "))
    for k in range (elementos):
        clave  = (input("Ingrese su clave: "))
        valor = (input(f"Ingrese el valor para la clave '{clave}': "))#Se le asigna el valor a la clave
        dicc[clave] = valor
    for k,v in dicc.items(): # tuplas
        print(k, "->", v)
    return dicc


def dejar_primer_valor(dicc_1, dicc_2):
    # Encontrar las claves comunes
    clave_comun = set(dicc_1.keys()) & set(dicc_2.keys())

    # Verificar si no hay claves comunes
    if not clave_comun:
        print("No hay claves en común entre los dos diccionarios.")
        return dicc_2
    # Recorrer las claves comunes y eliminar de dicc_2 las que tengan el mismo valor en ambos diccionarios
    for clave in clave_comun:
        del dicc_2[clave]  # Eliminar la clave de dicc_2 si el valor es igual
    return dicc_2  # Retornar el diccionario después de recorrer todas las claves comunes


if __name__ == "__main__":
    dicc_1 = {} #Se crean los diccionarios vacios
    dicc_2 = {}
    
    #Se utiliza la funcion para llenar los diccionarios
    print("Llenar el primer diccionario")
    dicc_1 = llenar_diccionario(dicc_1)
    
    print("Llenar el segundo diccionario")
    dicc_2 = llenar_diccionario(dicc_2)
    dicc_nuevo = dejar_primer_valor(dicc_1, dicc_2)
    dicc_1.update(dicc_nuevo) #Mezcla los diccionarios

    print (f"El nuevo diccionario es: {dicc_1}")
```
##### Tercer punto
Dado el JSON:
```python
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "D��az Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["F�utbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```
Cree un programa que lea de un archivo con dicho JSON y:
- Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
- Imprima los nombres completos (nombre y apellidos) de las personas que est�en en un rango de edades dado por el usuario.

```python

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
```
