import csv

print("Sistema de Gestion de Paises")

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

    while True:
        try:
            nombre = input("Ingrese el nombre del pais: ").strip()
            if nombre == "":
                raise ValueError
            break
        except ValueError:
            print("Error: El nombre no puede estar vacio.")

    while True:
        try:
            poblacion = int(input("Ingrese poblacion: "))
            if poblacion <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un numero mayor que 0.")

    while True:
        try:
            superficie = int(input("Ingrese superficie: "))
            if superficie <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un numero mayor que 0.")

    while True:
        try:
            continente = input("Ingrese continente: ").strip()
            if continente == "":
                raise ValueError
            break
        except ValueError:
            print("Error: El continente no puede estar vacio.")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    print("Pais agregado correctamente")


def buscar_pais(paises):

    while True:
        try:
            nombre_buscado = input("Ingrese el nombre del pais: ").strip()
            if nombre_buscado == "":
                raise ValueError
            break
        except ValueError:
            print("Error: Debe ingresar un nombre.")

    encontrados = []

    for pais in paises:
        if nombre_buscado.lower() in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron paises.")
    else:
        print("\nResultados encontrados:\n")
        for pais in encontrados:
            print(
                f"Nombre: {pais['nombre']} | "
                f"Poblacion: {pais['poblacion']} | "
                f"Superficie: {pais['superficie']} km² | "
                f"Continente: {pais['continente']}"
            )

def actualizar_pais(paises):

    while True:
        try:
            nombre = input("Ingrese el nombre del pais a actualizar: ").strip()
            if nombre == "":
                raise ValueError
            break
        except ValueError:
            print("Error: Debe ingresar un nombre de pais.")

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            print("\nPais encontrado")
            print(f"Nombre: {pais['nombre']}")
            print(f"Poblacion actual: {pais['poblacion']}")
            print(f"Superficie actual: {pais['superficie']}")

            while True:
                try:
                    poblacion = int(input("Ingrese nueva poblacion: "))
                    if poblacion <= 0:
                        raise ValueError
                    pais["poblacion"] = poblacion
                    break
                except ValueError:
                    print("Error: Ingrese un numero entero mayor que 0.")

            while True:
                try:
                    superficie = int(input("Nueva superficie: "))
                    if superficie <= 0:
                        raise ValueError
                    pais["superficie"] = superficie
                    break
                except ValueError:
                    print("Error: Ingrese un numero entero mayor que 0.")

            print("Pais actualizado correctamente.")
            return

    print("No se encontro el pais.")

def mostrar_menu_filtros():
    print("\n---FILTROS---")
    print("1. Filtrar por continente.")
    print("2. Filtrar por rango de poblacion.")
    print("3. Filtrar por rango de superficie.")
    print("0. Volver.")

def filtrar_continente(paises):

    while True:
        try:
            continente = input("Ingrese el continente: ").strip()
            if continente == "":
                raise ValueError
            break
        except ValueError:
            print("Error: Debe ingresar un continente.")

    encontrados = False

    print("\nPaises encontrados:\n")

    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            print(f"{pais['nombre']} - {pais['continente']}")
            encontrados = True

    if not encontrados:
        print("No se encontraron paises")

def filtrar_poblacion(paises):

    while True:
        try:
            minimo = int(input("Ingrese la poblacion minima: ").strip())
            if minimo <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: ingrese un numero entero mayor que 0.")

    # NUEVO: pide el maximo y valida que sea mayor al minimo
    while True:
        try:
            maximo = int(input("Ingrese la poblacion maxima: ").strip())
            if maximo <= minimo:
                raise ValueError
            break
        except ValueError:
            print("Error: ingrese un numero entero mayor que el minimo.")

    encontrados = False

    print("\nPaises encontrados:\n")

    for pais in paises:

        # MODIFICADO: ahora filtra por rango (minimo Y maximo)
        if pais["poblacion"] >= minimo and pais["poblacion"] <= maximo:
            print(f"{pais['nombre']} - {pais['poblacion']} habitantes")
            encontrados = True

    if not encontrados:
        print("No se encontraron paises.")

def filtrar_superficie(paises):

    while True:
        try:
            minimo = int(input("Ingrese la superficie minima: ").strip())
            if minimo <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: ingrese un numero entero mayor que 0.")

    # NUEVO: pide el maximo y valida que sea mayor al minimo
    while True:
        try:
            maximo = int(input("Ingrese la superficie maxima: ").strip())
            if maximo <= minimo:
                raise ValueError
            break
        except ValueError:
            print("Error: ingrese un numero entero mayor que el minimo.")

    encontrados = False

    print("\nPaises encontrados:\n")

    for pais in paises:

        # MODIFICADO: ahora filtra por rango (minimo Y maximo)
        if pais["superficie"] >= minimo and pais["superficie"] <= maximo:
            print(f"{pais['nombre']} - {pais['superficie']} km²")
            encontrados = True

    if not encontrados:
        print("No se encontraron paises.")

def menu_filtros(paises):

    while True:

        mostrar_menu_filtros()

        try:
            opcion = input("Seleccione una opcion: ").strip()

            if opcion not in ["0", "1", "2", "3"]:
                raise ValueError

            if opcion == "1":
                filtrar_continente(paises)
            elif opcion == "2":
                filtrar_poblacion(paises)
            elif opcion == "3":
                filtrar_superficie(paises)
            elif opcion == "0":
                print("Volviendo al menu principal...")
                break

        except ValueError:
            print("Error: opcion invalida. Intente nuevamente.")


paises = cargar_paises("paises.csv")

while True:
    mostrar_menu()

    opcion = input("Seleccione una opcion: ")

    if not validar_opcion(opcion):
        print("Error: Opcion invalida")
        continue

    if opcion == "0":
        print("Fin del programa")
        break

    elif opcion == "1":
        agregar_pais(paises)

    elif opcion == "2":
        actualizar_pais(paises)

    elif opcion == "3":
        buscar_pais(paises)

    elif opcion == "4":
        menu_filtros(paises)

    elif opcion == "5":
        print("Opcion en desarrollo")

    elif opcion == "6":
        print("Opcion en desarrollo")

    else:
        print("Opcion invalida.")
