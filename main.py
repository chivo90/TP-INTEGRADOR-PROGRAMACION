print("Sistema de Gestion de Paises")

import csv

def cargar_paises(nombre_archivo):
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter=';')

            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)


    except FileNotFoundError:
        print("Error: No se encontro el archivo")

    return paises

def mostrar_menu():
    print("\n--- GESTION DE PAISES ---")
    print("1. Agregar pais")
    print("2. Actualizar pais")
    print("3. Buscar pais")
    print("4. Filtrar paises")
    print("5. Ordenar paises")
    print("6. Estadisticas")
    print("0. Salir")

def validar_opcion(opcion):
    return opcion in ["0","1","2", "3", "4", "5", "6"]

def agregar_pais(paises):

    nombre = input("Ingrese el nombre del pais: ").strip()

    while nombre == "":
        print("Error: El nombre no puede estar vacio.")
        nombre = input("Ingrese el nombre del pais: ").strip()

    poblacion = int(input("Ingrese poblacion: "))

    while poblacion <=0:
        print("Error: Debe ser mayor que 0")
        poblacion = int(input("Ingrese poblacion: "))

    superficie = int(input("Ingrese superficie: "))

    while superficie <=0:
        print("Error: Debe ser mayor que 0")
        superficie = int(input("Ingrese superficie: "))

    continente = input("Ingrese continente: ").strip()

    while continente =="":
        print("Error: El continente no puede estar vacio")
        continente = input("Ingrese continente: ").strip()

    
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    print("Pais agregado correctamente")

paises = cargar_paises("paises.csv")

for pais in paises:
    print(pais)

while True:
    mostrar_menu()

    opcion = input("Seleccione una opcion: ")

    if not validar_opcion(opcion):
        print("Error: Opcion invalida")
        continue

    if opcion == 0:
        print("Fin del programa")
        break
    
    elif opcion =="1":
        agregar_pais(paises)

        
    print("Funcionalidad en desarrollo")

