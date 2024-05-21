import mysql.connector
from mysql.connector import Error


def insertar_datos(no_cliente, nombre, direccion, telefono, fechaInstalacion, equipos, mensualidad, localidad, comentarios, paquete, ip):
            # Conexión a la base de datos
            conexion =  connect_and_query()

            if conexion.is_connected():
                cursor = conexion.cursor()

                # Consulta SQL para insertar datos
                sql_insert_query = """ INSERT INTO clientes (no_cliente, nombre, direccion, telefono, fechaInstalacion, equipos, mensualidad, localidad, comentarios, paquete, ip)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
                datos = (no_cliente, nombre, direccion, telefono, fechaInstalacion, equipos, mensualidad, localidad, comentarios, paquete, ip)

                # Ejecutar la consulta
                cursor.execute(sql_insert_query, datos)

                # Confirmar la transacción
                conexion.commit()

                print("Se guardo de manera correcta tu cliente: " + nombre)

                if conexion.is_connected():
                    cursor.close()
                    conexion.close()
                    print("Conexión a MySQL cerrada")


def connect_and_query():
    """ Conectar a la base de datos MySQL y realizar una consulta """

        # Conexión a la base de datos
    return mysql.connector.connect(
            host='122.122.124.8',
            database='doblenet',
            user='dni',
            password='MinuzaFea265/'
        )
insertar_datos(1, "test", "test", "1234567890", "2024-05-04", "M5", "300", "Loreto", "Test Remoto","100M/20M", "122.122.126.4") 