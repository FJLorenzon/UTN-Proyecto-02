'''
Created on 25 jun 2026

@author: ati05
'''

import customtkinter as ctk
import db
import funciones as fn

# ----- INICIAMOS LA DB
db.crear_tablas()

# ----- TEMA
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

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


#------------------------------------
# --- FRAME BOTONES
#------------------------------------
main_frame = ctk.CTkFrame(app, width=280, height=120)
main_frame.grid(row=0, column=0, padx=20, pady=10, sticky='ew')
main_frame.grid_propagate(False)

# --- Botonera
btn01 = ctk.CTkButton(main_frame, text='Cargar jugador', width=200, height=10, command=lambda:fn.cargar_jugador(carga_frame))
btn01.grid(row=0, column=0, padx=40, pady=8)

btn02 = ctk.CTkButton(main_frame, text='Cargar penales', width=200, height=10, command=lambda:fn.cargar_penal(carga_frame))
btn02.grid(row=1, column=0, padx=40, pady=8)

btn03 = ctk.CTkButton(main_frame, text='Ver gráfico', width=200, height=10, command=lambda:fn.ver_grafico(carga_frame))
btn03.grid(row=2, column=0, padx=40, pady=8)


#------------------------------------
# --- FRAME CARGA DE DATOS
#------------------------------------
carga_frame = ctk.CTkFrame(app, width=280, height=200)
carga_frame.grid(row=1, column=0, padx=20, pady=10, sticky='nsew')
carga_frame.grid_propagate(False)





#------------------------------------
#--------- FOOTER 
#------------------------------------
footer = ctk.CTkFrame(app, height=80, corner_radius=0)
footer.grid(row=3, column=0, sticky='ew')
# Texto footer
texto_footer = ctk.CTkLabel(footer, text='UTN Proyecto 2026 - Franco Lorenzon', font=('Arial', 10))
texto_footer.grid(padx=70, pady=4)


app.mainloop()