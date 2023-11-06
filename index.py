#bin/python

import json
import os
import pymysql

conexion = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    db="plinko"
)

folder_path = "D:\Documentos\Programas\Godot\Godot\plinko\WorldGame01"
datasave = {}

cursor = conexion.cursor()

for filename in os.listdir(folder_path):
    print("procesado archivo: ", filename)
    if filename.endswith(".json"):
        with open(os.path.join(folder_path, filename), "r") as f:
            data = json.load(f)
            datasave["angulo_salida"] = data["angulo_salida"]
            datasave["angulo_ruido"] = data["angulo_salida_con_ruido"]
            datasave["coordenadas"] = data["coordenadas"]
            query = "INSERT INTO datos (angulo, angulo_ruido, coordenadas) VALUES (%s, %s, %s)"
            values = (datasave["angulo_salida"] , datasave["angulo_ruido"] , str(datasave["coordenadas"]))
            cursor.execute(query, values)
            conexion.commit()

            #print(json.dumps(data, indent=4))

cursor.close()
conexion.close()            