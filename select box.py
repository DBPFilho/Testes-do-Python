import tkinter as tk

def atualizar_selecao(*args):
    selecionada = selectbox_var.get()
    label_selecao.config(text=f"Opção selecionada: {selecionada}")

# Crie uma janela
janela = tk.Tk()

# Crie uma variável de controle para armazenar a opção selecionada
selectbox_var = tk.StringVar(janela)

# Defina as opções da selectbox
opcoes = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]

# Crie a selectbox
selectbox = tk.OptionMenu(janela, selectbox_var, *opcoes)
selectbox.pack()

# Associe a função 'atualizar_selecao' ao evento de alteração da variável 'selectbox_var'
selectbox_var.trace("w", atualizar_selecao)

# Crie um rótulo para exibir a seleção
label_selecao = tk.Label(janela)
label_selecao.pack()

# Inicie o loop principal da janela
janela.mainloop()
