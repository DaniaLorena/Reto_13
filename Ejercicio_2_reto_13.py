

def llenar_diccionario(dicc : dict):
    elementos = int (input("¿Cuantos elemento dese que tenga el diccionario?: "))
    for k in range (elementos):
        clave  = (input("Ingrese su clave: "))
        valor = (input(f"Ingrese el valor para la clave '{clave}': "))
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
    dicc_1 = {}
    dicc_2 = {}
    
    print("Llenar el primer diccionario")
    dicc_1 = llenar_diccionario(dicc_1)
    
    print("Llenar el segundo diccionario")
    dicc_2 = llenar_diccionario(dicc_2)
    dicc_nuevo = dejar_primer_valor(dicc_1, dicc_2)
    dicc_1.update(dicc_nuevo)

    print (f"El nuevo diccionario es: {dicc_1}")


