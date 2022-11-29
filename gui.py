from tkinter import *
from tkinter import ttk
import tkinter.font as font

root = Tk()
root.update()
root.configure(bg="#222831")
root.geometry("1080x720")

#variables globales
BG_COLOR = "#222831"
LIGHT_COLOR = "#3A4750"
BTN_COLOR = "#D72323"
TXT_COLOR = "#F1F6F9"
LIGHT_TXT_COLOR = "#A9A9A9"
COMBO_COLOR = "#303841"

#imagenes
arrow_icon = PhotoImage(file="img/arrow.png")
filtros_icon = PhotoImage(file="img/filter.png")
search_icon = PhotoImage(file="img/search.png")

#estados
filtros_estado = 0

#frame principal 
app_frame = Frame(root, bg=BG_COLOR)

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

#styles - treeview
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
    font = ("Calibri",18),
    relief = "flat"
    )

style.configure("Treeview.Heading", background=LIGHT_COLOR, borderwidth=0)
style.map("Treeview.Heading", background=[("hover", "none")])
style.map("Treeview", background=[("selected", BTN_COLOR)])
style.map("Treeview",relief=[("selected","flat")])


def crea_lineas(archivo):
    datos = archivo.readlines()
    for i in range(len(datos)):
        datos[i] = datos[i].lower()
        datos[i] = datos[i].replace("\n","")
        datos[i] = datos[i].replace('"', '')
        datos[i] = datos[i].replace('\ufeff', '')
        datos[i] = datos[i].replace(", ", ",")
        datos[i] = datos[i].split(",")
    return datos

#main
def main(): 
    def menu_filtros():
        global filtros_estado
        nonlocal filtros_frame
        
        if filtros_estado == 1:
            filtros_frame.grid_remove()
            filtros_estado = 0
            return
        
        filtros_frame.grid(row=1,column=0,sticky="nswe",columnspan=4,pady=(8,0),rowspan=2)
        genero_txt.grid(row=0,column=0,padx=(30,0),pady=45,sticky="w")
        combo_genero.grid(row=0,column=1,pady=45,padx=(0,30),sticky="nswe")

        valoracion_txt.grid(row=1,column=0, sticky="w",padx=(30,20))
        combo_valoracion.grid(row=1,column=1,padx=(0,30),sticky="nswe")

        filtros_estado = 1
    
    def busqueda():
        pass
    
    #configuracion grid app
    root.columnconfigure(index=0,weight=1)
    root.rowconfigure(index=0,weight=1)
    app_frame.columnconfigure(index=0,weight=1)
    app_frame.rowconfigure(index=4,weight=1)
    
    app_frame.grid(row=0,column=0,sticky="nswe",padx=30,pady=20)
    
    #barra de busqueda
    search_frame = Frame(app_frame,borderwidth=10,bg=LIGHT_COLOR)
    search_frame.columnconfigure(index=0,weight=1)    
    search_frame.grid(row=0,column=0, columnspan=3,sticky="nswe")
    
    search = Entry(search_frame,bg=LIGHT_COLOR,bd=0,fg=LIGHT_TXT_COLOR)
    search["font"] = ("Calibri",13)
    search.insert(END,"Buscar pelicula")
    search.grid(row=0,column=0,columnspan=3,sticky="nswe")
   
    search_button = Button(search_frame,image=search_icon,background=LIGHT_COLOR,border=0)
    search_button.grid(row=0, column=1)
    
    #Añadir pelicula y genero
    button_font = font.Font(size=12,family="Arial",weight="bold")

    button_pel = Button(app_frame, text="Añadir pelicula",bg=BTN_COLOR,fg=TXT_COLOR,pady=12,padx=60,border=0)
    button_pel["font"] = button_font
    button_pel.grid(row=2,column=3,pady=80,sticky="we")
    
    button_gen = Button(app_frame, text="Añadir genero",bg=BTN_COLOR,fg=TXT_COLOR,pady=12,padx=60,border=0)
    button_gen["font"] = button_font
    button_gen.grid(row=2,column=2,sticky="we",padx=30)
    

    #boton abrir filtros
    button_filt = Button(app_frame,text="Filtros",bg=LIGHT_COLOR,fg=TXT_COLOR,border=0,height=2,command=menu_filtros,image=filtros_icon,compound="right",padx=10)
    
    
    button_filt.grid(row=0,column=3,sticky="nswe",padx=(30,0))
    button_filt["font"] = ("Calibri", 13)

    
    #filtros
    filtros_frame = Frame(app_frame,bg=LIGHT_COLOR)
    filtros_frame.columnconfigure(index=1, weight=1)
    
    genero_txt = Label(filtros_frame,text="Genero",fg="white",bg=LIGHT_COLOR)        
    genero_txt["font"] = ("Calibri",15)

    valoracion_txt = Label(filtros_frame,text="Valoracion",fg="white",bg=LIGHT_COLOR)
    valoracion_txt["font"] = ("Calibri",15)

    combo_genero = ttk.Combobox(filtros_frame,font=("Calibri",13),justify="center",style="Mystyle.TCombobox")
    combo_genero["state"] = "readonly"
    combo_genero.set("<Cualquiera>")
    combo_genero["values"] = ("Accion","Accion","Accion")
        
    combo_valoracion = ttk.Combobox(filtros_frame,font=("Calibri",13),justify="center",style="Mystyle.TCombobox")
    combo_valoracion["state"] = "readonly"
    combo_valoracion.set("<Cualquiera>")
    combo_valoracion["values"] = ("1.0-1.5","1.5-2.0","2.0-2.5")

    #seccion de generos
    titulo = Label(app_frame,text="Generos",bg=BG_COLOR,fg=TXT_COLOR)
    titulo["font"] = ("Calibri", 32)
    titulo.grid(row=3,column=0,sticky="w",pady=(0,30))

    gen_container = Frame(app_frame,bg=BG_COLOR)
    gen_container.columnconfigure(index=0, weight=1)
    gen_container.rowconfigure(index=0, weight=1)
    
    #seccion de generos - arbol de generos
    arbol_generos = ttk.Treeview(gen_container,style="nodotbox.Treeview")
    archivo_generos = open("generos.csv","r",encoding="utf-8")
    generos = crea_lineas(archivo_generos)
    
    arbol_generos.insert("", "end","general",text="General")
    for genero in generos:
        arbol_generos.insert(genero[1],"end",genero[0],text=genero[0].capitalize())
    
    gen_container.grid(row=4,column=0,columnspan=4,sticky="nswe")
    arbol_generos.grid(row=0,column=0, sticky="nswe")
    
    #mainloop
    root.mainloop()
   

main()