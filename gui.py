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


def main(): 
    #configuracion grid app
    root.columnconfigure(index=0,weight=1)
    root.rowconfigure(index=0,weight=1)
    
    app_frame = Frame(root, bg=BG_COLOR)
    app_frame.columnconfigure(index=0,weight=1)
    app_frame.rowconfigure(index=4,weight=1)
    
    app_frame.grid(row=0,column=0,sticky="nswe",padx=30,pady=20)
    
    #styles
    style = ttk.Style()
    style.theme_use("alt")

    root.option_add('*TCombobox*Listbox*Background', LIGHT_COLOR)
    root.option_add('*TCombobox*Listbox*Foreground', "white")
    root.option_add('*TCombobox*Listbox*selectBackground', BTN_COLOR)
    root.option_add('*TCombobox*Listbox*selectForeground', "white")
    root.option_add('*TCombobox*Listbox*font', ("Calibri",13))

    style.map('TCombobox', fieldbackground=[('readonly', LIGHT_COLOR)])
    style.map('TCombobox', selectbackground=[('readonly', LIGHT_COLOR)])
    style.map('TCombobox', selectforeground=[('readonly', "white")])
    style.map('TCombobox', background=[('readonly', LIGHT_COLOR)])
    style.map('TCombobox', foreground=[('readonly', "white")])

    layout = []
    style.layout("TCombobox", layout)
    
    
    #barra de busqueda
    search_frame = Frame(app_frame,borderwidth=13,bg=LIGHT_COLOR)
    search_frame.columnconfigure(index=0,weight=1)    
    search_frame.grid(row=0,column=0, columnspan=3,sticky="nswe")
    

    search = Entry(search_frame,bg=LIGHT_COLOR,bd=0,fg=LIGHT_TXT_COLOR)
    search["font"] = ("Calibri",13)
    search.insert(END,"Buscar pelicula")
    search.grid(row=0,column=0,columnspan=3,sticky="nswe")
   
    
    combo_filt = ttk.Combobox(app_frame,text="Filtros",font=("Calibri",13),justify="center")
    combo_filt["state"] = "readonly"
    combo_filt.set("Filtros")
    combo_filt["values"] = ("Titulo","Genero","Valoracion")
    
    combo_filt.grid(row=0,column=3,sticky="nswe",padx=(30,0))
    
    #botones
    button_font = font.Font(size=12,family="Arial",weight="bold")

    button_pel = Button(app_frame, text="Añadir pelicula",bg=BTN_COLOR,fg=TXT_COLOR,pady=12,padx=60,border=0)
    button_pel["font"] = button_font
    button_pel.grid(row=2,column=3,pady=80,sticky="we")
    
    button_gen = Button(app_frame, text="Añadir genero",bg=BTN_COLOR,fg=TXT_COLOR,pady=12,padx=60,border=0)
    button_gen["font"] = button_font
    button_gen.grid(row=2,column=2,sticky="we",padx=30)

    #seccion de generos
    titulo = Label(app_frame,text="General",bg=BG_COLOR,fg=TXT_COLOR)
    titulo["font"] = ("Calibri", 32)
    titulo.grid(row=3,column=0,sticky="w",pady=(0,30))

    
    gen_container = Frame(app_frame,bg=BG_COLOR)

    for i in range(4):
        for i2 in range(2):
            gen_card = Button(gen_container,text="Accion",bg=LIGHT_COLOR,fg=TXT_COLOR,padx=80,pady=50,border=0)
            gen_card["font"] = ("Calibri",17)
            if i == 0:
                gen_card.grid(row=i2,column=i,pady=(0,28))
            else:
                gen_card.grid(row=i2,column=i,padx=(28,0),pady=(0,28))
    
    gen_container.grid(row=4,column=0,columnspan=4,sticky="nswe")

    #mainloop
    root.mainloop()
   

main()