'''
Created on 26 jun 2026

@author: ati05
'''
import customtkinter as ctk
import random
import matplotlib.pyplot as plt
from collections import Counter
import db


#------------------------------------
#--------- FUNCIONES DE FRAME GLOBAL
#------------------------------------
def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        

#------------------------------------
#--------- FUNCIONES DE FRAME JUGADOR
#------------------------------------
def cargar_jugador(carga_frame):
    # Vaciamos el frame carga_frame
    limpiar_frame(carga_frame)
    
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
    
    
#------------------------------------
#--------- FUNCIONES DE FRAME PENAL 
#------------------------------------
def cargar_penal(carga_frame):
    # Vaciamos el frame carga_frame
    limpiar_frame(carga_frame)
    
    # Titulo
    texto_carga = ctk.CTkLabel(carga_frame, text = '-- CARGAR PENALES --')
    texto_carga.grid(padx=70, pady= 5)
    
    # Label carga jugador
    label_jugador = ctk.CTkLabel(carga_frame, text='Jugador:')
    label_jugador.grid(row=1, column=0, padx=(5,0), pady=8, sticky='w')
    # Traemos los jugadores de la db
    jugadores= db.select_jugadores()
    jugador_valor= {jugador[1]: jugador[0] for jugador in jugadores}
    # Armamos la lista con los jugadores
    combobox_jugador = ctk.CTkComboBox(carga_frame,values=list(jugador_valor.keys()), width=190)
    combobox_jugador.grid(row=1, column=0, padx=(0,5), pady=8, sticky='e')
    combobox_jugador.set('')
    
    # Entry partido que pateo el penal
    entry_equipo = ctk.CTkEntry(carga_frame, placeholder_text= 'Equipo que recibió el penal', width=270)
    entry_equipo.grid(row=2, column=0, padx=5, pady=8)

    # Label penales
    label_jugador = ctk.CTkLabel(carga_frame, text='Ejecución:')
    label_jugador.grid(row=3, column=0, padx=(5,0), pady=8, sticky='w')    
    # Armamos la lista de los lugares donde patea
    lugares= ('Centro', 'Arriba izquierda', 'Abajo izquierda', 'Arriba derecha', 'Abajo derecha')
    combobox_penal = ctk.CTkComboBox(carga_frame,values=lugares, width=190)
    combobox_penal.grid(row=3, column=0, padx=(0,5), pady=8, sticky='e')
    combobox_penal.set('')
    
    # Boton guardar
    btn_carga = ctk.CTkButton(carga_frame, text='GUARDAR', width=60, height=20, command=lambda: guardar_penal(combobox_jugador, jugador_valor, entry_equipo, combobox_penal))
    btn_carga.grid(row=4, column=0, padx=50, pady=10)
    
    
    
def guardar_penal(combobox_jugador, jugador_valor, entry_equipo, combobox_penal):
    # Guardamos los datos del jugador
    nombre = combobox_jugador.get()
    id_jugador = jugador_valor[nombre]
    equipo = entry_equipo.get()
    penal = combobox_penal.get()

    # Llamamos a la fuction que inserta los valores en la db
    db.insertar_penal(id_jugador, equipo, penal)
    
    # Vaciamos solamente el campo penal
    entry_equipo.delete(0, 'end')
    combobox_penal.set('')


