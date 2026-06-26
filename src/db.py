'''
Created on 25 jun 2026

@author: ati05
'''

import sqlite3

conexion = sqlite3.connect("datos_penales.db")
cursor = conexion.cursor()

def crear_tablas():

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jugadores(
            id_jugador INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            pierna TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS penales(
            id_penal INTEGER PRIMARY KEY AUTOINCREMENT,
            id_jugador INTEGER NOT NULL,
            equipo TEXT NOT NULL,
            penal TEXT NOT NULL,
            FOREIGN KEY(id_jugador)
            REFERENCES jugadores(id_jugador)
        )
    """)

    conexion.commit()


### DEFINIMOS LOS INSERTS
#--------------------------------------------------
def insertar_jugador(nombre, pierna):
    cursor.execute(
        "INSERT INTO jugadores(nombre, pierna) VALUES (?, ?)",
        (nombre, pierna)
    )
    conexion.commit()
    
def insertar_penal(id_jugador, equipo, penal):
    cursor.execute(
        "INSERT INTO penales (id_jugador, equipo, penal) VALUES (?,?,?)", 
        (id_jugador, equipo, penal)
    )
    conexion.commit()
    
def select_jugadores():
    cursor.execute("SELECT * FROM jugadores ORDER BY nombre")
    return cursor.fetchall()
    
def select_penales(id_jugador):
    cursor.execute("SELECT * FROM penales WHERE id_jugador = ?", (id_jugador,))
    return cursor.fetchall()
    
    
    
    
    
    

