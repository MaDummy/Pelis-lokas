from tkinter import *
import tkinter.font as font
from crea_lista import crea_lista

def anadir_pelicula(pel_window,enter,leave):
    def valida_genero(genero: str) -> bool: #Valida que existe el genero ingresado ya existe
        for generos in lista_generos:
            if genero.lower() == generos[0].lower() or genero.lower() == generos[1].lower():
                return True
        return False

    
    def valida_ano(ano: str) -> bool: 
        if not ano.isdigit(): #Se revisa que el año sea un número
            return False
        if int(ano) < 1895: #Se revisa que sea mayor o igual a 1895.
            return False
        return True


    def valida_valoracion(valoracion: str) -> bool:
        if not valoracion.isdigit(): #Se revisa que la validación sea un número.
            return False
        if (int(valoracion) < 1) or (int(valoracion) > 5): #Se revisa que la valoración esté entre 1 y 5.
            return False
        return True


    def valida_repeticion(titulo: str, director: str) -> bool:
        for pelicula in lista_peliculas: #Se valida si el titulo y el director están juntos en el archivo de películas.
            if titulo.lower() == pelicula[0].lower()  and director.lower() == pelicula[1].lower():
                return True
        return False


    def valida_pelicula(titulo: str, director: str, genero: str, ano: str, valoracion: str) -> bool:
        if titulo == '' or director == '' or genero == '' or ano == '' or valoracion == '':
            print("Falta algun tipo de dato. Intente nuevamente.")
            return False
        
        if not valida_ano(ano):
            print("No se pudo agregar la película, el año no es valido")
            return False

        if not valida_valoracion(valoracion):
            print("No se pudo agregar la pelicula, la valoración no es valida")
            return False
        
        if not valida_genero(genero):
            print("No se pudo agregar la pelicula, el genero no existe")
            return False
        
        if valida_repeticion(titulo, director):
            print("La película ya existe")
            return False

        return True


    def anade_pelicula():
        '''VARIABLES GLOBALES'''

        global lista_peliculas
        global lista_generos

        '''SE RECOGEN LOS TEXTOS INGRESADOS'''

        titulo = entry_titulo.get()
        director = entry_director.get()
        genero = entry_genero.get()
        ano = entry_ano.get()
        valoracion = entry_valoracion.get()

        '''SE CREAN LAS LISTAS CORRESPONDIENTES A LOS GÉNEROS Y PELÍCULAS'''

        archivo_generos = open("generos.csv","r+",encoding="utf-8")
        lista_generos = crea_lista(archivo_generos)

        archivo_peliculas = open("peliculas.csv","r+",encoding="utf-8")
        lista_peliculas = crea_lista(archivo_peliculas)

        '''VALIDACIÓN PRINCIPAL'''

        if valida_pelicula(titulo, director, genero, ano, valoracion): #Si la película es válida, se añade a la lista y a la base de datos de películas.
            pelicula = [titulo.title(), director.title(), genero.capitalize(), int(ano), int(valoracion)]
            lista_peliculas.append(pelicula)

            archivo_peliculas.write(f'“{titulo.title()}”, “{director.title()}”, “{genero.capitalize()}”, {ano}, {valoracion}”\n')
  
    '''------------------------------------------------INTERFAZ GRÁFICA------------------------------------------------'''

    '''PARA CENTRAR LA VENTANA'''
    largo = pel_window.winfo_screenwidth()
    altura = pel_window.winfo_screenheight()

    borde_x = int((largo/2) - (1074/2))
    borde_y = int((altura/2) - (800/2))

    pel_window.geometry("{}x{}+{}+{}".format(
        1074, 
        800, 
        borde_x, 
        borde_y))
    '''PARA CENTRAR LA VENTANA'''

    pel_window.configure(bg ="#222831") #El color del fondo
    pel_window.columnconfigure(index=0, weight=1) #para que el frame principal se expanda horizontalmente
    pel_window.rowconfigure(index=0, weight=1) #para que el frame principal se expanda verticalmente

    main_frame = Frame(pel_window,bg="#222831") #se define el frame donde ira el contenido
    main_frame.grid(row=0,column=0,sticky="nswe",padx=70,pady=50)
    main_frame.columnconfigure(index=1,weight=1) #para que se expanda el contenido del frame

    '''TEXTOS'''

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

    '''SE DEFINEN LAS CAJAS DE TEXTO'''

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

    '''SE DEFINEN LAS ENTRADAS DE TEXTO'''

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

    '''SE POSICIONAN LAS CAJAS DE TEXTO Y SUS ENTRADAS CORRESPONDIENTES'''

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

    '''BOTONES'''

    button_font = font.Font(size=13,family="Arial",weight="bold")

    buttons_frame = Frame(main_frame,bg="#222831") #Frame donde iran los botones
    buttons_frame.grid(row=5, column=1, pady=50, sticky="we",padx=(45,0))

    #BOTON CANCELAR
    btn_cancelar_frame = Frame(buttons_frame, bg="white", bd=1) #Frame donde va el boton cancelar
    btn_cancelar = Button(btn_cancelar_frame, bg="#262C35", text="Cancelar", fg="white", padx=90, bd=0, pady=15,activebackground="#262C35",activeforeground="white",cursor="hand2",command=pel_window.destroy)
    btn_cancelar["font"] = button_font

    btn_cancelar_frame.grid(row=0, column=0,padx=(0,60))
    btn_cancelar.grid(row=0, column=0)

    #BOTON AÑADIR PELICULAS
    btn_anadir = Button(buttons_frame, bg="#D72323", text="Añadir Pelicula", fg="white", padx=75, bd=0, pady=15,activebackground="#7c242c",activeforeground="white",cursor="hand2",command=anade_pelicula)
    btn_anadir["font"] = button_font

    btn_anadir.grid(row=0,column=1,padx=(0,0),sticky="w")

    #EVENTOS
    btn_anadir.bind("<Enter>",enter)
    btn_anadir.bind("<Leave>",leave)