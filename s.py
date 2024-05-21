from tkinter import Menu, ttk, Tk, Toplevel
from customtkinter import CTk
import mysql.connector
import tkinter as tk
from customtkinter import *
import customtkinter as ctk
from tkinter import Toplevel, Menu
from tkinter import *
from tkinter import messagebox as MessageBox
from tkcalendar import DateEntry

app = CTk()
app.title("Wisplus Desktop")
app.geometry("1200x700")

#frame = ctk.CTkFrame(master=app, fg_color="#0080E4", border_color="#005FA9", border_width=2)
#Podemos definir entre light o dark segun el tema
set_appearance_mode("light")



#======================================FUNCIONES============================================#
def buscarCliente():
    nombre = buscarEntry.get()

        # Conexión a la base de datos
    conexion = conectar_db()
        
    if conexion.is_connected():
            cursor = conexion.cursor()
            # Consulta SQL para buscar cliente
            sql_search_query = "SELECT * FROM clientes WHERE nombre LIKE %s"
            cursor.execute(sql_search_query, ('%' + nombre + '%',))
            cliente = cursor.fetchone()
            
            if cliente:
                # Mostrar los datos del cliente en el formulario
                dnaEntry.delete(0, 'end')
                nombreEntry.delete(0, 'end')
                direccionEntry.delete(0, 'end')
                telefononEntry.delete(0, 'end')
                comentarioEntry.delete("1.0", "end")
                ipEntry.delete(0, 'end')

                dnaEntry.insert(0, cliente[0])
                nombreEntry.insert(0, cliente[1])
                direccionEntry.insert(0, cliente[2])
                telefononEntry.insert(0, cliente[3])
                fechaInstalacionEntry.set_date(cliente[4])
                equiposEntry.set(cliente[5])
                mensualidadEntry.set(cliente[6])
                localidadEntry.set(cliente[7])
                comentarioEntry.insert("1.0", cliente[8])
                paqueteEntry.set(cliente[9])
                ipEntry.insert(0, cliente[10])

                buscarResult.set(f"Cliente encontrado: {cliente[1]}")
            else:
                buscarResult.set("Cliente no encontrado")
                cursor.close()
                conexion.close()

# Función para actualizar los datos del cliente en la base de datos
def actualizarCliente():
    no_cliente = dnaEntry.get()
    nombre = nombreEntry.get()
    direccion = direccionEntry.get()
    telefono = telefononEntry.get()
    fechaInstalacion = fechaInstalacionEntry.get_date()
    equipos = equiposEntry.get()
    mensualidad = mensualidadEntry.get()
    localidad = localidadEntry.get()
    comentarios = comentarioEntry.get("1.0", "end-1c")
    paquete = paqueteEntry.get()
    ip = ipEntry.get()
    
    try:
        # Conexión a la base de datos
        conexion = conectar_db()

        if conexion.is_connected():
            cursor = conexion.cursor()

            # Consulta SQL para actualizar datos
            sql_update_query = """ 
            UPDATE clientes 
            SET nombre = %s, direccion = %s, telefono = %s, fechaInstalacion = %s, equipos = %s, 
                mensualidad = %s, localidad = %s, comentarios = %s, paquete = %s, ip = %s 
            WHERE no_cliente = %s """
            datos = (nombre, direccion, telefono, fechaInstalacion, equipos, mensualidad, localidad, comentarios, paquete, ip, no_cliente)

            # Ejecutar la consulta
            cursor.execute(sql_update_query, datos)

            # Confirmar la transacción
            conexion.commit()

            MessageBox.showinfo("Correcto", f"Se actualizaron los datos del cliente: {nombre}")

            if conexion.is_connected():
                cursor.close()
                conexion.close()
                print("Conexión a MySQL cerrada")

    except mysql.connector.Error as e:
        MessageBox.showinfo("Error", f"No se pudo actualizar el cliente: {e}")

