#lee un archivo .csv y retorna una lista con cada una de las lineas del archivo como una sublista
def crea_lista(archivo: str) -> list:

    arch_datos = open(archivo, 'r', encoding = 'utf-8')
    datos = arch_datos.readlines()
    arch_datos.close()

    if datos[len(datos)-1][len(datos[len(datos)-1])-1:] != '\n': #Verifica si el ultimo indice(str) del ultimo indice(list) es '\n'.
        with open(archivo, 'a', encoding = 'utf-8') as arch:
            arch.write('\n') #Si el ultimo indice no es un salto de línea, por conveniencia, se le añade uno.

    for i in range(len(datos)): #Se hacen los reemplazos correspondientes.
        datos[i] = datos[i].replace("\n","")
        datos[i] = datos[i].replace('”', '')
        datos[i] = datos[i].replace('“', '')
        datos[i] = datos[i].replace('\ufeff', '') #Caso excepcional.
        datos[i] = datos[i].replace(", ", ",")
        datos[i] = datos[i].split(",")
        if datos[i][len(datos[i])-1].isdigit(): #En el caso de las películas, se reemplazan los tipo de variables de str a int de los últimos dos índices.
            datos[i][3], datos[i][4] = int(datos[i][3]), int(datos[i][4])

    return datos