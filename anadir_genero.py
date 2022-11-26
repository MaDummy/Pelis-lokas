from tkinter import *

def borrar_texto(ventana):
    ventana = str(ventana)
    canvas.delete(ventana)

def cancelar():
    '''FUNCION CANCELAR'''
    window.destroy() #Destruye el programa, lo cierra.

def subgenero():
    '''FUNCION QUE AÑADE SUBGENEROS'''

    with open('generos.csv', 'a', encoding = "utf-8") as arch_generos: #Abro el archivo de generos.csv para agregarle más géneros, con la extensión append del CRUD.
        genero_padre = entry0.get() #Asigno una variable que toma el valor del género padre escrito.
        genero_ingresado = entry1.get() #Asigno una variable que toma el valor del género ingresado escrito.

        gp_existe = False

        for genero in generos:
            if genero_padre in genero: #Revisa la primera vez que el genero padre aparezca dentro de los generos.
                gp_existe = True

            if gp_existe and genero_ingresado in genero: #Si el genero padre existe y el genero ingresado también, printea que ya existe.
                print("El genero ya existe.")
                break

            if generos.index(genero) == len(generos)-1 and gp_existe: #Una vez ya haya revisado toda la lista de generos, si el genero ingresado
                generos.append([genero_ingresado, genero_padre])     #sigue sin existir, entonces lo ingresa a la lista de generos y al archivo csv.
                arch_generos.write("\n" + genero_ingresado + ";" + genero_padre)
                print("Se ha ingresado con exito.")
                canvas.forget(text)
               
                break #Como a la lista de generos se le añade un indice más, revisará la lista en el nuevo índice. Para evitar esto, puse un break.

            if generos.index(genero) == len(generos)-1 and not gp_existe: #Si al revisar la lista de generos, el genero padre sigue sin existir,          
                text = canvas.create_text(                                       #entonces printea que no se ingresó el genero.
                140, 141.0,
                text = "El género padre no existe.",
                fill = "#ffffff",
                font = ("MontserratRoman-Regular", int(14.0)))

    arch_generos.close() #Cierro el archivo.

def btn_clicked():
    print("Button Clicked")

arch_generos = open('generos.csv', 'r') #Se abre el archivo de generos una sola vez, para leerlo y generar una lista "generos"
generos = arch_generos.readlines()      #con la que se trabajará durante lo que dura esta ventana.
for genero in range(len(generos)):
    generos[genero] = generos[genero].strip().strip().strip("ï»¿").split(';') #El strip("ï»¿") es porque tira eso en el
                                                                              #primer indice de la lista "generos".
arch_generos.close()

#A partir de aqui se crean, de manera jerárquica, las ventanas a utilizar.

window = Tk() #Se crea la ventana.

window.geometry("1074x710") #Se establece el alto y ancho de la ventana.
window.configure(bg = "#222831") #El color del fondo

canvas = Canvas(  #El canvas será el fondo en el cual se insertarán imágenes luego.
    window,
    bg = "#222831",
    height = 710,
    width = 1074,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0) #Se le asigna la posicion inicial al canvas.

background_img = PhotoImage(file = "background.png") #Se define la imagen de fondo
background = canvas.create_image( #Finalmente, se le añade el fondo, que contiene las palabras del género padre y el género a ingresar.
    537.0, 345.0,
    image=background_img)

img_subgenero = PhotoImage(file = "img0.png") #Se define la imagen con el boton "Añadir sub-género"
ad_subgenero = Button( #Se crea el boton para añadir el sub-género. Imagen, evento a realizar (función), y el relieve plano del botón.
    image = img_subgenero,
    borderwidth = 0,
    highlightthickness = 0,
    command = subgenero,
    relief = "flat")

ad_subgenero.place( #Se usa el GM Place para ubicar el botón dentro de la ventana.
    x = 574, y = 515,
    width = 244,
    height = 86)

img1 = PhotoImage(file = "img1.png") #Se define la imagen del botón "Cancelar".

b1 = Button( #Se crea el botón para cancelar, con los mismos parámetros que el botón "Añadir sub-genero"
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = cancelar,
    relief = "flat")

b1.place( #Se ubica, con el GM Place, al botón "Cancelar".
    x = 256, y = 515,
    width = 244,
    height = 86)

entry0_img = PhotoImage(file = "img_textBox0.png") #Se define la imagen de la caja de texto respectiva al género padre.
entry0_bg = canvas.create_image(
    608.0, 193.5,
    image = entry0_img)

entry0 = Entry( #Se define la caja de texto del género padre.
    bd = 0,
    bg = "#3a4750",
    highlightthickness = 0)

entry0.place( #Se ubica la caja de texto del género padre.
    x = 192, y = 163,
    width = 832,
    height = 59)

entry1_img = PhotoImage(file = "img_textBox1.png") #Se define la imagen de la caja de texto respectiva al género a ingresar.
entry1_bg = canvas.create_image(
    608.0, 327.5,
    image = entry1_img)

entry1 = Entry( #Se define la caja de texto del género a ingresar.
    bd = 0,
    bg = "#3a4750",
    highlightthickness = 0)

entry1.place( #Se ubica la caja de texto.
    x = 192, y = 297,
    width = 832,
    height = 59)

window.resizable(False, False) #Se define que la ventana no sea reajustable en tamaño.
window.mainloop() #Para que el progrma siga ejecutándose hasta cerrarlo.
