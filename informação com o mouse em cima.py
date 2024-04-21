import tkinter as tk
from tkinter import ttk

def mostrar_tooltip(event):
    label.tooltip.place(x=event.x_root, y=event.y_root-30)

def ocultar_tooltip(event):
    label.tooltip.place_forget()

root = tk.Tk()

label = ttk.Label(root, text="Passe o mouse sobre mim")
label.pack(pady=10)

label.tooltip = tk.Label(root, bg="white", relief="solid", borderwidth=1)
label.tooltip.config(text="Texto de Informação")

label.bind("<Enter>", mostrar_tooltip)
label.bind("<Leave>", ocultar_tooltip)

root.mainloop()
