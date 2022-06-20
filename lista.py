# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:11:58 2022

@author: Alfonso
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")
cursor=conexion.cursor()
consulta='''SELECT*FROM LIBRO WHERE PRECIO>=55
ORDER BY TITULO'''

cursor=conexion.cursor()
cursor.execute(consulta)

libros=cursor.fetchall()

for libro in libros:
    print(libro)
    conexion.close()