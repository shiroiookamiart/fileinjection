#bin/python
#codigo por david beltran shiro 

import json
import os
import pymysql

conexion = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    db="namedb"
)

folder_path = "path"
datasave = {}

cursor = conexion.cursor()

for filename in os.listdir(folder_path):
    print("procesado archivo: ", filename)
    if filename.endswith(".json"):
        with open(os.path.join(folder_path, filename), "r") as f:
            data = json.load(f)
            datasave["column_1"] = data["column_1"]
            datasave["column_2"] = data["column_2"]
            datasave["column_3"] = data["column_3"]
            query = "INSERT INTO data (column_1, column_2, column_3) VALUES (%s, %s, %s)"
            values = (datasave["column_1"] , datasave["column_2"] , str(datasave["column_3"]))
            cursor.execute(query, values)
            conexion.commit()

            #print(json.dumps(data, indent=4))

cursor.close()
conexion.close()            
