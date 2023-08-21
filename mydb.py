# Install.Mysql.on.your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

# Configuración de la conexión a la base de datos
config = {
    'user': 'root',
    'password': '12345',
    'host': 'localhost',
    'database': 'colegio'
}

try:
    # Intenta conectarte a la base de datos
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Conexión exitosa a la base de datos MySQL")
        # Aquí puedes realizar operaciones en la base de datos
        connection.close()
    else:
        print("No se pudo conectar a la base de datos")

except mysql.connector.Error as e:
    print("Error al conectar a la base de datos:", e)