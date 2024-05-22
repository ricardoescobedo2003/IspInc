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
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import datetime
import otro

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
