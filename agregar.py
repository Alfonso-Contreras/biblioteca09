# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 09:05:57 2022

@author: Alfonso
"""


import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

consulta =""" INSERT INTO
            PAIS (NOMBRE, ESTADO)
            VALUES('BRASIL', 'A')
          """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()

conexion.close()