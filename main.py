from customtkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox as MessageBox
from tkinter import Toplevel, Menu
from tkinter import Menu, ttk, Tk, Toplevel
from plyer import notification
from tkcalendar import DateEntry

#============================================= FRAMES Y CONFIG ===================================================#
app = CTk()
app.title("Raton App")
app.geometry("1200x780")
app.resizable(False, False)
set_appearance_mode("light")

#Imagen de actualizacion
procesoCompletoIcon = "icons/process-completed.ico"
advertenciaIcon = "icons/dialog-warning.ico"

ipIcono = Image.open("icons/testConexxion.png")
ipIconoPhoto = ImageTk.PhotoImage(ipIcono)


usuarioIcono = Image.open("icons/crearUsuario.png")
usuarioIconoPhoto = ImageTk.PhotoImage(usuarioIcono)

verUsuarioIcono = Image.open("icons/verClientes.png")
verUsuarioIconoPhoto = ImageTk.PhotoImage(verUsuarioIcono)


actualizarUsuarioIcono = Image.open("icons/actualizarUsuario.png")
actualizarUsuarioIconoPhoto = ImageTk.PhotoImage(actualizarUsuarioIcono)

crearPagosIcono = Image.open("icons/crearPago.png")
crearPagosIconoPhoto = ImageTk.PhotoImage(crearPagosIcono)

verPagosIcono = Image.open("icons/verPagos.png")
verPagosIconoPhoto = ImageTk.PhotoImage(verPagosIcono)

eliminarIcono = Image.open("icons/eliminarCliente.png")
eliminarIconoPhoto = ImageTk.PhotoImage(eliminarIcono)

salirIcono = Image.open("icons/salir.png")
salirIconoPhoto = ImageTk.PhotoImage(salirIcono)


elementary = Image.open("icons/distributor-logo.png")
elementaryPhoto = ImageTk.PhotoImage(elementary)

panel = CTkFrame(master=app, fg_color="#839192", border_color="#4D5656", border_width=0, corner_radius=0)
banner = CTkFrame(master=app, fg_color="#839192", border_color="#4D5656", border_width=0, corner_radius=0)
centro = CTkFrame(master=app, fg_color="#ABB2B9", border_color="#4D5656", border_width=1, corner_radius=0)
#============================================= FRAMES Y CONFIG ===================================================#










