# TP-INTEGRADOR-PROGRAMACION
Trabajo Practico Integrador de Programacion 1

## Integrantes

- Gustavo Rivero
- Rodrigo Zampa

## Estado 

Proyecto en desarrollo.

## Objetivo

Desarrollar una aplicacion de consola que permita gestionar informacion de paises utilizando: 
Python
Archivos CSV
Listas y diccionarios

## Funcionalidades

El sistema permite:
- Cargar paises desde un archivo CSV
- Agregar nuevos paises
- Buscar paises por nombre
- Actualizar poblacion y superficie
- Filtrar paises:
	* Por nombre
	* Por poblacion
	* Por superficie
	* En orden ascendente o descendente
- Mostrar estadisticas:
	* Pais con mayor y menor poblacion
	* Promedios de poblacion y superficie
	* Cantidad de paises por continente

## Estructura del proyecto
📁 TP-INTEGRADOR-PROGRAMACION/

- ── paises.csv        # Datos iniciales
- ── main.py           # Programa principal
- ── README.md         # Documentación

## Formato del archivo CSV
El archivo paises.csv debe respetar el siguiente formato:
- nombre;poblacion;superficie;continente
- Argentina;46000000;2780000;America
- Brasil;214000000;8516000;America
- España;47000000;505000;Europa

## Ejecución

Tener Python 3 instalado
Colocar el archivo paises.csv en la misma carpeta
Ejecutar el programa:
	main.py con Visual Studio Code

## Uso
El sistema funciona mediante un menú interactivo:
--- GESTION DE PAISES ---
1. Agregar pais
2. Actualizar pais
3. Buscar pais
4. Filtrar paises
5. Ordenar paises
6. Estadisticas
0. Salir

Seleccionar una opción e ingresar los datos solicitados.
