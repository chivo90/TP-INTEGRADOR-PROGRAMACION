# ====================================================
# Sistema de Gestión de Países
# Permite cargar, agregar, buscar, actualizar,
# filtrar, ordenar y mostrar estadísticas de países.
# Los datos iniciales se leen desde un archivo CSV.
# ====================================================
import csv

# Titulo del programa
print("Sistema de Gestion de Paises")

#----------------------------------------------------
# Funcion para cargar los paises desde un archivo CSV
#----------------------------------------------------
def cargar_paises(nombre_archivo):
    
    # Lista donde se almacenan todos los paises
    paises = []

    try:
        # Abrimos el archivo en modo lectura
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter=';')

            # Recorremos cada fila del archivo
            for fila in lector:
                # Creamos un diccionario con los datos del pais
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                
                # Agregamos el pais a la lista
                paises.append(pais)

    # Si el archivo no existe mostramos un error
    except FileNotFoundError:
        print("Error: No se encontro el archivo")

    # Devolvemos la lista de paises cargados
    return paises

#---------------------------------------
# Funcion para mostrar el menu principal
#---------------------------------------
def mostrar_menu():
    print("\n--- GESTION DE PAISES ---")
    print("1. Agregar pais")
    print("2. Actualizar pais")
    print("3. Buscar pais")
    print("4. Filtrar paises")
    print("5. Ordenar paises")
    print("6. Estadisticas")
    print("0. Salir")

#--------------------------------------------------------
# Funcion para verificar si la opcion ingresada es valida
#--------------------------------------------------------
def validar_opcion(opcion):
    return opcion in ["0","1","2", "3", "4", "5", "6"]

#-------------------------------------
# Funcion para agregar pais a la lista
#-------------------------------------
def agregar_pais(paises):

    # Validacion del nombre
    while True:
        try:
            nombre = input("Ingrese el nombre del pais: ").strip()
            if nombre == "":
                raise ValueError
            break
        except ValueError:
            print("Error: El nombre no puede estar vacio.")

    # Validacion de la poblacion
    while True:
        try:
            poblacion = int(input("Ingrese poblacion: "))
            if poblacion <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un numero mayor que 0.")

    # Validacion de la superficie
    while True:
        try:
            superficie = int(input("Ingrese superficie: "))
            if superficie <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un numero mayor que 0.")

    # Validacion del continente
    while True:
        try:
            continente = input("Ingrese continente: ").strip()
            if continente == "":
                raise ValueError
            break
        except ValueError:
            print("Error: El continente no puede estar vacio.")

    # Creamos el diccionario del nuevo pais
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    #Lo agregamos a la lista
    paises.append(nuevo_pais)
    print("Pais agregado correctamente")

#---------------------------------------
# Funcion para buscar un pais por nombre
#---------------------------------------
def buscar_pais(paises):

    # Validacion del nombre
    while True:
        try:
            nombre_buscado = input("Ingrese el nombre del pais: ").strip()
            if nombre_buscado == "":
                raise ValueError
            break
        except ValueError:
            print("Error: Debe ingresar un nombre.")

    encontrados = []

    # Recorremos la lista buscando coincidencias
    for pais in paises:
        if nombre_buscado.lower() in pais["nombre"].lower():
            encontrados.append(pais)
    
    # Mostramos los resultados
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

#----------------------------------------------------------
# Funcion para actualizar poblacion y superficie de un pais
#----------------------------------------------------------
def actualizar_pais(paises):

    # Validacion del nombre
    while True:
        try:
            nombre = input("Ingrese el nombre del pais a actualizar: ").strip()
            if nombre == "":
                raise ValueError
            break
        except ValueError:
            print("Error: Debe ingresar un nombre de pais.")

    # Recorremos la lista para buscar el pais
    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            print("\nPais encontrado")
            print(f"Nombre: {pais['nombre']}")
            print(f"Poblacion actual: {pais['poblacion']}")
            print(f"Superficie actual: {pais['superficie']}")

            # Validamos y actualizamos la poblacion
            while True:
                try:
                    poblacion = int(input("Ingrese nueva poblacion: "))
                    if poblacion <= 0:
                        raise ValueError
                    pais["poblacion"] = poblacion
                    break
                except ValueError:
                    print("Error: Ingrese un numero entero mayor que 0.")

            # Validamos y actualizamos la superficie
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

#----------------------------------------
# Funcion para mostrar el menu de filtros
#----------------------------------------
def mostrar_menu_filtros():
    print("\n---FILTROS---")
    print("1. Filtrar por continente.")
    print("2. Filtrar por rango de poblacion.")
    print("3. Filtrar por rango de superficie.")
    print("0. Volver.")

#-------------------------------------------
# Funcion para filtrar paises por continente
#-------------------------------------------
def filtrar_continente(paises):

    # Validacion del continente
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

    # Mostramos solo los paises del continente indicado
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            print(f"{pais['nombre']} - {pais['continente']}")
            encontrados = True

    if not encontrados:
        print("No se encontraron paises")

