'''
Autor: Cristian David Florez
Fecha: 2021-07-20
Descripción: Creacion e importacion del mapa que sera recorrido por el ninja para el desarrollo del juego.

Puntos a tener en cuenta:
    
    El tamaño del mapa debe ser de 10x10 
    El mapa debe ser cargado desde un archivo .txt
    El mapa debe ser cargado en una interfaz grafica
    Los elementos del mapa seran representados por numero enteros
        donde 0 es un espacio vacio, 1 es una pared, 2 es el inicio, 3 es el final
        para las barreras podria utilizar una lista interna con valores que representen
        el lado que esta bloqueado.

'''

'''
import tkinter.filedialog

def seleccionar_archivo():
    ruta_archivo = tkinter.filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
        print("Contenido del archivo seleccionado:")
        print(contenido)

if __name__ == "__main__":
    seleccionar_archivo()
    
'''

def cargar_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print("El archivo no se pudo encontrar.")
        return None

# Ruta del archivo a cargar
ruta_archivo = f'./Mapa.txt'

# Cargar el archivo
contenido_archivo = cargar_archivo(ruta_archivo)

# Imprimir el contenido del archivo si se cargó correctamente
if contenido_archivo is not None:
    print("Contenido del archivo:")
    print(contenido_archivo)