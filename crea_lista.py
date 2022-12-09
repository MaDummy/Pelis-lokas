#lee un archivo .csv y retorna una lista con cada una de las lineas del archivo como una sublista
def crea_lista(archivo) -> list:
    datos = archivo.readlines()
    
    if datos[len(datos)-1][len(datos[len(datos)-1])-1:] != '\n': #Verifica si el ultimo indice(str) del ultimo indice(list) es '\n'.
        archivo.write('\n') #Si el ultimo indice no es un salto de línea, por conveniencia, se le añade uno.
    
    for i in range(len(datos)):
        datos[i] = datos[i].replace("\n","")
        datos[i] = datos[i].replace('"', '')
        datos[i] = datos[i].replace('“',"")
        datos[i] = datos[i].replace('”',"")
        datos[i] = datos[i].replace('\ufeff', '')
        datos[i] = datos[i].replace(", ", ",")
        datos[i] = datos[i].split(",")
    return datos