#------------------------------------
#--------- FUNCIONES DEL GRAFICO 
#------------------------------------
def ver_grafico(carga_frame):
    # Vaciamos el frame carga_frame
    limpiar_frame(carga_frame)
    
    # Titulo
    texto_carga = ctk.CTkLabel(carga_frame, text = '-- GRÁFICO PENALES --')
    texto_carga.grid(padx=70, pady= 5)
    
    # Label carga jugador
    label_jugador = ctk.CTkLabel(carga_frame, text='Jugador:')
    label_jugador.grid(row=1, column=0, padx=(5,0), pady=8, sticky='w')
    # Traemos los jugadores de la db
    jugadores= db.select_jugadores()
    jugador_valor= {jugador[1]: jugador[0] for jugador in jugadores}
    # Armamos la lista con los jugadores
    combobox_jugador = ctk.CTkComboBox(carga_frame,values=list(jugador_valor.keys()), width=190)
    combobox_jugador.grid(row=1, column=0, padx=(0,5), pady=8, sticky='e')
    combobox_jugador.set('')
    
    # Boton guardar
    btn_carga = ctk.CTkButton(carga_frame, text='GRAFICAR', width=60, height=20, command=lambda: generar_grafico(combobox_jugador, jugador_valor))
    btn_carga.grid(row=2, column=0, padx=50, pady=10)
    
    
def generar_grafico(combobox_jugador, jugador_valor):
    nombre = combobox_jugador.get()

    if nombre == "":
        print("Selecciona un jugador")
        return

    id_jugador = jugador_valor[nombre]

    # Traer penales desde la DB
    penales = db.select_penales(id_jugador)

    # 0 -> id_penal
    # 1 -> id_jugador
    # 2 -> equipo
    # 3 -> penal
    posiciones = [p[3] for p in penales]

    if not posiciones:
        print("No hay penales cargados")
        return

    # Cantidad de penales por zona
    conteo = Counter(posiciones)
    total_penales = len(posiciones)

    # Crear figura
    _,ax = plt.subplots(figsize=(9, 5))

    # =========================
    # DIBUJAR EL ARCO
    # =========================

    # Marco
    ax.plot([-1, 1], [1, 1], color="black", linewidth=4)
    ax.plot([-1, -1], [0, 1], color="black", linewidth=4)
    ax.plot([1, 1], [0, 1], color="black", linewidth=4)

    # Divisiones
    ax.plot([0, 0], [0, 1], "--", color="gray")
    ax.plot([-1, 1], [0.5, 0.5], "--", color="gray")

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-0.1, 1.15)

    ax.set_aspect("equal")
    ax.axis("off")

    # =========================
    # COORDENADAS
    # =========================
    zonas = {
        "Arriba izquierda": (-0.75, 0.75),
        "Centro": (0, 0.75),
        "Arriba derecha": (0.75, 0.75),
        "Abajo izquierda": (-0.75, 0.25),
        "Abajo derecha": (0.75, 0.25)
    }

    colores = {
        "Arriba izquierda": "red",
        "Centro": "blue",
        "Arriba derecha": "green",
        "Abajo izquierda": "orange",
        "Abajo derecha": "purple"
    }

    # =========================
    # DIBUJAR LOS PENALES
    # =========================
    for posicion in posiciones:

        if posicion not in zonas:
            continue

        x, y = zonas[posicion]

        # Variacion para evitar superposicion
        x += random.uniform(-0.08, 0.08)
        y += random.uniform(-0.08, 0.08)

        ax.scatter(
            x,
            y,
            s=120,
            color=colores[posicion],
            edgecolors="black",
            zorder=3
        )

    # =========================
    # PORCENTAJES
    # =========================
    for zona, (x, y) in zonas.items():

        cantidad = conteo.get(zona, 0)
        porcentaje = (cantidad / total_penales) * 100

        ax.text(
            x,
            y - 0.22,
            f"{cantidad}\n{porcentaje:.1f}%",
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
            bbox=dict(
                boxstyle="round",
                facecolor="white",
                edgecolor="gray",
                alpha=0.85
            )
        )

    # =========================
    # TOTAL DE PENALES
    # =========================
    ax.text(
        -1.15,
        1.08,
        f"Total de penales: {total_penales}",
        fontsize=11,
        fontweight="bold",
        bbox=dict(
            boxstyle="round",
            facecolor="#E8E8E8",
            edgecolor="black"
        )
    )

    # =========================
    # TITULO
    # =========================
    plt.title(f"Distribución de penales - {nombre}", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.show()
