from customtkinter import *
import paramiko
from tkinter import messagebox
from librouteros import connect
import tkinter as tk
from tkinter import ttk

set_appearance_mode("light")


def corte():
    app = CTk()
    app.title("Corte de Internet")
    app.geometry("1200x800")
    app.resizable(False, False)

    banner = CTkFrame(master=app, fg_color="#ABB2B9", border_color="#4D5656",corner_radius=0)
    panel = CTkFrame(master=app, fg_color="#ABB2B9", border_color="#4D5656", corner_radius=0)


    def envioDat():
          hostname = hostEntry.get()
          username = usuarioEntry.get()
          password = passwordEntry.get()
          client_ip = ipEntry.get()
          limit = limitOpcions.get()

          comandoCorte(hostname, username, password, client_ip, limit)
          messagebox.showinfo("Corte", "Cliente bloqueado")

    def envioDSB():
          hostname = hostEntry.get()
          username = usuarioEntry.get()
          password = passwordEntry.get()
          client_ip = ipEntry.get()
          limit = freeOpcions.get()

          comandoCorte(hostname, username, password, client_ip, limit)
          messagebox.showinfo("Corte", "Cliente desbloqueado")

    def cambio():
          hostname = hostEntry.get()
          username = usuarioEntry.get()
          password = passwordEntry.get()
          client_ip = ipClienteEntry.get()
          limit = limiteOp.get()

          comandoCorte(hostname, username, password, client_ip, limit)
          messagebox.showinfo("Corte", f"Cambio hecho a {limit}")

    def dchpDat():
          host = hostEntry.get()
          username = usuarioEntry.get()
          password = passwordEntry.get()
          obtener_leases(username, password, host)

    def queues():
          host = hostEntry.get()
          username = usuarioEntry.get()
          password = passwordEntry.get()
          mostrar_queues(username, password, host)

    menuTab = CTkTabview(master=app, width=700, height=550)
    menuTab.add("Corte Indefinido")
    menuTab.add("Corte Por Tiempo")
    menuTab.add("Corte por Fecha")
    menuTab.add("Cambio de Velocidad")

    hostLabel = CTkLabel(master=banner, text="IP Microtik")
    hostEntry = CTkEntry(master=banner,
                         placeholder_text="122.122.124.1",
                         width=150,
                         height=30)
    
    usuarioLabel = CTkLabel(master=banner, text="Usuario")
    usuarioEntry = CTkEntry(master=banner,
                         placeholder_text="admin",
                         width=150,
                         height=30,)

    passwordLabel = CTkLabel(master=banner, text="Password")
    passwordEntry = CTkEntry(master=banner,
                         placeholder_text="********",
                         width=150,
                         height=30,
                         show="*")

    ipLabel = CTkLabel(master=menuTab.tab("Corte Indefinido"), text="Ip Cliente")
    ipEntry = CTkEntry(master=menuTab.tab("Corte Indefinido"),
                       placeholder_text="122.122.126.7",
                       width=150,
                       height=30
                       )
    limitLabel = CTkLabel(master=menuTab.tab("Corte Indefinido"), text="Limite BLK")
    limitOpcions = CTkComboBox(master=menuTab.tab("Corte Indefinido"),
                               values=["1K/1K",
                                       "1M/1M",
                                       "3M/3M"])
    
    freeLabel = CTkLabel(master=menuTab.tab("Corte Indefinido"), text="Limit DSB")
    freeOpcions = CTkComboBox(master=menuTab.tab("Corte Indefinido"),
                               values=["100M/7M",
                                       "100M/15M",
                                       "100M/20M"])
    
    bloquearButton = CTkButton(master=menuTab.tab("Corte Indefinido"),
                                        text="Bloquear",
                                        width=150,
                                        command=envioDat)
    
    desbloquearButton = CTkButton(master=menuTab.tab("Corte Indefinido"),
                                        text="Desbloquear",
                                        width=150,
                                        command=envioDSB)
    



    ipClienteLB = CTkLabel(master=menuTab.tab("Cambio de Velocidad"), text="Ip Cliente")
    ipClienteEntry = CTkEntry(master=menuTab.tab("Cambio de Velocidad"),
                       placeholder_text="122.122.126.7",
                       width=150,
                       height=30
                       )
    limiteLB = CTkLabel(master=menuTab.tab("Cambio de Velocidad"), text="Nv Mbps")
    limiteOp = CTkComboBox(master=menuTab.tab("Cambio de Velocidad"),
                               values=["1K/1K",
                                       "1M/1M",
                                       "3M/3M",
                                       "Modifica manual"])


    cambioButton = CTkButton(master=menuTab.tab("Cambio de Velocidad"),
                                        text="Cambiar Mbps",
                                        width=150,
                                        command=cambio)
    

    dhcpButton = CTkButton(master=panel,
                                        text="DCHP List",
                                        width=150,
                                        command=dchpDat,
                                        corner_radius=0)
    
    queuesButton = CTkButton(master=panel,
                             text="QUEUES List",
                             width=150,
                             command=queues,
                             corner_radius=0)
    
    mensageLabwl = CTkLabel(master=menuTab.tab("Corte Por Tiempo"), text="Esta opcion solo se encuentra disponible en la version Servidor")
    mensageFecha = CTkLabel(master=menuTab.tab("Corte por Fecha"), text="Esta opcion solo se encuentra disponible en la version Servidor")



    
    hostLabel.place(relx=0.1,
                    rely=0.1)
    hostEntry.place(relx=0.2,
                    rely=0.1)

    usuarioLabel.place(relx=0.4,
                       rely=0.1)
    usuarioEntry.place(relx=0.5,
                       rely=0.1)
    
    passwordLabel.place(relx=0.7,
                        rely=0.1)
    passwordEntry.place(relx=0.8,
                        rely=0.1)
    
    ipLabel.place(relx=0.1,
                  rely=0.1)
    ipEntry.place(relx=0.2,
                  rely=0.1)

    limitLabel.place(relx=0.5,
                     rely=0.1)
    limitOpcions.place(relx=0.6,
                       rely=0.1)

    freeLabel.place(relx=0.1,
                    rely=0.2)
    freeOpcions.place(relx=0.2,
                      rely=0.2)
    bloquearButton.place(relx=0.2,
                         rely=0.3)
    desbloquearButton.place(relx=0.6,
                            rely=0.3)
    

    ipClienteLB.place(relx=0.1,
                  rely=0.1)
    ipClienteEntry.place(relx=0.2,
                  rely=0.1)

    limiteLB.place(relx=0.5,
                     rely=0.1)
    limiteOp.place(relx=0.6,
                       rely=0.1)


    cambioButton.place(relx=0.2,
                         rely=0.3)
    dhcpButton.place(relx = 0.0,
                     rely = 0.1)
    queuesButton.place(relx=0.0,
                       rely=0.2)
    
    mensageLabwl.pack()
    mensageFecha.pack()
    
    menuTab.place(relx=0.2,
                  rely=0.1,
                  )

    banner.place(relx=0.0,
            rely=0.0,
            relwidth=1.0,
            relheight=0.1)
    
    panel.place(relx=0.0,
            rely=0.0,
            relwidth=0.1,
            relheight=1.0)
    app.mainloop()


