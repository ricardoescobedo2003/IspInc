import paramiko
import re

def consultar_trafico_mikrotik(host, username, password, ip_client):
    try:
        # Conectarse al dispositivo MikroTik
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=username, password=password)

        # Ejecutar el comando para obtener las colas
        stdin, stdout, stderr = client.exec_command('/queue simple print')

        # Leer la salida y buscar la información de la IP en las colas
        queues_output = stdout.read().decode('utf-8')

        # Buscar la información de la IP en las colas
        queues_info = []
        for line in queues_output.splitlines():
            if 'name=' in line and 'target=' in line:
                name_match = re.search(r'name=(\S+)', line)
                target_match = re.search(r'target=(\S+)', line)
                if name_match and target_match:
                    queue_name = name_match.group(1)
                    target_ip = target_match.group(1)
                    if target_ip == ip_client:
                        queues_info.append(queue_name)

        # Si se encontraron colas que coinciden, obtener detalles
        if queues_info:
            for queue_name in queues_info:
                command = f'/queue simple print detail where name={queue_name}'
                stdin, stdout, stderr = client.exec_command(command)
                queue_detail = stdout.read().decode('utf-8')
                print(queue_detail)

        else:
            print(f'No se encontró tráfico para la IP {ip_client}')

        # Cerrar la conexión
        client.close()

    except Exception as e:
        print(f'Error: {str(e)}')

# Ejemplo de uso:
host = '122.122.124.1'
username = 'admin'
password = '070523'
ip_client = '122.122.123.18'

consultar_trafico_mikrotik(host, username, password, ip_client)
