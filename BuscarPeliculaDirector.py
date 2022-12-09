from tkinter import *
from crea_lista import crea_lista

archivo_peliculas = 'peliculas.csv'
peliculas = crea_lista(archivo_peliculas)

#############BuscarPelicula######################

Lista_Final = []
Peli_Abuscar = input("Ingrese pelicula: ")

for pelicula in peliculas:
    for indice in range(2):
        if Peli_Abuscar in pelicula[indice].lower():
            Lista_Final.append(pelicula)
            break

print(Lista_Final)