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

paises = cargar_paises("paises.csv")

for pais in paises:
    print(pais)