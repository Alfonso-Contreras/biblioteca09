# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:38:56 2022

@author: Alfonso
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")
cursor=conexion.cursor()
consulta="""UPDATE EDITORIAL SET NOMBRE='Editorial imprenta union
WHERE IDEDITORAIL=1'"""



cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()