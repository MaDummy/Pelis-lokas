def anadir_saltolinea(archivo: str):

    arch = open(archivo, 'r', encoding = 'utf-8')
    datos = arch.readlines()
    arch.close()

    print(datos[len(datos)-1][len(datos[len(datos)-1])-1:])

    if datos[len(datos)-1][len(datos[len(datos)-1])-1:] != '\n': #Verifica si el ultimo indice(str) del ultimo indice(list) es '\n'.
        print("No hay salto de linea")
        with open(archivo, 'a', encoding = 'utf-8') as arch:
            arch.write('\n')
            print("Ahora hay un salto de linea")