#============================================= FUNCIONES ===================================================#
def testConexion():
    """ Conectar a la base de datos MySQL """
    try:
        connection = mysql.connector.connect(
            host=ipEntry.get(),
            database='doblenet',
            user=UserEntry.get(),
            password=PasswordEntry.get()
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado a MySQL Server versión {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            MessageBox.showinfo("Conetado", f"Conexion establecida a: {record}")

    except Error as e:


        MessageBox.showerror("No Conectar", f"Error al conectar a MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

       
def salir():
    resultado = MessageBox.askquestion("Salir", "Estas seguro que deseas salir?")
    if  resultado == "yes":
        app.destroy()

# Función para conectar a la base de datos MySQL
def conectar_db():
    return mysql.connector.connect(
        host=ipEntry.get(),
        user=UserEntry.get(),
        password=PasswordEntry.get(),
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

def registrarCliente():
    no_cliente =dnaEntry.get()
    nombre = nameEntry.get()
    direccion = direccionEntry.get()
    telefono = telefonoEntry.get()
    fechaInstalacion = fechaEntry.get()
    equipos = equiposEntry.get()
    mensualidad = mensualidadEntry.get()
    localidad = localidadEntry.get()
    comentarios = comentarioEntry.get("1.0", "end-1c")
    paquete = paquetedEntry.get()
    ip = ipClienteEntry.get()
    insertar_datos(no_cliente, nombre, direccion, telefono, fechaInstalacion, equipos, mensualidad, localidad, comentarios, paquete, ip)

def insertar_datos(no_cliente, nombre, direccion, telefono, fechaInstalacion, equipos, mensualidad, localidad, comentarios, paquete, ip):
            # Conexión a la base de datos
            conexion =  conectar_db()

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

                MessageBox.showinfo("Correcto", "Se guardo de manera correcta tu cliente: " + nombre)

                if conexion.is_connected():
                    cursor.close()
                    conexion.close()
                    print("Conexión a MySQL cerrada")

def insertar_pago(no_cliente, nombre, fecha, monto, no_recibo):
            # Conexión a la base de datos
            conexion =  conectar_db()

            if conexion.is_connected():
                cursor = conexion.cursor()

                # Consulta SQL para insertar datos
                sql_insert_query = """ INSERT INTO pagos (no_cliente, nombre, fecha,
                                                            monto, no_recibo)
                                    VALUES (%s, %s, %s, %s, %s) """
                datos = (no_cliente, nombre, fecha, monto, no_recibo)

                # Ejecutar la consulta
                cursor.execute(sql_insert_query, datos)

                # Confirmar la transacción
                conexion.commit()


                if conexion.is_connected():
                    cursor.close()
                    conexion.close()
                    print("Conexión a MySQL cerrada")

def crearPago():
    toplevel_window = CTkToplevel(app)
    toplevel_window.geometry("1000x500")
    toplevel_window.title("Registrar Pago")
    toplevel_window.resizable(False, False)

    panel2 = CTkFrame(master=toplevel_window, fg_color="#839192", border_color="#4D5656", border_width=0, corner_radius=0)
    
    def confirmacion():
         resultado = MessageBox.askquestion("Confirmar", "Estas segurdo de registrar?")
         if resultado == "yes":
              envioDatos()


    def salir1():
         toplevel_window.destroy()

    def envioDatos():
         no_cliente = dnaEntry.get()
         nombre = nameEntry.get()
         fecha = fechaEntry.get()
         monto = montoEntry.get()
         no_recibo = noReciboEntry.get()

         insertar_pago(no_cliente, nombre, fecha, monto, no_recibo)

    dnaLabel = CTkLabel(master=toplevel_window,
                    text="DNA del Cliente",
                    text_color="#000000",
                    )
    dnaEntry = CTkEntry(master=toplevel_window,
                    placeholder_text="12325",
                    height=30,
                    width=100,
                    font=("Helvetica", 12))

    nameLabel = CTkLabel(master=toplevel_window,
                        text="Nombre",
                        text_color="#000000")
    nameEntry = CTkEntry(master=toplevel_window,
                        placeholder_text="Clielia Escobedo",
                        height=30,
                        width=150,
                        font=("Helvetica", 12))

    fechaLabel = CTkLabel(master=toplevel_window,
                          text="Fecha Ins")
    fechaEntry = DateEntry(master=toplevel_window,
                                    date_pattern='y-mm-dd')
    

    montoLabel = CTkLabel(master=toplevel_window,
                          text="Pago $")
    montoEntry = CTkComboBox(master=toplevel_window,
                                values=["250",
                                        "300",
                                        "350",
                                        "375"]
                                )
    noReciboLbel = CTkLabel(master=toplevel_window,
                            text="No Recibo")
    noReciboEntry = CTkEntry(master=toplevel_window,
                        placeholder_text="REC009",
                        height=30,
                        width=150)
    
    guardarPagoButton = CTkButton(master=panel2,
                        text="Crear Pago",
                        image=CTkImage(dark_image=crearPagosIcono,
                                        light_image=crearPagosIcono),
                                        command=confirmacion
                                        )

    verPagosButton1 = CTkButton(master=panel2,
                        text="Ver Pagos",
                        image=CTkImage(dark_image=verPagosIcono,
                                        light_image=verPagosIcono),
                                        ) 
      
    salirButton1 = CTkButton(master=panel2,
                        text="Salir",
                        image=CTkImage(dark_image=salirIcono,
                                        light_image=salirIcono),
                                        command=salir1)
    



    guardarPagoButton.place(relx=0.2,
                            rely=0.1
                            )
    verPagosButton1.place(relx=0.2,
                          rely=0.2)
    salirButton1.place(relx=0.2,
                       rely=0.9)
    
    dnaLabel.place(relx=0.4,
                   rely=0.1)
    dnaEntry.place(relx=0.5,
                   rely=0.1)

    nameLabel.place(relx=0.7,
                    rely=0.1)
    nameEntry.place(relx=0.8,
                    rely=0.1)
    
    fechaLabel.place(relx=0.4,
                     rely=0.2)
    fechaEntry.place(relx=0.5,
                     rely=0.2)

    montoLabel.place(relx=0.7,
                     rely=0.2)
    montoEntry.place(relx=0.8,
                     rely=0.2)
    
    noReciboLbel.place(relx=0.4,
                       rely=0.3)
    noReciboEntry.place(relx=0.5,
                        rely=0.3)
    
    panel2.place(relx=0.0,
                rely=0.0,
                relwidth=0.3,
                relheight=1.0)

def verPagos():
    verPagosWindow = Toplevel(app)
    verPagosWindow.title("Ver Clientes")
    verPagosWindow.geometry("1000x600")
    
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT no_cliente, nombre, fecha, monto, no_recibo
        FROM pagos
    """)
    rows = cursor.fetchall()

    columns = ("no_cliente", "nombre", "fecha", "monto", "no_recibo")

    tree = ttk.Treeview(verPagosWindow, columns=columns, show='headings')
    tree.heading("no_cliente", text="No. Cliente")
    tree.heading("nombre", text="Nombre")
    tree.heading("fecha", text="Fecha")
    tree.heading("monto", text="Pago $")
    tree.heading("no_recibo", text="Recibo")

    for row in rows:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill='both')

    conn.close()


def web():
     MessageBox.showinfo("Proximamente", "Estas opciones solo estan disponibles en la web")

#============================================= FUNCIONES ===================================================#



#=============================================== BOTONES =====================================================#
ipButton = CTkButton(master=panel,
                     text="Test Conexion",
                     image=CTkImage(dark_image=ipIcono,
                                    light_image=ipIcono),
                                    command=testConexion,
                                    fg_color="transparent",
                                    border_color="#F4F6F7",
                                    border_width=2,
                                    border_spacing=0
                                    )

salirButton = CTkButton(master=panel,
                     text="Salir",
                     image=CTkImage(dark_image=salirIcono,
                                    light_image=salirIcono),
                                    command=salir)

registrarButton = CTkButton(master=panel,
                     text="Crear Cliente",
                     image=CTkImage(dark_image=usuarioIcono,
                                    light_image=usuarioIcono),
                                    command=registrarCliente)


verClientesButton = CTkButton(master=panel,
                     text="Ver Clientes",
                     image=CTkImage(dark_image=verUsuarioIcono,
                                    light_image=verUsuarioIcono),
                                    command=verClientes)

actualizarClientesButton = CTkButton(master=panel,
                     text="Actualizar Clientes",
                     image=CTkImage(dark_image=actualizarUsuarioIcono,
                                    light_image=actualizarUsuarioIcono),
                                    command=web)

eliminarsButton = CTkButton(master=panel,
                     text="Eliminar Cliente",
                     image=CTkImage(dark_image=eliminarIcono,
                                    light_image=eliminarIcono),
                                    command=web)

crearPagosButton = CTkButton(master=panel,
                     text="Crear Pago",
                     image=CTkImage(dark_image=crearPagosIcono,
                                    light_image=crearPagosIcono),
                                    command=crearPago)


verPagosButton = CTkButton(master=panel,
                     text="Ver Pago",
                     image=CTkImage(dark_image=verPagosIcono,
                                    light_image=verPagosIcono),
                                    command=verPagos)



#=============================================== BOTONES =====================================================#






#============================================= WIDGETS =====================================================#

ipLabel = CTkLabel(master=banner,
                   text="IP Servidor SQL")
ipEntry = CTkEntry(master=banner,
                   placeholder_text="122.122.124.8",
                   height=30,
                   width=160,
                   font=("Helvetica", 12))

UserLabel = CTkLabel(master=banner,
                     text="Usuario")
UserEntry = CTkEntry(master=banner,
                   placeholder_text="admin",
                   height=30,
                   width=160,
                   font=("Helvetica", 12))

PasswordLabel = CTkLabel(master=banner,
                     text="Clave")
PasswordEntry = CTkEntry(master=banner,
                   placeholder_text="*****",
                   height=30,
                   width=160,
                   font=("Helvetica", 12),
                   show="*")

databaseLabel = CTkLabel(master=banner,
                     text="Database")
databaseLabel = CTkEntry(master=banner,
                   placeholder_text="admin",
                   height=30,
                   width=160,
                   font=("Helvetica", 12))


#============================================BANNER CENTRO+++++++++++++++++++++++++++++++++#

dnaLabel = CTkLabel(master=centro,
                   text="DNA del Cliente",
                   text_color="#000000",
                   )
dnaEntry = CTkEntry(master=centro,
                   placeholder_text="12325",
                   height=30,
                   width=100,
                   font=("Helvetica", 12))

nameLabel = CTkLabel(master=centro,
                     text="Nombre del CLiente",
                     text_color="#000000")
nameEntry = CTkEntry(master=centro,
                     placeholder_text="Clielia Escobedo",
                     height=30,
                     width=150,
                     font=("Helvetica", 12))

direccionLabel = CTkLabel(master=centro,
                     text="Direccion",
                     text_color="#000000")
direccionEntry = CTkEntry(master=centro,
                     placeholder_text="San Mateo #12",
                     height=30,
                     width=100,
                     font=("Helvetica", 12))


telefonoLabel = CTkLabel(master=centro,
                     text="No Celular",
                     text_color="#000000")
telefonoEntry = CTkEntry(master=centro,
                     placeholder_text="000-000-000-0",
                     height=30,
                     width=150,
                     font=("Helvetica", 12))


fechaLabel = CTkLabel(master=centro, text="Fecha Ins")
fechaEntry = DateEntry(master=centro,
                                  date_pattern='y-mm-dd')


equiposLabel = CTkLabel(master=centro, text="Equpos Instalados")
equiposEntry = CTkComboBox(master=centro,
                               values=["Router 840N y Antena M5",
                                       "ONT (Terminal de Red Optica)",
                                       "Mercusys y M5",
                                       "Router TpLink y M5AC"]
                               )

paqueteLabel = CTkLabel(master=centro, text="Paquete")
paquetedEntry = CTkComboBox(master=centro,
                               values=["100M/7M",
                                       "100M/15M",
                                       "100M/20M",
                                       "100M/30"]
                               )

mensualidadLabel = CTkLabel(master=centro, text="Mensualidad")
mensualidadEntry = CTkComboBox(master=centro,
                               values=["250",
                                       "300",
                                       "350",
                                       "375"]
                               )

localidadLabel = CTkLabel(master=centro, text="Localidad")
localidadEntry = CTkComboBox(master=centro,
                               values=["Loreto",
                                       "Las Playas",
                                       "Tierra Blanca",
                                       "China"]
                               )




comentarioLabel = CTkLabel(master=centro, text="Comentario")
comentarioEntry = CTkTextbox(master=centro,
                             width=500,
                                 height=150,
                                 font=("Consolas",12)
                                 )

ipClienteLabel = ctk.CTkLabel(master=centro, text="Direccion Ip")
ipClienteEntry = ctk.CTkEntry(master=centro,
                           placeholder_text="192.168.0.3",
                           height=30,
                           width=150,
                           font=("Helvetica", 12))


#============================================BANNER CENTRO+++++++++++++++++++++++++++++++++#


#============================================= WIDGETS =====================================================#











#============================================= CONFIG DE WIDGETS===================================================#

ipLabel.place(relx=0.1,
              rely=0.1)
ipEntry.place(relx=0.2,
              rely=0.1,
              )

UserLabel.place(relx=0.4,
                rely=0.1)
UserEntry.place(relx=0.5,
              rely=0.1,
              )

PasswordLabel.place(relx=0.7,
                rely=0.1)
PasswordEntry.place(relx=0.8,
              rely=0.1,
              )




ipButton.place(relx=0.2,
               rely=0.8)

salirButton.place(relx=0.2,
               rely=0.9)

registrarButton.place(relx=0.2,
                      rely=0.1)

verClientesButton.place(relx=0.2,
                      rely=0.2)

actualizarClientesButton.place(relx=0.2,
                      rely=0.3)

eliminarsButton.place(relx=0.2,
                      rely=0.4)

crearPagosButton.place(relx=0.2,
                      rely=0.5)

verPagosButton.place(relx=0.2,
                      rely=0.6)


dnaLabel.place(relx=0.1,
               rely=0.1
               )

dnaEntry.place(relx=0.2,
               rely=0.1)

nameLabel.place(relx=0.4,
                rely=0.1)

nameEntry.place(relx=0.5,
                rely=0.1)


direccionLabel.place(relx=0.1,
                rely=0.2)

direccionEntry.place(relx=0.2,
                rely=0.2)

telefonoLabel.place(relx=0.4,
                rely=0.2)

telefonoEntry.place(relx=0.5,
                rely=0.2)

fechaLabel.place(relx=0.1,
                rely=0.3)

fechaEntry.place(relx=0.2,
                rely=0.3)

equiposLabel.place(relx=0.4,
                rely=0.3)

equiposEntry.place(relx=0.5,
                rely=0.3)


paqueteLabel.place(relx=0.1,
                rely=0.4)

paquetedEntry.place(relx=0.2,
                rely=0.4)

mensualidadLabel.place(relx=0.4,
                rely=0.4)

mensualidadEntry.place(relx=0.5,
                rely=0.4)

localidadLabel.place(relx=0.1,
                rely=0.5)

localidadEntry.place(relx=0.2,
                rely=0.5)

ipClienteLabel.place(relx=0.4,
                rely=0.5)

ipClienteEntry.place(relx=0.5,
                rely=0.5)

comentarioLabel.place(relx=0.1,
                      rely=0.6)

comentarioEntry.place(relx=0.2,
                      rely=0.6)

panel.place(relx=0.0,
            rely=0.0,
            relwidth=0.2,
            relheight=1.0)

banner.place(relx=0.0,
            rely=0.0,
            relwidth=1.0,
            relheight=0.1)

centro.place(relx=0.2,
            rely=0.1,
            relwidth=1.0,
            relheight=1.0)
#============================================= CONFIG DE WIDGETS===================================================#



app.mainloop()