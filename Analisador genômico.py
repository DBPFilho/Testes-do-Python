import re
import tkinter as tk

# Cria a janela
janela = tk.Tk()
janela.title("Busca de Sequência")
janela.geometry("400x400")

# Cria as labels e as caixas de texto
label_seq_f = tk.Label(janela, text="Primer foward: ")
label_seq_f.pack()
entrada_seq_f = tk.Entry(janela)
entrada_seq_f.pack()

label_seq_r = tk.Label(janela, text="Primer reverse: ")
label_seq_r.pack()
entrada_seq_r = tk.Entry(janela)
entrada_seq_r.pack()

label_seq_busca = tk.Label(janela, text="Digite a sequência a ser buscada: ")
label_seq_busca.pack()
entrada_seq_busca = tk.Entry(janela)
entrada_seq_busca.pack()

# Função para buscar a sequência
def buscar_sequencia():
    seqf = entrada_seq_f.get().upper()
    seq = entrada_seq_r.get().upper()

    # Divide a sequência em conjuntos de 10
    seqf_dividida = [seqf[i:i+10] for i in range(0, len(seqf), 10)]
    seq_dividida = [seq[i:i+10] for i in range(0, len(seq), 10)]

    # Realiza as substituições
    seq_substituida = ""
    for conjunto in seq_dividida:
        conjunto_substituido = conjunto.replace("A", "B").replace("T", "V").replace("C", "D").replace("G", "H")
        for nucleotideo in conjunto_substituido:
            conjunto_substituido2 = nucleotideo.replace("B", "T").replace("V", "A").replace("D", "G").replace("H", "C")
            seq_substituida += conjunto_substituido2

    # Inverte a sequência substituída
    seq_invertida = seq_substituida[::-1]

    # Busca a sequência
    seq_busca = entrada_seq_busca.get().replace(" ", "").upper()
    seq_busca = re.sub(r'\s+', '', seq_busca)
    seq_busca = re.sub(r'\d', '', seq_busca)

    # Marca as sequências encontradas em vermelho
    seq_busca_formatada = seq_busca
    if seqf in seq_busca:
        seq_encontrada = seqf
        pos = seq_busca.find(seq_encontrada)
        seq_busca_formatada = seq_busca[:pos] + seq_encontrada + seq_busca[pos+len(seq_encontrada):]
        resultado_busca.configure(state="normal")
        resultado_busca.insert("end", seq_busca_formatada)
        resultado_busca.tag_add("encontrado", f"1.{pos}", f"1.{pos+len(seq_encontrada)}")
        resultado_busca.configure(state="disabled")

    if seq_invertida in seq_busca:
        seq_encontrada2 = seq_invertida
        pos = seq_busca.find(seq_encontrada2)
        seq_busca_formatada = seq_busca_formatada[:pos] + seq_encontrada2 + seq_busca_formatada[pos+len(seq_encontrada2):]
        resultado_busca.configure(state="normal")
        resultado_busca.insert("end", seq_busca_formatada)
        resultado_busca.tag_add("encontrado", f"1.{pos}", f"1.{pos+len(seq_encontrada2)}")
        resultado_busca.configure(state="disabled")

    if seqf not in seq_busca and seq_invertida not in seq_busca:
        resultado_busca.configure(state="normal")
        resultado_busca.delete("1.0", "end")
        resultado_busca.insert("end", "Sequência não encontrada!")
        resultado_busca.configure(state="disabled")
        return
    # Cria uma lista de tuplas com a posição inicial e final de cada sequência encontrada em vermelho
    posicoes = []
    if seqf in seq_busca:
        pos_ini = seq_busca_formatada.find('{}'.format(seqf))
        pos_fim = pos_ini + len(seqf)
        posicoes.append((pos_ini, pos_fim))

    if seq_invertida in seq_busca:
        pos_ini = seq_busca_formatada.rfind('{}'.format(seq_invertida)) 
        pos_fim = pos_ini + len(seq_invertida)
        posicoes.append((pos_ini, pos_fim))

    # Calcula a quantidade de letras entre a última letra em vermelho da primeira sequência encontrada
    # e a primeira letra em vermelho da última sequência encontrada
    if len(posicoes) >= 2:
        pos_ini_primeira_sequencia = posicoes[0][0]
        pos_fim_ultima_sequencia = posicoes[-1][1]
        qtd_letras_entre_sequencias = pos_fim_ultima_sequencia - posicoes[0][1] + seq_busca_formatada[pos_fim_ultima_sequencia:].find('\033[31m') + len(seq_invertida)
        resultado_cont.configure(state="normal")
        resultado_cont.delete("1.0", "end")
        resultado_cont.insert(tk.END, f"Foram encontrados: {qtd_letras_entre_sequencias} pares de base")
        resultado_cont.configure(state="disabled")
    else:
        resultado_cont.configure(state="normal")
        resultado_cont.delete("1.0", "end")
        resultado_cont.insert(tk.END, "Sequência não encontrada!")
        resultado_cont.configure(state="disabled")
    print("{}".format(print("{qtd_letras_entre_sequencias}")))
    # Imprime a sequência encontrada
    resultado_busca.insert("end", seq_busca_formatada)

# Cria o botão de busca
botao_buscar = tk.Button(janela, text="Buscar", command=buscar_sequencia)
botao_buscar.pack()

# Cria o widget para exibir o resultado da busca
resultado_busca = tk.Text(janela)
resultado_busca.configure(state="disabled", height=10, font=("Helvetica", 10))
resultado_busca.tag_configure("encontrado", foreground="red")

# Adiciona o widget resultado_busca à janela
resultado_busca.pack()

# Cria o widget para exibir o resultado da contagem
resultado_cont = tk.Text(janela)
resultado_cont.configure(state="disabled", height=3, font=("Helvetica", 10))

# Adiciona o widget resultado_cont à janela
resultado_cont.pack()




