import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

def abrir_arquivo():
    filepath = filedialog.askopenfilename(title="Selecione um arquivo FASTA", filetypes=[("Arquivos FASTA", "*.fasta *.fa")])
    if filepath:
        with open(filepath, "r") as arquivo:
            linhas = arquivo.readlines()
            mostrar_conteudo(linhas)

def mostrar_conteudo(linhas):
    texto.delete("1.0", tk.END)  # Limpa o texto atual
    titulo_atual = ""
    conteudo_atual = ""
    maior_conteudo = ("", "", 0)  # Título, Conteúdo e Tamanho do maior texto
    menor_conteudo = ("", "", float('inf'))  # Título, Conteúdo e Tamanho do menor texto

    for linha in linhas:
        if linha.startswith(">"):
            if titulo_atual and conteudo_atual:
                texto.insert(tk.END, f"{titulo_atual}\n{conteudo_atual}\n\n")
                tamanho_atual = len(conteudo_atual.replace(" ", "").replace("\n", ""))
                if tamanho_atual > maior_conteudo[2]:
                    maior_conteudo = (titulo_atual, conteudo_atual, tamanho_atual)
                if tamanho_atual < menor_conteudo[2]:
                    menor_conteudo = (titulo_atual, conteudo_atual, tamanho_atual)
            titulo_atual = linha.strip()
            conteudo_atual = ""
        else:
            conteudo_atual += linha.strip()
    
    if titulo_atual and conteudo_atual:
        texto.insert(tk.END, f"{titulo_atual}\n{conteudo_atual}\n\n")
        tamanho_atual = len(conteudo_atual.replace(" ", "").replace("\n", ""))
        if tamanho_atual > maior_conteudo[2]:
            maior_conteudo = (titulo_atual, conteudo_atual, tamanho_atual)
        if tamanho_atual < menor_conteudo[2]:
            menor_conteudo = (titulo_atual, conteudo_atual, tamanho_atual)
    
    if maior_conteudo[0] and maior_conteudo[1]:
        texto.insert(tk.END, f"Maior conteúdo ({maior_conteudo[2]} caracteres):\n{maior_conteudo[0]}\n{maior_conteudo[1]}\n\n")
    
    if menor_conteudo[0] and menor_conteudo[1]:
        texto.insert(tk.END, f"Menor conteúdo ({menor_conteudo[2]} caracteres):\n{menor_conteudo[0]}\n{menor_conteudo[1]}\n\n")

# Cria a janela principal
janela = tk.Tk()
janela.title("Visualizador de Arquivos FASTA")

# Botão para abrir o arquivo
botao_abrir = tk.Button(janela, text="Abrir Arquivo FASTA", command=abrir_arquivo)
botao_abrir.pack(pady=10)

# Área de texto com barra de rolagem
scroll = tk.Scrollbar(janela)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, yscrollcommand=scroll.set, font=("Helvetica", 12))
texto.pack(expand=True, fill="both")

scroll.config(command=texto.yview)

janela.mainloop()
