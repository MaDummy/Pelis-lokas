from crea_lista import crea_lista
from saltodelinea import anadir_saltolinea
from anadir_pelicula import *

def valida_genero(genero): #valida que existe el genero ingresado ya existe
    global lista_genero
    for generos in lista_genero:
        if genero.lower() == generos[0].lower() or genero.lower() == generos[1].lower():
            return True
    return False

def valida_ano(ano): 
    if int(ano) < 1895:
        return False
    return True

def valida_valoracion(valoracion):
    if (int(valoracion) < 1) or (int(valoracion) > 5):
        return False
    return True

def valida_repeticion(titulo, director):
    global peliculas

    for pelicula in peliculas:
        if titulo.lower() == pelicula[0].lower()  and director.lower() == pelicula[1].lower():
            return True

    return False

def anade_pelicula(titulo, director, genero, ano, valoracion):
    global peliculas

    if titulo == '' or director == '' or genero == '' or ano == '' or valoracion == '':
        print("Falta algun tipo de dato. Intente nuevamente.")
        return False

    if valida_repeticion(titulo, director):
        print("La película ya existe")
        return False

    if not valida_genero(genero):
        print("No se pudo agregar la pelicula, el genero no existe")
        return False

    if not valida_ano(ano):
        print("No se pudo agregar la película, el año no es valido")
        return False

    if not valida_valoracion(valoracion):
        print("No se pudo agregar la pelicula, la valoración no es valida")
        return False

    return True

titulo = entry_titulo.get()
director = entry_director.get()
genero = entry_genero.get()
ano = entry_ano.get()
valoracion = entry_valoracion.get()

generos_arch = "generos.csv"
anadir_saltolinea(generos_arch)

lista_genero = crea_lista(generos_arch)

peliculas_arch = "peliculas.csv"
anadir_saltolinea(peliculas_arch)

peliculas = crea_lista(peliculas_arch)

if anade_pelicula(titulo, director, genero, ano, valoracion):
    peliculas_arch = open('peliculas.csv', 'a', encoding = 'utf-8')

    pelicula = [titulo.title(), director.title(), genero.capitalize(), int(ano), int(valoracion)]
    peliculas.append(pelicula)

    pelicula = f'“{titulo.title()}”, “{director.title()}”, “{genero.capitalize()}”, {ano}, {valoracion}”\n'
    peliculas_arch.write(pelicula)

    peliculas_arch.close()

print()
print()
print(peliculas)