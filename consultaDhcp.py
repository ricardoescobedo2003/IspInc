import tkinter as tk
from tkinter import ttk
from librouteros import connect
from corteCliente import dhcpEnvio

# Función para obtener las leases DHCP
def obtener_leases():
    api = connect(username='admin', password='070523', host='122.122.124.1')
    leases = api('/ip/dhcp-server/lease/print')

    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    root.title("DHCP Leases")

    # Crear un Treeview para mostrar las leases
    tree = ttk.Treeview(root, columns=('IP Address', 'Active Hostname'), show='headings')
    tree.heading('IP Address', text='IP Address')
    tree.heading('Active Hostname', text='Active Hostname')
    tree.pack(fill=tk.BOTH, expand=True)

    # Obtener las leases y añadirlas al Treeview
    leases = obtener_leases()
    for lease in leases:
        address = lease.get('address')
        hostname = lease.get('host-name')
        if address and hostname:
            tree.insert('', 'end', values=(address, hostname))

    # Iniciar el loop de Tkinter
    root.mainloop()

datos = dhcpEnvio('mi_hostname', 'mi_username', 'mi_password')
print(datos['hostname'])  # Esto imprimirá 'mi_hostname'
print(datos['username'])  # Esto imprimirá 'mi_username'
print(datos['password'])  # Esto imprimirá 'mi_password'w