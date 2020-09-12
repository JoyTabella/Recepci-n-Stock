## Comments
# -*- coding: utf-8 -*- 

import MySQLdb

print "Script de Login"

db = MySQLdb.connect(host="localhost",user="root",passwd="papa",db="chbd")

query = db.cursor()

sql = ' SELECT * FROM `usuario` WHERE `nombreUsuario`=nombreUsuario AND `contraseniaUsuario`=contraseniaUsuario  ; '

query.execute(sql)

#filasdeconteo = query.execute(sql)
#print ("filas de conteo " , filasdeconteo)
nombreUI = raw_input("Usuario: ")
contraseniaUI = raw_input("Contrasenia: ")

#data1 = query.fetchone()
 
results = query.fetchall()

if results:
    for row in results:
        nombreUsuario = row[1]
        contraseniaUsuario = row[2]


        if (nombreUI==nombreUsuario and contraseniaUI==contraseniaUsuario):
            print "ingreso ok"
        else:
            print "ingreso incorrecto"
else:
    print "no hay resultados"