def comandoCorte(hostname, username, password, client_ip, limit):

        port = 22


        # Comando para ajustar la velocidad del queue a 1k/1k para la IP del cliente
        command = f"/queue simple set [find target={client_ip}/32] max-limit={limit}"

        # Crear un cliente SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
                # Conectarse al dispositivo MikroTik
                ssh.connect(hostname, port, username, password)

                # Ejecutar el comando
                stdin, stdout, stderr = ssh.exec_command(command)

                # Leer la salida y los errores (si hay)
                output = stdout.read().decode()
                error = stderr.read().decode()

                if output:
                        print("Output:")
                        print(output)

                if error:
                        print("Error:")
                        print(error)

        finally:
        # Cerrar la conexión SSH
         ssh.close()
file:///home/ricardo/Documents/RatonServer/main.py

def dhcpEnvio(hostname, username, password):
    return {
        'hostname': hostname,
        'username': username,
        'password': password
    }

def obtener_leases(username, password, host):
    api = connect(username=username, password=password, host=host)
    leases = api('/ip/dhcp-server/lease/print')

    # Crear una ventana Toplevel
    top = tk.Toplevel()
    top.title("DHCP Leases")

    # Crear un Treeview para mostrar las leases
    tree = ttk.Treeview(top, columns=('IP Address', 'Active Hostname'), show='headings')
    tree.heading('IP Address', text='IP Address')
    tree.heading('Active Hostname', text='Active Hostname')
    tree.pack(fill=tk.BOTH, expand=True)

    # Añadir las leases al Treeview
    for lease in leases:
        address = lease.get('address')
        hostname = lease.get('host-name')
        if address and hostname:
            tree.insert('', 'end', values=(address, hostname))

    # Iniciar el loop de la ventana Toplevel
    top.mainloop()


def obtener_queues(username, password, host):
    """Función para obtener las colas del MikroTik"""
    api = connect(username=username, password=password, host=host)
    queues = api('/queue/simple/print')
    return queues

file:///home/ricardo/Documents/RatonServer/main.py

def mostrar_queues(username, password, host):
    """Función para mostrar las colas en una ventana toplevel"""
    queues = obtener_queues(username, password, host)
    
    # Crear la ventana toplevel
    toplevel = tk.Toplevel()
    toplevel.title("MikroTik Queues")
    
    # Crear un Treeview para mostrar las colas
    tree = ttk.Treeview(toplevel, columns=('Name', 'Target', 'Upload Max Limit', 'Download Max Limit'), show='headings')
    tree.heading('Name', text='Name')
    tree.heading('Target', text='Target')
    tree.heading('Upload Max Limit', text='Upload Max Limit')
    tree.heading('Download Max Limit', text='Download Max Limit')
    tree.pack(fill=tk.BOTH, expand=True)
    
    # Añadir las colas al Treeview
    for queue in queues:
        name = queue.get('name')
        target = queue.get('target')
        max_limit = queue.get('max-limit', '0/0').split('/')
        upload_max_limit = max_limit[0]
        download_max_limit = max_limit[1]
        if name and target:
            tree.insert('', 'end', values=(name, target, upload_max_limit, download_max_limit))