#------------------------------------------
# Funcion para filtrar paises por poblacion
#------------------------------------------
def filtrar_poblacion(paises):

    #Validacion de la poblacion minima
    while True:
        try:
            minimo = int(input("Ingrese la poblacion minima: ").strip())
            if minimo <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: ingrese un numero entero mayor que 0.")

    # Validamos el maximo y verificamos que sea mayor al minimo
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

    # Mostramos los paises cuya poblacion esta dentro del rango
    for pais in paises:

        if pais["poblacion"] >= minimo and pais["poblacion"] <= maximo:
            print(f"{pais['nombre']} - {pais['poblacion']} habitantes")
            encontrados = True

    if not encontrados:
        print("No se encontraron paises.")

#----------------------------------------------------
# Funcion para filtrar paises por rango de superficie
#----------------------------------------------------
def filtrar_superficie(paises):

    #Validacion de la superficie minima
    while True:
        try:
            minimo = int(input("Ingrese la superficie minima: ").strip())
            if minimo <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: ingrese un numero entero mayor que 0.")

    # Validamos el maximo y verificamos que sea mayor al minimo
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

    # Mostramos los paises cuya superficie esta dentro del rango
    for pais in paises:

        if pais["superficie"] >= minimo and pais["superficie"] <= maximo:
            print(f"{pais['nombre']} - {pais['superficie']} km²")
            encontrados = True

    if not encontrados:
        print("No se encontraron paises.")

#------------------------------------------
# Funcion para controlar el menu de filtros
#------------------------------------------
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

#----------------------------------------------
# Funcion para mostrar el menu de ordenamientos
#----------------------------------------------
def mostrar_menu_ordenamiento():
    print("\n--- ORDENAR PAISES ---")
    print("1. Ordenar por nombre")
    print("2. Ordenar por poblacion")
    print("3. Ordenar por superficie")
    print("0. Volver")

#-------------------------------------------------------------
# Funcion para ordenar la lista segun el criterio seleccionado
# ----------------------------------------------------------- 
def ordenar_paises(paises, criterio, descendente):
    # sorted() devuelve una nueva lista ordenada
    return sorted(paises, key=lambda pais: pais[criterio], reverse=descendente)

#-----------------------------------------------
# Funcion para controlar el menu de ordenamiento
#-----------------------------------------------
def menu_ordenamiento(paises):

    while True:

        mostrar_menu_ordenamiento()

        # Validacion de la opcion 
        try:
            opcion = input("Seleccione una opcion: ").strip()

            if opcion not in ["0", "1", "2", "3"]:
                raise ValueError

            if opcion == "0":
                print("Volviendo al menu principal...")
                break

            # Asociamos la opcion con el criterio
            if opcion == "1":
                criterio = "nombre"
            elif opcion == "2":
                criterio = "poblacion"
            elif opcion == "3":
                criterio = "superficie"

            # Elegimos el tipo de orden
            orden = input("Orden: (A)scendente o (D)escendente? ").strip().upper()

            if orden not in ["A", "D"]:
                print("Error: ingrese A o D.")
                continue

            descendente = orden == "D"

            resultado = ordenar_paises(paises, criterio, descendente)

            # Mostramos el resultado
            print("\nResultado:\n")
            for pais in resultado:
                print(
                    f"{pais['nombre']} | "
                    f"Poblacion: {pais['poblacion']} | "
                    f"Superficie: {pais['superficie']} km² | "
                    f"Continente: {pais['continente']}"
                )

        except ValueError:
            print("Error: opcion invalida. Intente nuevamente.")

#--------------------------------------------
# Funcion para calcular y mostrar estadisticas
#--------------------------------------------
def mostrar_estadisticas(paises):

    # Verificamos que Existan paises cargados
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    # Inicializamos con el primer pais
    mayor_pob = paises[0]
    menor_pob = paises[0]

    # Buscamos el pais con mayor y menor poblacion
    for pais in paises:
        if pais["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = pais
        if pais["poblacion"] < menor_pob["poblacion"]:
            menor_pob = pais

    # Calculamos los promedios
    total_poblacion = 0
    total_superficie = 0

    for pais in paises:
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

    promedio_pob = total_poblacion / len(paises)
    promedio_sup = total_superficie / len(paises)

    # Contamos cuantos paises hay por continente
    por_continente = {}

    for pais in paises:
        continente = pais["continente"]
        if continente in por_continente:
            por_continente[continente] += 1
        else:
            por_continente[continente] = 1

    # Mostramos las estadisticas
    print("\n--- ESTADISTICAS ---\n")
    print(f"Pais con mayor poblacion: {mayor_pob['nombre']} ({mayor_pob['poblacion']} hab.)")
    print(f"Pais con menor poblacion: {menor_pob['nombre']} ({menor_pob['poblacion']} hab.)")
    print(f"Promedio de poblacion:    {promedio_pob:.0f} hab.")
    print(f"Promedio de superficie:   {promedio_sup:.0f} km²")
    print("\nPaises por continente:")

    for continente, cantidad in por_continente.items():
        print(f"  {continente}: {cantidad}")

# Cargamos los datos desde el archivo CSV
paises = cargar_paises("paises.csv")

# Bucle principal que controla la ejecucion del sistema
while True:
    mostrar_menu()

    opcion = input("Seleccione una opcion: ")

    # Validamos la opcion elegida
    if not validar_opcion(opcion):
        print("Error: Opcion invalida")
        continue

    # Segun la opcion elegida llamamos a la funcion correspondiente
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
        menu_ordenamiento(paises)

    elif opcion == "6":
        mostrar_estadisticas(paises)

    else:
        print("Opcion invalida.")



