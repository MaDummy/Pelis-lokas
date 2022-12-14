from tkinter import *
from tkinter import ttk
import tkinter.font as font
from crea_lista import crea_lista
from anadir_genero import anadir_genero
from anadir_pelicula import anadir_pelicula

'''ROOT'''
root = Tk()
root.title("Películas")

'''PARA CENTRAR LA VENTANA'''
largo = root.winfo_screenwidth()
altura = root.winfo_screenheight()

borde_x = int((largo/2) - (1074/2))
borde_y = int((altura/2) - (700/2))

root.geometry("{}x{}+{}+{}".format(
    1074, 
    700, 
    borde_x, 
    borde_y))
'''PARA CENTRAR LA VENTANA'''

root.update()
root.configure(bg="#222831")


#archivos
try:
    archivo_generos = open("generos.csv","r+",encoding="utf-8") 
except FileNotFoundError:
    archivo_generos = open("generos.csv", "x",encoding="utf-8")
    archivo_generos.close()
    
    archivo_generos = open("generos.csv","r+",encoding="utf-8") 
    
try:
    archivo_peliculas = open("peliculas.csv","r+",encoding="utf-8") 
except FileNotFoundError:
    archivo_peliculas = open("peliculas.csv", "x",encoding="utf-8")
    archivo_peliculas.close()

    archivo_peliculas = open("peliculas.csv","r+",encoding="utf-8")


generos = crea_lista(archivo_generos)
peliculas = crea_lista(archivo_peliculas)

#colores
BG_COLOR = "#222831"
LIGHT_COLOR = "#3A4750"
BTN_COLOR = "#D72323"
BTN_HOVER_COLOR = "#e63434"
BTN_ACTIVE_COLOR = "#7c242c"
TXT_COLOR = "#F1F6F9"
LIGHT_TXT_COLOR = "#A9A9A9"
COMBO_COLOR = "#303841"

#imagenes
arrow_icon = PhotoImage(file="img/arrow.png")
filtros_icon = PhotoImage(file="img/filter.png")
search_icon = PhotoImage(file="img/search.png")
home_icon = PhotoImage(file="img/home.png")
movie_icon = PhotoImage(file="img/movie.png")
genre_icon = PhotoImage(file="img/genre.png")

#estados
filtros_estado = 0

#styles
style = ttk.Style(root)
style.theme_use("default")

#styles - combobox
root.option_add('*TCombobox*Listbox*Background', COMBO_COLOR)
root.option_add('*TCombobox*Listbox*Foreground', "white")
root.option_add('*TCombobox*Listbox*selectBackground', BTN_COLOR)
root.option_add('*TCombobox*Listbox*selectForeground', "white")
root.option_add('*TCombobox*Listbox*font', ("Calibri",14))
root.option_add('*TCombobox*Listbox*bd', "0")

style.map('TCombobox', fieldbackground=[('readonly', COMBO_COLOR)])
style.map('TCombobox', selectbackground=[('readonly', "none")])
style.map('TCombobox', selectforeground=[('readonly', "white")])
style.map('TCombobox', background=[('readonly', COMBO_COLOR)])
style.map('TCombobox', foreground=[('readonly', "white")])

style.element_create('Mystyle.TCombobox.downarrow', 'image', arrow_icon)

style.layout(
    'Mystyle.TCombobox', [(
        'Combobox.field', {
            'sticky': NSEW,
            'children': [(
                'Mystyle.TCombobox.downarrow', {
                    'side': 'right',
                    'sticky': S
                }
            ) 
                
            ]
        }
    )]
)

style.configure("Mystyle.TCombobox",relief= "flat", borderwidth=0,highlightthickness=0)

#Styles - Vista de árbol
style.layout('nodotbox.Treeview.Item', 
             [('Treeitem.padding',
               {'children': [('Treeitem.indicator', {'side': 'left', 'sticky': ''}),
                 ('Treeitem.image', {'side': 'left', 'sticky': ''}),
                 ('Treeitem.text', {'side': 'left', 'sticky': ''})],
                'sticky': 'nswe'})])