# Función para mostrar los clientes en un Treeview
def verClientes():
    verClientesWindow = Toplevel(app)
    verClientesWindow.title("Ver Clientes")
    verClientesWindow.geometry("1000x600")
    
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT no_cliente, nombre, direccion, telefono, fechaInstalacion, equipos,
                   mensualidad, localidad, paquete, ip
            FROM clientes
        """)
        rows = cursor.fetchall()

        columns = ("No. Cliente", "Nombre", "Dirección", "Teléfono", "Fecha Instalación", "Equipos",
                   "Mensualidad", "Localidad", "Paquete", "IP")

        tree = ttk.Treeview(verClientesWindow, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)

        for row in rows:
            tree.insert("", "end", values=row)

        tree.pack(expand=True, fill='both')

        conn.close()

    except mysql.connector.Error as e:
       MessageBox.showinfo("Error", f"Error al recuperar datos: {e}")

# Widgets de la aplicación
buscarLabel = ctk.CTkLabel(master=app, text="Buscar Cliente por Nombre")
buscarEntry = ctk.CTkEntry(master=app,
                           placeholder_text="Nombre del cliente",
                           height=10,
                           width=160,
                           font=("Helvetica", 12))
buscarButton = ctk.CTkButton(master=app, text="Buscar",
                             border_width=2,
                             command=buscarCliente)


buscarResult = ctk.StringVar()
buscarResultLabel = ctk.CTkLabel(master=app, textvariable=buscarResult)

dnaLabel = ctk.CTkLabel(master=app, text="DNA Cliente")
dnaEntry = ctk.CTkEntry(master=app, 
                        placeholder_text="Ejemplo 23",
                        height=10,
                        width=160,
                        font=("Helvetica", 12))

nameLabel = ctk.CTkLabel(master=app, text="Ingresa el nombre")
nombreEntry = ctk.CTkEntry(master=app,
                           placeholder_text="Ricardo Escobedo",
                           height=10,
                           width=160,
                           font=("Helvetica", 12))

direccionLabel = ctk.CTkLabel(master=app, text="Dirección")
direccionEntry = ctk.CTkEntry(master=app,
                              placeholder_text="Joaquin Amaro",
                              height=10,
                              width=160,
                              font=("Helvetica", 12))

telefonoLabel = ctk.CTkLabel(master=app, text="Teléfono")
telefononEntry = ctk.CTkEntry(master=app,
                              placeholder_text="4981442266",
                              height=10,
                              width=160,
                              font=("Helvetica", 12))

fechaInstalacionLabel = ctk.CTkLabel(master=app, text="Fecha de Instalación")
fechaInstalacionEntry = DateEntry

def registrarCliente():
    no_cliente =dnaEntry.get()
    nombre = nombreEntry.get()
    direccion = direccionEntry.get()
    telefono = telefononEntry.get()
    fechaInstalacion = fechaInstalacionEntry.get()
    equipos = equiposEntry.get()
    mensualidad = mensualidadEntry.get()
    localidad = localidadEntry.get()
    comentarios = comentarioEntry.get("1.0", "end-1c")
    paquete = paqueteEntry.get()
    ip = ipEntry.get()
    insertar_datos(no_cliente, nombre, direccion, telefono, fechaInstalacion, equipos, mensualidad, localidad, comentarios, paquete, ip)

def insertar_datos(no_cliente, nombre, direccion, telefono, fechaInstalacion, equipos, mensualidad, localidad, comentarios, paquete, ip):
            # Conexión a la base de datos
            conexion =  conectar_db()

            if conexion.is_connected():
                cursor = conexion.cursor()

                # Consulta SQL para insertar datos
                sql_insert_query = """ INSERT INTO clientes (no_cliente,
                                                nombre, direccion, telefono,
                                                fechaInstalacion, equipos, mensualidad,
                                                localidad, comentarios, paquete, ip)

                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
                datos = (no_cliente, nombre, direccion, telefono, fechaInstalacion, equipos, mensualidad, localidad, comentarios, paquete, ip)

                # Ejecutar la consulta
                cursor.execute(sql_insert_query, datos)

                # Confirmar la transacción
                conexion.commit()

                MessageBox.showinfo("Correcto", "Se guardo de manera correcta tu cliente: " + nombre)

                if conexion.is_connected():
                    cursor.close()
                    conexion.close()
                    print("Conexión a MySQL cerrada")

def salir():
    resultado = MessageBox.askquestion("Salir", "Estas seguro que deseas salir?")
    if  resultado == "yes":
        app.destroy()

def conectar_db():
    return mysql.connector.connect(
        host="122.122.124.8",
        user="dni",
        password="MinuzaFea265/",
        database="doblenet"
    )

