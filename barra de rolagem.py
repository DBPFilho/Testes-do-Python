import tkinter as tk
from tkinter import ttk

def adicionar_label():
    new_label = tk.Label(canvas, text=f"Label {len(labels) + 1}")
    labels.append(new_label)
    canvas.create_window(0, len(labels) * 30, anchor="nw", window=new_label)
    update_scroll_region()

def update_scroll_region():
    canvas.configure(scrollregion=canvas.bbox("all"))

# Criação da janela principal
root = tk.Tk()
root.title("Barra de Rolagem")

# Frame contendo a barra de rolagem
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Criação do canvas com barra de rolagem vertical
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Lista para armazenar as labels criadas
labels = []

# Botão para adicionar novas labels
botao_adicionar = ttk.Button(root, text="Adicionar Label", command=adicionar_label)
botao_adicionar.pack()

# Chamada inicial para ajustar o tamanho da região rolável
update_scroll_region()

root.mainloop()