style.configure("Treeview",
    background= LIGHT_COLOR,
    foreground= "white",
    fieldbackground= LIGHT_COLOR,
    borderwidth = 0,
    rowheight = 35,
    font = ("Calibri",17)
    )

style.configure("Treeview.Heading", background=LIGHT_COLOR, borderwidth=0,foreground="white",font=("Calibri",13))

style.map("Treeview.Heading", background=[("hover", "none")])
style.map("Treeview", background=[("selected", BTN_COLOR)])
style.map("Treeview",relief=[("selected","flat")])

#Styles - Scrollbar
style.configure("Vertical.TScrollbar",background=LIGHT_COLOR,arrowcolor="white")
style.map("Vertical.TScrollbar",background=[("hover",BG_COLOR)])

#Scrollbar
class AutoScrollbar(ttk.Scrollbar):
    def set(self, low, high):
        if float(low) <= 0.0 and float(high) >= 1.0:
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, low, high)

'''----------FUNCIÓN PRINCIPAL-----------'''

#funcion principal
def main(): 
    '''---------SUB-FUNCIONES PRINCIPALES---------'''
    #funciones encargadas de abrir y cerrar el menú de filtros
    def menu_filtros():
        global filtros_estado
        
        #si el menu está abierto, se cierra y cambia su estado a 0 (cerrado)
        if filtros_estado == 1:
            cierra_filtros()
            return
        abre_filtros()

    def abre_filtros():
        global filtros_estado
        #abre el menu
        filtros_frame.grid(row=1,column=0,sticky="nswe",columnspan=4,pady=(8,0),rowspan=2)
        #cambia su estado a 1 (abierto)
        filtros_estado = 1
    
    def cierra_filtros():
        global filtros_estado
        #cierra el menu
        filtros_frame.grid_remove()
        #cambia su estado a 0 (cerrado)
        filtros_estado = 0
    
    #Funciones encargadas de desplegar el arbol de generos y la tabla de peliculas
    def despliega_generos():
        #Modifica el estilo del arbol de generos
        style.configure("Treeview", 
            font=("Calibri",17),
            background=LIGHT_COLOR,
            rowheight=35,
            fieldbackground=LIGHT_COLOR,
            borderwidth=0,
            )
        
        style.configure("Treeview.Heading",
            borderwidth=0,
            font=("Calibri",13)
        )

        arbol_generos_btn.grid_remove()
        peliculas_titulo.grid_remove()
        peliculas_frame.grid_remove()

        lista_peliculas_btn.grid(row=3,column=3,sticky="e",pady=(0,30))
        generos_titulo.grid(row=3,column=0,sticky="w",pady=(0,30))
        generos_frame.grid(row=4,column=0,columnspan=4,sticky="nswe")
        
    #funcion que despliega las peliculas
    def despliega_peliculas():
        #Modifica el estilo de la tabla de peliculas
        style.configure("Treeview", 
            font=("Calibri",14),
            background="#283039",
            rowheight=40,
            fieldbackground="#283039",
            )
        
        style.configure("Treeview.Heading",borderwidth=0,font=("Calibri",16))

        generos_titulo.grid_remove()
        generos_frame.grid_remove()
        lista_peliculas_btn.grid_remove()

        arbol_generos_btn.grid(row=3,column=3,sticky="e",pady=(0,30))         
        peliculas_titulo.grid(row=3,column=0,sticky="w",pady=(0,30))
        peliculas_frame.grid(row=4,column=0,columnspan=4,sticky="nswe")
         
    #Funciones encargadas de llenar las distintas tablas del programa
    def llena_peliculas():
        for pelicula in peliculas:
            tabla_peliculas.insert("","end",values=(pelicula[0],pelicula[1],pelicula[2],str(pelicula[3]),str(pelicula[4]) + "/5"))
    
    def llena_arbol():
        arbol_generos.insert("", "end","general",text="General")
        for genero in generos:
            arbol_generos.insert(genero[1].lower(),"end",genero[0].lower(),text=genero[0])
    
    def llena_combo():
        combo_values = ["<Cualquiera>"]
        for genero1 in generos:
            if genero1[0] not in combo_values: #Añade el genero una sola vez al combo
                combo_values.append(genero1[0].capitalize())
        combo_genero["values"] = tuple(combo_values)
    
    
    #FUNCIÓN BÚSQUEDA DE PELÍCULAS
    def busqueda(event = None):
        global filtros_estado
        
        #Limpia resultados anteriores
        limpia_resultados()
        
        #Modifica el estilo de la tabla de resultados
        style.configure("Treeview", 
            font=("Calibri",14),
            background="#283039",
            rowheight=40,
            fieldbackground="#283039",
            )
        
        style.configure("Treeview.Heading",borderwidth=0,font=("Calibri",16))

        #Activa el boton home
        home_button["state"] = "active"
        home_button["cursor"] = "hand2"

        #Elimina boton para cambiar entre peliculas y generos
        lista_peliculas_btn.grid_remove()
        arbol_generos_btn.grid_remove()

        #Elimina el arbol de generos o tabla de peliculas
        peliculas_titulo.grid_remove()
        peliculas_frame.grid_remove()
        generos_titulo.grid_remove()
        generos_frame.grid_remove()
        
        #Resultados 
        lista_resultados = []
        valoracion = combo_valoracion.get()
        genero = combo_genero.get()
        nombre = search.get().strip()
        
        if nombre == "Buscar película":
            nombre = ''

        if genero == "<Cualquiera>" and valoracion != "<Cualquiera>": #Caso en el que se busque por valoración y nombre
            pelis_nom = []
            for pelicula in peliculas:
                if nombre.lower() in pelicula[0].lower() or nombre.lower() in pelicula[1].lower():
                    pelis_nom.append(pelicula)

            for pelicula in pelis_nom:
                if pelicula[4] == valoracion:
                    lista_resultados.append(pelicula)

        if genero == "<Cualquiera>" and valoracion == "<Cualquiera>": #Caso en el que se busque solo por el nombre
            for pelicula in peliculas:
                if nombre.lower() in pelicula[0].lower() or nombre.lower() in pelicula[1].lower():
                   lista_resultados.append(pelicula)
        
        if genero != "<Cualquiera>" and valoracion == "<Cualquiera>": #Caso en el que se busque por género y nombre
            pelis_nom = []
            for pelicula in peliculas:
                if nombre.lower() in pelicula[0].lower() or nombre.lower() in pelicula[1].lower():
                    pelis_nom.append(pelicula)

            for dupla_generos in generos: #Se recorren los géneros con la variable "género" equivalente a una lista que contiene al género y su género padre.
                if genero.lower() == dupla_generos[0].lower() or genero.lower() == dupla_generos[1].lower():
                    for subgenero in generos: #Se recorren los subgéneros correspondientes a ese género, por ejemplo "Romance" o "Acción".
                        if subgenero[1].lower() == genero.lower(): #Si "Romance" es el género padre de la lista "genero".
                            for pelicula in pelis_nom: #Se recorren las peliculas con la variable "pelicula", correspondiente a una lista con sus datos.
                                if pelicula[2].lower() == subgenero[0].lower(): #Si la pelicula, en su segundo índice (género), corresponde al subgénero del género buscado
                                    lista_resultados.append(pelicula) #Añade la película a la lista con los resultados.

                    for pelicula in pelis_nom: #Luego, recorre las peliculas asociadas al género especifico. Si fuera "Acción", buscaría la película asociada al género "Acción".
                        if pelicula[2].lower() == genero.lower(): #Si la película, en su segundo índice, corresponde al género a buscar
                            lista_resultados.append(pelicula) #Se añade la película
                    break

        if genero != "<Cualquiera>" and valoracion != "<Cualquiera>": #Caso en el que se busque por valoración, género y nombre.
            pelis_nom = []
            for pelicula in peliculas:
                if nombre.lower() in pelicula[0].lower() or nombre.lower() in pelicula[1].lower():
                    if pelicula[4] == valoracion:
                        pelis_nom.append(pelicula)

            for dupla_generos in generos: #Mismo proceso que en búsqueda por género y nombre.
                if genero.lower() == dupla_generos[0].lower() or genero.lower() == dupla_generos[1].lower():
                    for subgenero in generos:
                        if subgenero[1].lower() == genero.lower():
                            for pelicula in pelis_nom:
                                if pelicula[2].lower() == subgenero[0].lower():
                                    lista_resultados.append(pelicula)

                    for pelicula in pelis_nom:
                        if pelicula[2].lower() == genero.lower():
                            lista_resultados.append(pelicula)
                    break

        #Numero resultados
        numero_resultados["text"] = f"Se han encontrado {len(lista_resultados)} resultados"
        if len(lista_resultados) == 1:
            numero_resultados["text"] = "Se ha encontrado 1 resultado"

        
        #Inserta los resultados en la tabla
        for resultado in lista_resultados:
            resultados.insert("","end",values=(resultado[0].title(),resultado[1].title(),resultado[2].capitalize(),str(resultado[3]),str(resultado[4]) + "/5"))
        
        #Muestra la tabla con los resultados
        numero_resultados.grid(row=3,column=0,sticky="w",pady=(0,30))
        resultados_frame.grid(row=4,column=0,columnspan=4,sticky="nswe")
        
        #Cierra los filtros
        cierra_filtros()
    
    #Funciones de limpieza
    def limpia_filtros():
        combo_genero.set("<Cualquiera>")
        combo_valoracion.set("<Cualquiera>")
    
    def limpia_resultados():
        resultados.delete(*resultados.get_children())
            
    #Funcion que permite al usuario volver al menú principal
    def volver_home():
        #Modifica el estilo del arbol de generos
        style.configure("Treeview", 
            font=("Calibri",17),
            background=LIGHT_COLOR,
            rowheight=35,
            fieldbackground=LIGHT_COLOR,
            borderwidth=0,
            )
        
        style.configure("Treeview.Heading",
            borderwidth=0,
            font=("Calibri",13)
        )
        
        #Desactiva el botón home
        home_button["state"] = "disabled"
        home_button["cursor"] = "arrow"

        #Muestra el boton para cambiar a peliculas
        lista_peliculas_btn.grid()
        
        #Muestra el arbol de generos
        generos_titulo.grid()
        generos_frame.grid()
        #Elimina tabla de resultados
        numero_resultados.grid_remove()
        resultados_frame.grid_remove()
        #Limpia los resultados
        limpia_resultados()
        #Limpia los filtros
        limpia_filtros()
        #Limpia el entry
        cierra_filtros()
        search.delete(0,END)
        search.focus_set()
        root.focus_set()
    
    
    #Funciones de actualizacion (al añadir peliculas y añadir generos)
    def actualiza_generos():
        global generos
        
        #se define la nueva pantalla
        gen_window = Toplevel(root)
        #llama a la funcion anadir_genero, que crea la nueva ventana

        anadir_genero(gen_window,enter,leave)
        #para que la ventana principal espere a que se cierre la nueva ventana antes de seguir con su ejecucion

        gen_window.grab_set()
        root.wait_window(gen_window)

        #cuando se cierra la ventana, lee nuevamente el archivo de generos y crea una lista con los generos
        archivo_generos.seek(0)
        generos = crea_lista(archivo_generos)

        #reinicia el arbol de generos y el combobox
        arbol_generos.delete(*arbol_generos.get_children())
        llena_arbol()
        combo_genero.delete(0,END)
        llena_combo()
    

    def actualiza_peliculas():
        global peliculas
        
        #se define la nueva pantalla
        pel_window = Toplevel(root)
        #llama a la funcion anadir_genero, que crea la nueva ventana
        anadir_pelicula(pel_window,enter,leave)
        
        #para que la ventana principal espere a que se cierre la nueva ventana antes de seguir con su ejecucion
        pel_window.grab_set()
        root.wait_window(pel_window)
        
        #cuando se cierra la ventana, lee nuevamente el archivo de peliculas y crea una lista con las peliculas
        archivo_peliculas.seek(0)
        peliculas = crea_lista(archivo_peliculas)
        #reinicia la tabla de peliculas
        tabla_peliculas.delete(*tabla_peliculas.get_children())
        llena_peliculas()


    #FUNCIONES EVENTO 'HOVER'
    def enter(evento):
        evento.widget['background'] = BTN_HOVER_COLOR

    def leave(evento):
        evento.widget['background'] = BTN_COLOR
    

    #FUNCIONES EVENTO 'FOCUS'
    def focus_in(evento):
        search["fg"] = "white"
        if evento.widget.get() == "Buscar película":
            search.delete(0,END)
    

    def focus_out(evento):
        if evento.widget.get() == "":
            search["fg"] = LIGHT_TXT_COLOR
            search.insert(END,"Buscar película")
       
    
    '''FRAME PRINCIPAL'''
    app_frame = Frame(root, bg=BG_COLOR)
    
    root.columnconfigure(index=0,weight=1)
    root.rowconfigure(index=0,weight=1)
    app_frame.columnconfigure(index=0,weight=1)
    app_frame.rowconfigure(index=4,weight=1)
    
    app_frame.grid(row=0,column=0,sticky="nswe",padx=30,pady=20)
    
    
    '''BARRA DE BÚSQUEDA'''
    #FRAME
    search_frame = Frame(app_frame,borderwidth=10,bg=LIGHT_COLOR)
    search_frame.columnconfigure(index=0,weight=1)    
    #ENTRY
    search = Entry(search_frame,bg=LIGHT_COLOR,bd=0,fg=LIGHT_TXT_COLOR)
    search["font"] = ("Calibri",13)
    search.insert(END,"Buscar película")
    #BOTON
    search_button = Button(search_frame,image=search_icon,background=LIGHT_COLOR,border=0,command=busqueda,activebackground=LIGHT_COLOR,cursor="hand2")
    
    #POSICIONAMIENTO DE WIDGETS
    search_frame.grid(row=0,column=0, columnspan=3,sticky="nswe")
    search.grid(row=0,column=0,columnspan=3,sticky="nswe")
    search_button.grid(row=0, column=1)
    
    '''BOTONES PRINCIPALES'''
    #VOLVER AL MENU PRINCIPAL
    home_button = Button(app_frame,image=home_icon,bg=BG_COLOR,bd=0,state="disabled",activebackground=BG_COLOR,command=volver_home)
    home_button.grid(row=2,column=0,sticky="w")

    #AÑADIR GENERO Y PELICULA
    button_font = font.Font(size=12,family="Arial",weight="bold")

    button_pel = Button(app_frame, text="Añadir película",bg=BTN_COLOR,fg=TXT_COLOR,pady=12,padx=60,border=0,activebackground=BTN_ACTIVE_COLOR, activeforeground="white",cursor="hand2",command=actualiza_peliculas)
    button_pel["font"] = button_font
    button_pel.grid(row=2,column=3,pady=(80,60),sticky="we")
    
    button_gen = Button(app_frame, text="Añadir género",bg=BTN_COLOR,fg=TXT_COLOR,pady=12,padx=60,border=0,activebackground=BTN_ACTIVE_COLOR,activeforeground="white",cursor="hand2",command=actualiza_generos)
    button_gen["font"] = button_font
    button_gen.grid(row=2,column=2,sticky="we",padx=30,pady=(80,60))
    
    '''FILTROS'''
    #BOTÓN DE FILTROS
    button_filt = Button(app_frame,text="Filtros",bg=LIGHT_COLOR,fg=TXT_COLOR,border=0,height=2,command=menu_filtros,image=filtros_icon,compound="right",padx=10,activebackground=LIGHT_COLOR,activeforeground="white",cursor="hand2")
    button_filt["font"] = ("Calibri", 13)
     
    #MENÚ DE FILTROS (FILTROS PRINCIPALES)
    filtros_frame = Frame(app_frame,bg=LIGHT_COLOR)
    filtros_frame.columnconfigure(index=1, weight=1)
    
    genero_txt = Label(filtros_frame,text="Género",fg="white",bg=LIGHT_COLOR)        
    genero_txt["font"] = ("Calibri",15)

    valoracion_txt = Label(filtros_frame,text="Valoración",fg="white",bg=LIGHT_COLOR)
    valoracion_txt["font"] = ("Calibri",15)

    #COMBOBOX GÉNERO
    combo_genero = ttk.Combobox(filtros_frame,font=("Calibri",13),justify="center",style="Mystyle.TCombobox")
    combo_genero["state"] = "readonly"
    combo_genero.set("<Cualquiera>")
    llena_combo() #llena el combobox con los generos
    
    #COMBOBOX VALORACIÓN
    combo_valoracion = ttk.Combobox(filtros_frame,font=("Calibri",13),justify="center",style="Mystyle.TCombobox")
    combo_valoracion["state"] = "readonly"
    combo_valoracion.set("<Cualquiera>")
    combo_valoracion["values"] = ("<Cualquiera>",1,2,3,4,5)

    #POSICIONAMIENTO DE LOS WIDGETS
    button_filt.grid(row=0,column=3,sticky="nswe",padx=(30,0))
    genero_txt.grid(row=0,column=0,padx=(30,0),pady=45,sticky="w")
    combo_genero.grid(row=0,column=1,pady=45,padx=(0,30),sticky="nswe")
    valoracion_txt.grid(row=1,column=0, sticky="w",padx=(30,20))
    combo_valoracion.grid(row=1,column=1,padx=(0,30),sticky="nswe")
    
    '''SECCIÓN VISTA DE ÁRBOL: GÉNEROS'''
    #BOTÓN
    arbol_generos_btn = Button(app_frame,image=genre_icon,bg=BG_COLOR,bd=0,activebackground=BG_COLOR,cursor="hand2",command=despliega_generos)
    
    #TÍTULO Y CONTENEDOR
    generos_titulo = Label(app_frame,text="Géneros",bg=BG_COLOR,fg=TXT_COLOR)
    generos_titulo["font"] = ("Calibri", 32)
    
    generos_frame = Frame(app_frame,bg=LIGHT_COLOR)
    generos_frame.columnconfigure(index=0, weight=1)
    generos_frame.rowconfigure(index=0, weight=1)
    
    #ÁRBOL DE GÉNEROS
    arbol_generos = ttk.Treeview(generos_frame,style="nodotbox.Treeview")
    arbol_generos.columnconfigure(index=0, weight=1)
    arbol_generos.rowconfigure(index=0, weight=1)
    llena_arbol() #Llena el arbol con los generos
    
    #SCROLLBAR
    arbol_scrollbar = AutoScrollbar(arbol_generos,command=arbol_generos.yview,orient="vertical")
    arbol_generos.configure(yscrollcommand=arbol_scrollbar.set)
    
    #POSICIONAMIENTO DE LOS WIDGETS
    generos_titulo.grid(row=3,column=0,sticky="w",pady=(0,20))
    generos_frame.grid(row=4,column=0,columnspan=4,sticky="nswe")
    arbol_scrollbar.grid(row=0,column=0,sticky="nse")
    arbol_generos.grid(row=0,column=0, sticky="nswe",padx=(10,0))
    
    '''SECCIÓN PELÍCULAS'''
    #BOTÓN
    lista_peliculas_btn = Button(app_frame,image=movie_icon,bg=BG_COLOR,bd=0,activebackground=BG_COLOR,cursor="hand2",command=despliega_peliculas)
    lista_peliculas_btn.grid(row=3,column=3,sticky="e",pady=(0,30))
    
    #FRAME Y TEXTO
    peliculas_titulo = Label(app_frame,text="Películas",bg=BG_COLOR,fg=TXT_COLOR,font=("Calibri",32))
    peliculas_frame = Frame(app_frame,bg=BG_COLOR)
    peliculas_frame.columnconfigure(index=0,weight=1)
    peliculas_frame.rowconfigure(index=0,weight=1)
    
    #TABLA
    tabla_columnas = ("Nombre","Director","Genero","Año","Valoracion")
    
    tabla_peliculas = ttk.Treeview(peliculas_frame, columns=tabla_columnas, show="headings")
    tabla_peliculas.columnconfigure(index=0,weight=1)
    tabla_peliculas.rowconfigure(index=0,weight=1)
    
    tabla_peliculas.column("Nombre", anchor="w",minwidth=275)
    tabla_peliculas.column("Director", anchor="w")
    tabla_peliculas.column("Año", anchor="center",width=80)
    tabla_peliculas.column("Genero", anchor="w")
    tabla_peliculas.column("Valoracion", anchor="center",width=150)

    tabla_peliculas.heading("Nombre", text="Nombre",anchor="w")
    tabla_peliculas.heading("Director", text="Director",anchor="w")
    tabla_peliculas.heading("Año", text="Año",anchor="center")
    tabla_peliculas.heading("Genero", text="Género",anchor="w")
    tabla_peliculas.heading("Valoracion", text="Valoración",anchor="center")
    
    llena_peliculas() #Llena la tabla de peliculas con las peliculas
    
    #SCROLLBAR
    tabla_peliculas_scrollbar = AutoScrollbar(tabla_peliculas,command=tabla_peliculas.yview,orient="vertical")
    tabla_peliculas.configure(yscrollcommand=tabla_peliculas_scrollbar.set)
    
    #POSICIONAMIENTO DE LOS WIDGETS
    tabla_peliculas.grid(row=0,column=0,sticky="nswe")
    tabla_peliculas_scrollbar.grid(row=0,column=0,sticky="nse")
    
    '''RESULTADOS DE BÚSQUEDA'''
    #FRAME Y TEXTO
    resultados_frame = Frame(app_frame,bg=BG_COLOR)
    resultados_frame.columnconfigure(index=0,weight=1)
    resultados_frame.rowconfigure(index=0,weight=1)
    
    numero_resultados = Label(app_frame,bg=BG_COLOR,fg="white")
    numero_resultados["font"] = ("Calibri",16)

    #TABLA CON TÍTULO, AUTOR, GÉNERO, AÑO Y VALORACIÓN
    resultados = ttk.Treeview(resultados_frame, columns=tabla_columnas, show="headings")
    resultados.columnconfigure(index=0,weight=1)
    resultados.rowconfigure(index=0,weight=1)
    
    resultados.column("Nombre", anchor="w",minwidth=275)
    resultados.column("Director", anchor="w")
    resultados.column("Año", anchor="center",width=80)
    resultados.column("Genero", anchor="w")
    resultados.column("Valoracion", anchor="center",width=150)

    resultados.heading("Nombre", text="Nombre",anchor="w")
    resultados.heading("Director", text="Director",anchor="w")
    resultados.heading("Año", text="Año",anchor="center")
    resultados.heading("Genero", text="Género",anchor="w")
    resultados.heading("Valoracion", text="Valoración",anchor="center")

    #SCROLLBAR
    resultados_scrollbar = AutoScrollbar(resultados,command=resultados.yview,orient="vertical")
    resultados.configure(yscrollcommand=resultados_scrollbar.set)
    
    #POSICIONAMIENTO DE LOS WIDGETS
    resultados.grid(row=0,column=0,sticky="nswe")
    resultados_scrollbar.grid(row=0,column=0,sticky="nse")
    
    '''EVENTOS'''
    #Eventos secundarios
    button_gen.bind("<Enter>",enter)
    button_gen.bind("<Leave>",leave)
    
    button_pel.bind("<Enter>",enter)
    button_pel.bind("<Leave>",leave)
    
    search.bind("<FocusIn>",focus_in)
    search.bind("<FocusOut>",focus_out)
    search.bind("<Return>",busqueda)

    '''MAINLOOP'''
    root.mainloop()
   
main()