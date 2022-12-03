#lee un archivo .csv y retorna una lista con cada una de las lineas del archivo como una sublista
def crea_lista(archivo):
    datos = archivo.readlines()
    for i in range(len(datos)):
        datos[i] = datos[i].replace("\n","")
        datos[i] = datos[i].replace('"', '')
        datos[i] = datos[i].replace('\ufeff', '')
        datos[i] = datos[i].replace(", ", ",")
        datos[i] = datos[i].split(",")
    return datos