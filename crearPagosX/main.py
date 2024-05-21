from customtkinter import *

app = CTk()

def crearPago():
    toplevel_window = CTkToplevel(app)
    toplevel_window.geometry("800x500")
    toplevel_window.title("Registrar Pago")
    toplevel_window.resizable(False, False)

    panel2 = CTkFrame(master=toplevel_window, fg_color="#839192", border_color="#4D5656", border_width=0, corner_radius=0)


    panel2.place(relx=0.0,
                rely=0.0,
                relwidth=0.2,
                relheight=1.0)

crearPago()
app.mainloop()