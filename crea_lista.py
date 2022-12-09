#lee un archivo .csv y retorna una lista con cada una de las lineas del archivo como una sublista
def crea_lista(archivo):
    arch_datos = open(archivo, 'r', encoding = 'utf-8')
    datos = arch_datos.readlines()
    arch_datos.close()

    if datos[len(datos)-1][len(datos[len(datos)-1])-1:] != '\n': #Verifica si el ultimo indice(str) del ultimo indice(list) es '\n'.
        with open(archivo, 'a', encoding = 'utf-8') as arch:
            arch.write('\n') #Si el ultimo indice no es un salto de línea, por conveniencia, se le añade uno.

    for i in range(len(datos)):
        datos[i] = datos[i].replace("\n","")
        datos[i] = datos[i].replace('”', '')
        datos[i] = datos[i].replace('“', '')
        datos[i] = datos[i].replace('\ufeff', '')
        datos[i] = datos[i].replace(", ", ",")
        datos[i] = datos[i].split(",")
        if datos[i][len(datos[i])-1].isdigit():
            datos[i][3], datos[i][4] = int(datos[i][3]), int(datos[i][4])

    return datos