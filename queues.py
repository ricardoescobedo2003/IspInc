import tkinter as tk
from tkinter import ttk
from librouteros import connect

# Función para obtener las colas
def obtener_queues():
    api = connect(username='admin', password='070523', host='122.122.124.1')
    queues = api('/queue/simple/print')
    return queues

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("MikroTik Queues")

# Crear un Treeview para mostrar las colas
tree = ttk.Treeview(root, columns=('Name', 'Target', 'Upload Max Limit', 'Download Max Limit'), show='headings')
tree.heading('Name', text='Name')
tree.heading('Target', text='Target')
tree.heading('Upload Max Limit', text='Upload Max Limit')
tree.heading('Download Max Limit', text='Download Max Limit')
tree.pack(fill=tk.BOTH, expand=True)

# Obtener las colas y añadirlas al Treeview
queues = obtener_queues()
for queue in queues:
    name = queue.get('name')
    target = queue.get('target')
    max_limit = queue.get('max-limit', '0/0').split('/')
    upload_max_limit = max_limit[0]
    download_max_limit = max_limit[1]
    if name and target:
        tree.insert('', 'end', values=(name, target, upload_max_limit, download_max_limit))

# Iniciar el loop de Tkinter
root.mainloop()
