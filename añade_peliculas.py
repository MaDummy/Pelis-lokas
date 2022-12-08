def valida_genero(genero): #valida que existe el genero ingresado ya existe
    global lista_genero
    for i in range(len(lista_genero)):
        if lista_genero[i][0] == genero:
            return True
    return False

def valida_generopadre(genero_padre): #valida que el genero padre exite
    global lista_genero
    if not genero_padre in lista_genero:
        return False
    return True

def valida_ano(ano): 
    if ano <=1895:
        return False
    return True

def valida_valoracion(valoracion):
    if (valoracion < 1) or (valoracion > 5):
        return False
    return True

def valida_repeticion(titulo, director):
    global peliculas
    for i in range (len(peliculas)):
        if (peliculas[i][0] == titulo) and (peliculas[i][1] == director):
            return False
    return True

def add_film(titulo, director, genero, ano, valoracion):
    global peliculas
    repeticion = valida_repeticion(titulo, director)
    if repeticion == False:
        return  print("La película ya existe")
    generoexiste = valida_genero(genero) and valida_generopadre(genero)
    if generoexiste == False:
        return print("No se pudo agregar la pelicula, el genero no existe")
    anovalido = valida_ano(ano)
    if anovalido == False:
        return print("No se pudo agregar la película, el año no es valido")
    valoracionvalida= valida_valoracion(valoracion)
    if valoracionvalida == False:
        return print("No se pudo agregar la pelicula, la valoración no es valida")
    if (repeticion and generoexiste and anovalido and valoracionvalida ==True):
        pelicula = [titulo, director, genero, ano, valoracion]
    peliculas.append(pelicula)
    print("La película se ha agregado exitosamente") 

valoracion = entry_valoracion.get()
titulo = entry_titulo.get()
director = entry_director.get()
genero = entry_genero.get()
ano = entry_ano.get() 
valoracion = entry_valoracion.get()
