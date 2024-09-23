import mysql.connector

conexion = mysql.connector.connect(user='root', password='Lissa@1234@', host="localhost", database="pruebapy", port='3306') #Para iniciar la conexcion del sql.

print(conexion) #probamos que la conexion funcione.