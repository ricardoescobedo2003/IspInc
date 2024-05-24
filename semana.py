import paramiko
import schedule
import time

def adjust_bandwidth(queue_name, new_max_limit, hostname, username, password):
    # Función para ajustar el ancho de banda
    port = 22  # Puerto SSH, generalmente es 22

    # Comando para ajustar el ancho de banda
    command = f'/queue simple set [find name="{queue_name}"] max-limit={new_max_limit}'

    # Crear una instancia del cliente SSH
    client = paramiko.SSHClient()

    # Agregar automáticamente la clave del servidor si no está en la lista de known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conectarse al dispositivo
        client.connect(hostname, port, username, password)
        
        # Ejecutar el comando para ajustar el ancho de banda
        stdin, stdout, stderr = client.exec_command(command)
        
        # Leer y mostrar la salida del comando, si es necesario
        output = stdout.read().decode()
        errors = stderr.read().decode()
        
        if output:
            print(f"Output: {output}")
        if errors:
            print(f"Errors: {errors}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Cerrar la conexión
        client.close()

def main():
    # Datos del usuario
    hostname = "122.122.124.1"
    username = "admin"
    password = "070523"
    queue_name = "Madrina"

    # Configurar horarios y límites de ancho de banda
    start_time = "22:30"
    first_limit = "1k/1k"
    end_time = "06:00"
    second_limit = "100M/15M"

    # Programar tareas con schedule
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'sunday']
    for day in days:
        schedule.every().__getattribute__(day).at(start_time).do(adjust_bandwidth, queue_name, first_limit, hostname, username, password)
        schedule.every().__getattribute__(day).at(end_time).do(adjust_bandwidth, queue_name, second_limit, hostname, username, password)

    print(f"Scheduler iniciado. Ejecutando ajustes de ancho de banda a las {start_time} y {end_time} los días {', '.join(days)}...")

    # Bucle infinito para mantener el script en ejecución y verificar el horario
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()