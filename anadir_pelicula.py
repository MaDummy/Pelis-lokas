from tkinter import *
import tkinter.font as font


def anadir_pelicula():
    #Interfaz Grafica
    window = Tk() #Se crea la ventana.

    window.geometry("1074x710") #Se establece el alto y ancho de la ventana.
    window.configure(bg ="#222831") #El color del fondo
    window.columnconfigure(index=0, weight=1) #para que el frame principal se expanda horizontalmente
    window.rowconfigure(index=0, weight=1) #para que el frame principal se expanda verticalmente

    main_frame = Frame(window,bg="#222831") #se define el frame donde ira el contenido
    main_frame.grid(row=0,column=0,sticky="nswe",padx=70,pady=50)
    main_frame.columnconfigure(index=1,weight=1) #para que se expanda el contenido del frame

    #texto
    titulo_txt = Label(main_frame, text="Titulo", bg="#222831", fg="white")
    titulo_txt["font"] = ("Calibri",20)

    director_txt = Label(main_frame, text="Director", bg="#222831", fg="white")
    director_txt["font"] = ("Calibri",20)

    ano_txt = Label(main_frame, text="Año", bg="#222831", fg="white")
    ano_txt["font"] = ("Calibri",20)

    genero_txt = Label(main_frame, text="Genero", bg="#222831", fg="white")
    genero_txt["font"] = ("Calibri",20)

    valoracion_txt = Label(main_frame, text="Valoracion", bg="#222831", fg="white")
    valoracion_txt["font"] = ("Calibri",20)

    #se definen las cajas de ingreso de texto
    entry_frame_titulo = Frame(main_frame, bd=13, bg="#3A4750") #para agregarle padding a entry_padre
    entry_frame_titulo.columnconfigure(index=0, weight=1)    
    entry_frame_titulo.grid(row=0, column=1, pady=(50,0),sticky="we")

    entry_frame_director = Frame(main_frame,bd=13,bg="#3A4750") #para agregarle padding a entry_director
    entry_frame_director.columnconfigure(index=0, weight=1)    
    entry_frame_director.grid(row=1, column=1, sticky="we",pady=(40,0))

    entry_frame_ano = Frame(main_frame, bd=13, bg="#3A4750") #para agregarle padding a entry_ano
    entry_frame_ano.columnconfigure(index=0, weight=1)    
    entry_frame_ano.grid(row=2, column=1, pady=(40,0),sticky="we")

    entry_frame_genero = Frame(main_frame, bd=13, bg="#3A4750") #para agregarle padding a entry_genero
    entry_frame_genero.columnconfigure(index=0, weight=1)    
    entry_frame_genero.grid(row=3, column=1, pady=(40,0),sticky="we")

    entry_frame_valoracion = Frame(main_frame, bd=13, bg="#3A4750") #para agregarle padding a entry_valoracion
    entry_frame_valoracion.columnconfigure(index=0, weight=1)    
    entry_frame_valoracion.grid(row=4, column=1, pady=(40,0),sticky="we")

    #entradas
    entry_titulo = Entry(entry_frame_titulo, bd=0, bg="#3A4750", fg="white")
    entry_titulo["font"] = ("Calibri",14)

    entry_director = Entry(entry_frame_director, bd=0, bg="#3A4750", fg="white")
    entry_director["font"] = ("Calibri",14)

    entry_ano = Entry(entry_frame_ano, bd=0, bg="#3A4750", fg="white")
    entry_ano["font"] = ("Calibri",14)

    entry_genero = Entry(entry_frame_genero, bd=0, bg="#3A4750", fg="white")
    entry_genero["font"] = ("Calibri",14)

    entry_valoracion = Entry(entry_frame_valoracion, bd=0, bg="#3A4750", fg="white")
    entry_valoracion["font"] = ("Calibri",14)

    #se posiciona el texto y las entradas
    titulo_txt.grid(row=0, column=0, sticky="w",pady=(50,0))
    entry_titulo.grid(row=0, column=0, sticky="nswe")

    director_txt.grid(row=1, column=0, sticky="w",pady=(40,0))
    entry_director.grid(row=0, column=0, sticky="nswe")

    ano_txt.grid(row=2, column=0, sticky="w",pady=(40,0))
    entry_ano.grid(row=0, column=0, sticky="nswe")

    genero_txt.grid(row=3, column=0, sticky="w",pady=(40,0))
    entry_genero.grid(row=0, column=0, sticky="nswe")

    valoracion_txt.grid(row=4, column=0, sticky="w",pady=(40,0),padx=(0,25))
    entry_valoracion.grid(row=0, column=0, sticky="nswe")

    #botones
    button_font = font.Font(size=13,family="Arial",weight="bold")

    buttons_frame = Frame(main_frame,bg="#222831") #frame donde iran los botones
    buttons_frame.grid(row=5, column=1, pady=50, sticky="we",padx=(45,0))

    #Se crea el botón para cancelar
    btn_cancelar_frame = Frame(buttons_frame, bg="white", bd=1) #frame donde va el boton cancelar
    btn_cancelar = Button(btn_cancelar_frame, bg="#262C35", text="Cancelar", fg="white", padx=90, bd=0, pady=15,activebackground="#262C35",activeforeground="white",cursor="hand2")
    btn_cancelar["font"] = button_font

    btn_cancelar_frame.grid(row=0, column=0,padx=(0,60))
    btn_cancelar.grid(row=0, column=0)

    #Se crea el botón para añadir peliculas
    btn_añadir = Button(buttons_frame, bg="#D72323", text="Añadir Pelicula", fg="white", padx=75, bd=0, pady=15,activebackground="#7c242c",activeforeground="white",cursor="hand2")
    btn_añadir["font"] = button_font

    btn_añadir.grid(row=0,column=1,padx=(0,0),sticky="w")
    window.mainloop() #Para que el programa siga ejecutándose hasta cerrarlo.
