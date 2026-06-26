'''
Created on 25 jun 2026

@author: ati05
'''

import customtkinter as ctk
import db

# ----- INICIAMOS LA DB
db.crear_tablas()

# ----- TEMA
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')


#------------------------------------
#--------- FUNCIONES 
#------------------------------------
def cargar_jugador():
    # Titulo
    texto_carga = ctk.CTkLabel(carga_frame, text = '-- CARGAR JUGADOR --')
    texto_carga.grid(padx=70, pady= 5)
    
    # Entry carga jugador
    entry_jugador = ctk.CTkEntry(carga_frame, placeholder_text= 'Ingresar nombre del jugador', width=270)
    entry_jugador.grid(row=1, column=0, padx=5, pady=10)

    # Pierna jugador
    label_pierna = ctk.CTkLabel(carga_frame, text='Perfil de ejecución:')
    label_pierna.grid(row=2, column=0, padx=(5,0), pady=10, sticky='w')
    lista_pierna = ctk.CTkOptionMenu(carga_frame, values=['Zurdo', 'Diestro'], width=120, fg_color=('gray20'), button_color=('gray30'), button_hover_color=('gray35'),text_color=('white'))
    lista_pierna.grid(row=2, column=0, padx=(0,5), pady=10, sticky='e')
    
    # Boton guardar
    btn_carga = ctk.CTkButton(carga_frame, text='GUARDAR', width=60, height=20, command=lambda: guardar_jugador(entry_jugador, lista_pierna))
    btn_carga.grid(row=3, column=0, padx=40, pady=15)
    
    
def guardar_jugador(entry_jugador, lista_pierna):
    # Guardamos los datos del jugador
    nombre = entry_jugador.get()
    pierna = lista_pierna.get()

    # Llamamos a la fuction que inserta los valores en la db
    db.insertar_jugador(nombre, pierna)
    
    # Vaciamos los campos
    entry_jugador.delete(0, 'end')
    lista_pierna.set('Zurdo')
    
def cargar_penales():
    # Titulo
    texto_carga = ctk.CTkLabel(carga_frame, text = '-- CARGAR PENALES --')
    texto_carga.grid(padx=70, pady= 5)
    
    # Entry carga jugador
    label_jugador = ctk.CTkLabel(carga_frame, text='Jugador:')
    label_jugador.grid(row=1, column=0, padx=(5,0), pady=10, sticky='w')
    # Traemos los jugadores de la db
    jugadores= db.select_jugadores()
    jugador_valor= {jugador[1]: jugador[0] for jugador in jugadores}
    # Armamos la lista con los jugadores
    combobox_jugador = ctk.CTkComboBox(carga_frame,values=list(jugador_valor.keys()), width=190)
    combobox_jugador.grid(row=1, column=0, padx=(0,5), pady=10, sticky='e')
    combobox_jugador.set('')

    '''
    # Pierna jugador
    label_pierna = ctk.CTkLabel(carga_frame, text='Perfil de ejecución:')
    label_pierna.grid(row=2, column=0, padx=(5,0), pady=10, sticky='w')
    lista_pierna = ctk.CTkOptionMenu(carga_frame, values=['Zurdo', 'Diestro'], width=120, fg_color=('gray20'), button_color=('gray30'), button_hover_color=('gray35'),text_color=('white'))
    lista_pierna.grid(row=2, column=0, padx=(0,5), pady=10, sticky='e')
    '''
    
    # Boton guardar
    btn_carga = ctk.CTkButton(carga_frame, text='GUARDAR', width=60, height=20, command=lambda: guardar_jugador(combobox_jugador, lista_pierna))
    btn_carga.grid(row=3, column=0, padx=40, pady=15)

def ver_grafico():
    jugadores = db.select_jugadores()
    print(jugadores)

#------------------------------------
#--------- INTERFAZ DE LA VENTANA 
#------------------------------------
app = ctk.CTk()  
app.title('Anotador de penales')
app.geometry('320x480')  
app.resizable(False, False)

# Configurar el temaño de la cuadrícula para centrar el contenido
app.grid_rowconfigure(0, weight=0)  # main_frame
app.grid_rowconfigure(1, weight=1)  # carga_frame
app.grid_rowconfigure(2, weight=0)  # footer
app.grid_columnconfigure(0, weight=1)  # Configura la columna 0 de la ventana para que ocupe todo el espacio disponible

# --- FRAME BOTONES
#------------------------------------
main_frame = ctk.CTkFrame(app, width=280, height=150)
main_frame.grid(row=0, column=0, padx=20, pady=20, sticky='ew')
main_frame.grid_propagate(False)

# --- Botonera
btn01 = ctk.CTkButton(main_frame, text='Cargar jugador', width=200, height=10, command=cargar_jugador)
btn01.grid(row=0, column=0, padx=40, pady=8)

btn02 = ctk.CTkButton(main_frame, text='Cargar penales', width=200, height=10, command=cargar_penales)
btn02.grid(row=1, column=0, padx=40, pady=8)

btn03 = ctk.CTkButton(main_frame, text='Ver gráfico', width=200, height=10, command=ver_grafico)
btn03.grid(row=2, column=0, padx=40, pady=8)


# --- FRAME CARGA DE DATOS
#------------------------------------
carga_frame = ctk.CTkFrame(app, width=280, height=200)
carga_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
carga_frame.grid_propagate(False)



#------------------------------------
#--------- FOOTER 
#------------------------------------
footer = ctk.CTkFrame(app, height=80, corner_radius=0)
footer.grid(row=2, column=0, sticky='ew')
# Texto footer
texto_footer = ctk.CTkLabel(footer, text='UTN Proyecto 2026 - Franco Lorenzon', font=('Arial', 10))
texto_footer.grid(padx=70, pady=5)

app.mainloop()
