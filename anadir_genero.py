from tkinter import *
import tkinter.font as font

#archivo generos
arch_generos = open('generos.csv', 'r',encoding="utf-8") #Se abre el archivo de generos una sola vez, para leerlo y generar una lista "generos"
generos = arch_generos.readlines()    
for genero in range(len(generos)):
    print(generos[genero])                                                                       

print(generos)
arch_generos.close()




def cancelar():
    '''FUNCION CANCELAR'''
    window.destroy() #Destruye el programa, lo cierra.

def subgenero():
    '''FUNCION QUE AÑADE SUBGENEROS'''

    with open('generos.csv', 'a', encoding = "utf-8") as arch_generos: #Abro el archivo de generos.csv para agregarle más géneros, con la extensión append del CRUD.
        genero_padre = entry_padre.get() #Asigno una variable que toma el valor del género padre escrito.
        genero_ingresado = entry_genero.get() #Asigno una variable que toma el valor del género ingresado escrito.

        gp_existe = False

        for genero in generos:
            if genero_padre in genero: #Revisa la primera vez que el genero padre aparezca dentro de los generos.
                gp_existe = True

            if gp_existe and genero_ingresado in genero: #Si el genero padre existe y el genero ingresado también, printea que ya existe.
                rect = Frame(main_frame,width=700,height=100,bg="#222831") #rectangulo para ocultar el mensaje anterior
                rect.place(relx=0.2)
                msg = Label(main_frame, text="El género ya existe.", bg="#222831",fg="white") #mensaje
                msg["font"] = ("Calibri", 20)
                msg.place(relx=0.43)
                print("El genero ya existe.")
                break

            if generos.index(genero) == len(generos)-1 and gp_existe: #Una vez ya haya revisado toda la lista de generos, si el genero ingresado
                generos.append([genero_ingresado, genero_padre])     #sigue sin existir, entonces lo ingresa a la lista de generos y al archivo csv.
                arch_generos.write("\n" + genero_ingresado + ";" + genero_padre)
                
                rect = Frame(main_frame,width=700,height=100,bg="#222831") #rectangulo para ocultar el mensaje anterior
                rect.place(relx=0.2)
                msg = Label(main_frame, text="Se ha ingresado con exito", bg="#222831",fg="white") #mensaje
                msg["font"] = ("Calibri", 20)
                msg.place(relx=0.385)
                print("Se ha ingresado con exito.")
                #canvas.forget(text)
               
                break #Como a la lista de generos se le añade un indice más, revisará la lista en el nuevo índice. Para evitar esto, puse un break.

            if generos.index(genero) == len(generos)-1 and not gp_existe: #Si al revisar la lista de generos, el genero padre sigue sin existir,          
                rect = Frame(main_frame,width=700,height=100,bg="#222831") #rectangulo para ocultar el mensaje anterior
                rect.place(relx=0.2)
                msg = Label(main_frame, text="El género padre no existe.", bg="#222831",fg="white") #mensaje
                msg["font"] = ("Calibri", 20)
                msg.place(relx=0.385)

    arch_generos.close() #Cierro el archivo.




#Interfaz Grafica
window = Tk() #Se crea la ventana.

window.geometry("1074x710") #Se establece el alto y ancho de la ventana.
window.configure(bg ="#222831") #El color del fondo
window.columnconfigure(index=0, weight=1) #para que el frame principal se expanda horizontalmente
window.rowconfigure(index=0, weight=1) #para que el frame principal se expanda verticalmente

main_frame = Frame(window,bg="#222831") #se define el frame donde ira el contenido
main_frame.grid(row=0,column=0,sticky="nswe",padx=70,pady=50)
main_frame.columnconfigure(index=1,weight=1) #para que se expanda el contenido del fram

#texto
genero_padre_txt = Label(main_frame, text="Genero Padre", bg="#222831", fg="white")
genero_padre_txt["font"] = ("Calibri",20)

genero_txt = Label(main_frame, text="Genero", bg="#222831", fg="white")
genero_txt["font"] = ("Calibri",20)


#se definen las cajas de ingreso de texto
entry_frame_padre = Frame(main_frame, bd=13, bg="#3A4750") #para agregarle padding a entry_padre
entry_frame_padre.columnconfigure(index=0, weight=1)    
entry_frame_padre.grid(row=0, column=1, pady=(160,0),sticky="we")

entry_frame_genero = Frame(main_frame,bd=13,bg="#3A4750") #para agregarle padding a entry_genero
entry_frame_genero.columnconfigure(index=0, weight=1)    
entry_frame_genero.grid(row=1, column=1, sticky="we")

#entradas
entry_padre = Entry(entry_frame_padre, bd=0, bg="#3A4750", fg="white")
entry_padre["font"] = ("Calibri",14)

entry_genero = Entry(entry_frame_genero, bd=0, bg="#3A4750", fg="white")
entry_genero["font"] = ("Calibri",14)

#se posiciona el texto y las entradas
genero_padre_txt.grid(row=0, column=0, sticky="w",pady=(160,0),padx=(0,20))
entry_padre.grid(row=0, column=0, sticky="nswe")

genero_txt.grid(row=1, column=0, sticky="w",pady=50)
entry_genero.grid(row=0, column=0, sticky="nswe")


#botones
buttons_frame = Frame(main_frame,bg="#222831") #frame donde iran los botones
buttons_frame.grid(row=2, column=1, pady=30, sticky="we",padx=(30,0))

#Se crea el botón para cancelar
btn_cancelar_frame = Frame(buttons_frame, bg="white", bd=1) #frame donde va el boton cancelar
btn_cancelar = Button(btn_cancelar_frame, bg="#262C35", text="Cancelar", fg="white", padx=90, bd=0, pady=15, command=cancelar)
btn_cancelar["font"] = ("Calibri",13)

btn_cancelar_frame.grid(row=0, column=0,padx=(0,60))
btn_cancelar.grid(row=0, column=0)

#Se crea el botón para añadir subgeneros
btn_añadir = Button(buttons_frame, bg="#D72323", text="Añadir Subgenero", fg="white", padx=70, bd=0, pady=15, command=subgenero)
btn_añadir["font"] = ("Calibri",13)

btn_añadir.grid(row=0,column=1,padx=(0,0),sticky="w")


window.mainloop() #Para que el programa siga ejecutándose hasta cerrarlo.
