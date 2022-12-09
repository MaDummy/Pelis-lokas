from tkinter import *
import tkinter.font as font
from crea_lista import crea_lista

def anadir_genero(gen_window,enter,leave):
    #archivo generos
    archivo_generos = open("generos.csv","r+",encoding="utf-8")
    lista_generos = crea_lista(archivo_generos) #Se crea una lista con los generos

    def subgenero():
        '''FUNCION QUE AÑADE SUBGENEROS'''
        nonlocal archivo_generos
        genero_padre = entry_padre.get() #Se asigna una variable que toma el valor del género padre escrito.
        genero_ingresado = entry_genero.get() #Se asigna una variable que toma el valor del género ingresado escrito.

        gp_existe = False

        for genero in lista_generos:
            if genero_padre.lower() == genero[0].lower() or genero_padre.lower() == genero[1].lower(): #Revisa la primera vez que el genero padre aparezca dentro de los generos.
                gp_existe = True

            if gp_existe and genero_ingresado.lower() == genero[0].lower() or genero_ingresado.lower() ==  genero[1].lower(): #Si el genero padre existe y el genero ingresado también, printea que ya existe.
                msg["text"] = "El género ya existe."
                msg.place(relx=0.415)
                break

            if lista_generos.index(genero) == len(lista_generos)-1 and gp_existe: #Una vez ya haya revisado toda la lista de generos, si el genero ingresado
                lista_generos.append([genero_ingresado, genero_padre])      #sigue sin existir, entonces lo ingresa a la lista de generos y al archivo csv.
                archivo_generos.write(f'“{genero_ingresado.capitalize()}”, “{genero_padre.capitalize()}”\n')
                
                msg["text"] = "Se ha ingresado con exito"
                msg.place_forget()
                msg.place(relx=0.385)
                break #Como a la lista de generos se le añade un indice más, revisará la lista en el nuevo índice. Para evitar esto, puse un break.

            if lista_generos.index(genero) == len(lista_generos)-1 and not gp_existe: #Si al revisar la lista de generos, el genero padre sigue sin existir,          
                msg["text"] = "El género padre no existe."
                msg.place_forget()
                msg.place(relx=0.385)


    #Interfaz Grafica

    #configuracion ventana
    '''PARA CENTRAR LA VENTANA'''
    largo = gen_window.winfo_screenwidth()
    altura = gen_window.winfo_screenheight()

    borde_x = int((largo/2) - (1074/2))
    borde_y = int((altura/2) - (550/2))

    gen_window.geometry("{}x{}+{}+{}".format(
        1074, 
        550, 
        borde_x, 
        borde_y))
    '''PARA CENTRAR LA VENTANA'''

    gen_window.configure(bg ="#222831") #El color del fondo
    gen_window.columnconfigure(index=0, weight=1) #para que el frame principal se expanda horizontalmente
    gen_window.rowconfigure(index=0, weight=1) #para que el frame principal se expanda verticalmente

    main_frame = Frame(gen_window,bg="#222831") #se define el frame donde ira el contenido
    main_frame.grid(row=0,column=0,sticky="nswe",padx=70,pady=(40,0))
    main_frame.columnconfigure(index=1,weight=1) #para que se expanda el contenido del frame

    #mensaje
    msg = Label(main_frame,text="",bg="#222831",fg="white") #Mensaje de error
    msg["font"] = ("Calibri", 20)

    #texto
    genero_padre_txt = Label(main_frame, text="Genero Padre", bg="#222831", fg="white")
    genero_padre_txt["font"] = ("Calibri",20)

    genero_txt = Label(main_frame, text="Genero", bg="#222831", fg="white")
    genero_txt["font"] = ("Calibri",20)


    #entradas - frames
    entry_frame_padre = Frame(main_frame, bd=13, bg="#3A4750") #para agregarle padding a entry_padre
    entry_frame_padre.columnconfigure(index=0, weight=1)    

    entry_frame_genero = Frame(main_frame,bd=13,bg="#3A4750") #para agregarle padding a entry_genero
    entry_frame_genero.columnconfigure(index=0, weight=1)    

    #entradas - entrys
    entry_padre = Entry(entry_frame_padre, bd=0, bg="#3A4750", fg="white")
    entry_padre["font"] = ("Calibri",14)

    entry_genero = Entry(entry_frame_genero, bd=0, bg="#3A4750", fg="white")
    entry_genero["font"] = ("Calibri",14)

    #entradas - posicionamiento
    entry_frame_padre.grid(row=0, column=1, pady=(110,0),sticky="we")
    entry_frame_genero.grid(row=1, column=1, sticky="we")

    genero_padre_txt.grid(row=0, column=0, sticky="w",pady=(110,0),padx=(0,20))
    entry_padre.grid(row=0, column=0, sticky="nswe")

    genero_txt.grid(row=1, column=0, sticky="w",pady=50)
    entry_genero.grid(row=0, column=0, sticky="nswe")


    #botones - fuente
    button_font = font.Font(size=13,family="Arial",weight="bold")

    #botones - frame
    buttons_frame = Frame(main_frame,bg="#222831") #frame donde iran los botones

    #botones - cancelar
    btn_cancelar_frame = Frame(buttons_frame, bg="white", bd=1) #frame donde va el boton cancelar
    btn_cancelar = Button(btn_cancelar_frame, bg="#262C35", text="Cancelar", fg="white", padx=90, bd=0, pady=15, command=gen_window.destroy,activebackground="#262C35",activeforeground="white",cursor="hand2")
    btn_cancelar["font"] = button_font

    #botones - añadir
    btn_anadir = Button(buttons_frame, bg="#D72323", text="Añadir Subgenero", fg="white", padx=70, bd=0, pady=15, command=subgenero,activebackground="#7c242c",activeforeground="white",cursor="hand2")
    btn_anadir["font"] = button_font

    #botones - posicionamiento 
    buttons_frame.grid(row=2, column=1, pady=30, sticky="we",padx=(30,0))

    btn_cancelar_frame.grid(row=0, column=0,padx=(0,60))
    btn_cancelar.grid(row=0, column=0)
    
    btn_anadir.grid(row=0,column=1,padx=(0,0),sticky="w")


    #eventos
    btn_anadir.bind("<Enter>",enter)
    btn_anadir.bind("<Leave>",leave)