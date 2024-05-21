import mysql.connector
from mysql.connector import Error

def connect():
    """ Conectar a la base de datos MySQL """
    try:
        connection = mysql.connector.connect(
            host='122.122.124.8',
            database='doblenet',
            user='dni',
            password='MinuzaFea265/'
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado a MySQL Server versión {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"Conectado a la base de datos: {record}")

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

if __name__ == "__main__":
    connect()