def verClientes():
    verClientesWindow = Toplevel(app)
    verClientesWindow.title("Ver Clientes")
    verClientesWindow.geometry("1000x600")
    
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT no_cliente, nombre, direccion, telefono, fechaInstalacion, equipos,
               mensualidad, localidad, paquete, ip
        FROM clientes
    """)
    rows = cursor.fetchall()

    columns = ("no_cliente", "nombre", "direccion", "telefono", "fechaInstalacion", "equipos",
               "mensualidad", "localidad", "paquete", "ip")

    tree = ttk.Treeview(verClientesWindow, columns=columns, show='headings')
    tree.heading("no_cliente", text="No. Cliente")
    tree.heading("nombre", text="Nombre")
    tree.heading("direccion", text="Dirección")
    tree.heading("telefono", text="Teléfono")
    tree.heading("fechaInstalacion", text="Fecha Instalación")
    tree.heading("equipos", text="Equipos")
    tree.heading("mensualidad", text="Mensualidad")
    tree.heading("localidad", text="Localidad")
    tree.heading("paquete", text="Paquete")
    tree.heading("ip", text="IP")

    for row in rows:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill='both')

    conn.close()

    # Crear el menú contextual
    def popup(event):
        menu.post(event.x_root, event.y_root)

    menu = Menu(tree, tearoff=0)
    menu.add_command(label="Editar", command=editar_cliente)
    menu.add_command(label="Eliminar", command=eliminar_cliente)
    menu.add_command(label="Pagar", command=eliminar_cliente)

    
    tree.bind("<Button-3>", popup)

def servidorMysql():
    servidorMysqlWindow = Toplevel(app)
    servidorMysqlWindow.title("Ver Clientes")
    servidorMysqlWindow.geometry("1000x600")

def editar_cliente():
    print("Editar cliente seleccionado")

def eliminar_cliente():
    print("Eliminar cliente seleccionado")

def modificarCliente():
    pass

def historialCliente():
    pass

def verHistorial():
    pass

def registrarPago():
    pass

def generarComprobante():
    pass

def confirmacionPago():
    pass

def modDark():
    set_appearance_mode("dark")

def modLight():
    set_appearance_mode("light")


#======================================FUNCIONES============================================#









#======================================WIDGETS DE INICIO============================================#
dnaLabel = ctk.CTkLabel(master=app, text="DNA Cliente")
dnaEntry = ctk.CTkEntry(master=app, 
                            placeholder_text="Ejemplo 23",
                            height=10,
                            width=160,
                            font=("Helvetica", 12))



nameLabel = ctk.CTkLabel(master=app, text="Ingresa el nombre")
nombreEntry = ctk.CTkEntry(master=app,
                           placeholder_text="Ricardo Escobedo",
                           height=10,
                           width=160,
                           font=("Helvetica", 12))

direccionLabel = ctk.CTkLabel(master=app, text="Direccion")
direccionEntry = ctk.CTkEntry(master=app,
                           placeholder_text="Joaquin Amaro",
                           height=10,
                           width=160,
                           font=("Helvetica", 12))

telefonoLabel = ctk.CTkLabel(master=app, text="Telefono")
telefononEntry = ctk.CTkEntry(master=app,
                           placeholder_text="4981442266",
                           height=10,
                           width=160,
                           font=("Helvetica", 12))


fechaInstalacionLabel = ctk.CTkLabel(master=app, text="Fecha de Instalacion")
fechaInstalacionEntry = DateEntry(master=app,
                                  date_pattern='y-mm-dd')

equiposLabel = ctk.CTkLabel(master=app, text="Equpos Instalados")
equiposEntry = ctk.CTkComboBox(master=app,
                               values=["Router 840N y Antena M5",
                                       "ONT (Terminal de Red Optica)",
                                       "Mercusys y M5",
                                       "Router TpLink y M5AC"]
                               )

mensualidadLabel = ctk.CTkLabel(master=app, text="Mensualidad")
mensualidadEntry = ctk.CTkComboBox(master=app,
                                   values=[
                                       "250",
                                       "300",
                                       "350",
                                       "400"
                                   ])

localidadLabel = ctk.CTkLabel(master=app, text="Localidad")
localidadEntry = ctk.CTkComboBox(master=app,
                               values=["Loreto",
                                       "Tierra Blanca",
                                       "El Rascon",
                                       "Las Playas",
                                       "Las huertas"])

comentarioLabel = ctk.CTkLabel(master=app, text="Comentario")
comentarioEntry = ctk.CTkTextbox(master=app, width=350,
                                 height=150,
                                 font=("Consolas",12)
                                 )

paqueteLabel = ctk.CTkLabel(master=app, text="Paquete")
paqueteEntry = ctk.CTkComboBox(master=app,
                               values=["100M/7M",
                                       "100M/15M",
                                       "100M/20M",
                                       "100M/30M"])

ipLabel = ctk.CTkLabel(master=app, text="Direccion Ip")
ipEntry = ctk.CTkEntry(master=app,
                           placeholder_text="192.168.0.3",
                           height=10,
                           width=160,
                           font=("Helvetica", 12))
#======================================WIDGETS DE INICIO============================================#


#======================================CONFIGURACION DE BOTON============================================#
btn = ctk.CTkButton(master=app, text="Agregar",
                    border_width=2,
                    command=registrarCliente)

btnSalir = ctk.CTkButton(master=app, text="Salir",
                    border_width=2,
                    command=salir)
#======================================CONFIGURACION DE BOTON============================================#

















#======================================MENU=============================================#
menu_bar = Menu(app)

# Opciones en el menu Usuario
usuario_menu = Menu(menu_bar, tearoff=0)
#usuario_menu.add_command(label="Registrar Cliente", command=registrarCliente)
usuario_menu.add_command(label="Ver Clientes", command=verClientes)
usuario_menu.add_command(label="Modificar Cliente", command=modificarCliente)

#Definimos las opciones de historial
historial_menu = Menu(menu_bar, tearoff=0)
historial_menu.add_command(label="Historial de Cliente", command=historialCliente)
historial_menu.add_command(label="Historial General", command=verHistorial)

#Definimos las opciones de Pagos
pago_menu = Menu(menu_bar, tearoff=0)
pago_menu.add_command(label="Registrar Pago", command=registrarPago)
pago_menu.add_command(label="Generar Comprobante", command=generarComprobante)
pago_menu.add_command(label="Confirmacion de Pago", command=confirmacionPago)

#Definimos las opciones de herramientas
herramientas_menu = Menu(menu_bar, tearoff=0)
herramientas_menu.add_command(label="Herramientas M5 Ubiquiti", command=registrarPago)
herramientas_menu.add_command(label="Microtik Basic", command=generarComprobante)
herramientas_menu.add_command(label="Network", command=confirmacionPago)

#Definimos las opciones de configuracion
configuracion_menu = Menu(menu_bar, tearoff=0)
configuracion_menu.add_command(label="Agregar Servidor MySQL", command=modLight)
configuracion_menu.add_command(label="Modo Dark", command=modDark)
configuracion_menu.add_command(label="Modo Light", command=modLight)




#Menu para salir
salir_menu = Menu(menu_bar, tearoff=0)
salir_menu.add_command(label="Salir", command=salir)


# Integra el menu usuario en la ventana
menu_bar.add_cascade(label="Usuario", menu=usuario_menu)
menu_bar.add_cascade(label="Historial", menu=historial_menu)
menu_bar.add_cascade(label="Pagos", menu=pago_menu)
menu_bar.add_cascade(label="Herramientas", menu=herramientas_menu)
menu_bar.add_cascade(label="Configuracion", menu=configuracion_menu)
menu_bar.add_cascade(label="Salir", menu=salir_menu)

app.config(menu=menu_bar)
#==========================================MENU============================================#


#====================================POSICIONES DE ELEMENTOS MAIN=====================================#
dnaLabel.place(relx=0.1, #El eje x es izqueirda y derecha
               rely=0.1,
               anchor="center")
dnaEntry.place(relx=0.3,
               rely=0.1,
               anchor="center")

nameLabel.place(relx=0.5,
                rely=0.1,
                anchor="center")
nombreEntry.place(relx=0.7,
                rely=0.1,
                anchor="center")

direccionLabel.place(relx=0.1,
                rely=0.2,
                anchor="center")
direccionEntry.place(relx=0.3,
                rely=0.2,
                anchor="center")

telefonoLabel.place(relx=0.5,
                rely=0.2,
                anchor="center")
telefononEntry.place(relx=0.7,
                rely=0.2,
                anchor="center")

fechaInstalacionLabel.place(relx=0.1,
                rely=0.3,
                anchor="center")
fechaInstalacionEntry.place(relx=0.3,
                rely=0.3,
                anchor="center")

equiposLabel.place(relx=0.5,
                rely=0.3,
                anchor="center")
equiposEntry.place(relx=0.7,
                rely=0.3,
                anchor="center")

mensualidadLabel.place(relx=0.1,
                       rely=0.4,
                       anchor="center")
mensualidadEntry.place(relx=0.3,
                       rely=0.4,
                       anchor="center")

localidadLabel.place(relx=0.5,
                       rely=0.4,
                       anchor="center")
localidadEntry.place(relx=0.7,
                       rely=0.4,
                       anchor="center")

comentarioLabel.place(relx=0.1,
                       rely=0.7,
                       anchor="center")

comentarioEntry.place(relx=0.4,
                       rely=0.7,
                       anchor="center")

paqueteLabel.place(relx=0.5,
                       rely=0.5,
                       anchor="center")
paqueteEntry.place(relx=0.7,
                       rely=0.5,
                       anchor="center")

ipLabel.place(relx=0.1,
                       rely=0.5,
                       anchor="center")
ipEntry.place(relx=0.3,
                       rely=0.5,
                       anchor="center")
#===================================BOTONES===========================================#
btn.place(relx=0.7,
                       rely=0.7,
                       anchor="center")

btnSalir.place(relx=0.7,
                       rely=0.8,
                       anchor="center")

buscarEntry.place(relx=0.9,
                  rely=0.6,
                  anchor="center")

buscarButton.place(relx=0.9,
                   rely=0.7,
                   anchor="center")
#===================================BOTONES===========================================#

#=====================================FRAMES==========================================#

#=====================================FRAMES==========================================#

#====================================POSICIONES DE ELEMENTOS MAIN=====================================#

app.mainloop()
