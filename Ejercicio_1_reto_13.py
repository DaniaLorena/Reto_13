#Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.

def llenar_diccionario(elementos):
    lista_lista = []
    for i in range (elementos):
        elemento = []
        clave  = int (input("Ingrese su clave: "))
        valor = str (input("Ingrese el valor: "))
        elemento.append (clave)
        elemento.append (valor)
        lista_lista.append (elemento)
    return lista_lista

def ordenar (elementos):
    lista_lista = llenar_diccionario(elementos)
    lista_lista.sort()
    diccionario = dict (lista_lista)
    print (diccionario)
    for k,v in diccionario.items(): # tuplas
        print(k, "->", v)

if __name__ == "__main__":
   elementos: int = int (input("Cuantos elementos desea que tenga el diccionario: "))
   ordenar(elementos)