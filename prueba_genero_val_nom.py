from crea_lista import crea_lista

arch = open('peliculas.csv', 'r', encoding='utf-8')
peliculas = crea_lista(arch)

print(peliculas)