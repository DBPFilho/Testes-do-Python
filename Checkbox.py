import tkinter as tk

def exibir_selecao():
    selecionadas = []
    if checkbox_var1.get() == 1:
        selecionadas.append("Opção 1")
    if checkbox_var2.get() == 1:
        selecionadas.append("Opção 2")
    if checkbox_var3.get() == 1:
        selecionadas.append("Opção 3")
    if checkbox_var4.get() == 1:
        selecionadas.append("Opção 4")
    
    if selecionadas:
        print("Opções selecionadas:", ", ".join(selecionadas))
    else:
        print("Nenhuma opção foi selecionada.")

# Crie uma janela
janela = tk.Tk()

# Crie variáveis de controle para armazenar o estado das checkboxes
checkbox_var1 = tk.IntVar()
checkbox_var2 = tk.IntVar()
checkbox_var3 = tk.IntVar()
checkbox_var4 = tk.IntVar()

# Crie as checkboxes
checkbox1 = tk.Checkbutton(janela, text="Opção 1", variable=checkbox_var1)
checkbox1.pack()
checkbox2 = tk.Checkbutton(janela, text="Opção 2", variable=checkbox_var2)
checkbox2.pack()
checkbox3 = tk.Checkbutton(janela, text="Opção 3", variable=checkbox_var3)
checkbox3.pack()
checkbox4 = tk.Checkbutton(janela, text="Opção 4", variable=checkbox_var4)
checkbox4.pack()

# Crie um botão para exibir as seleções
botao = tk.Button(janela, text="Exibir seleções", command=exibir_selecao)
botao.pack()

# Inicie o loop principal da janela
janela.mainloop()
