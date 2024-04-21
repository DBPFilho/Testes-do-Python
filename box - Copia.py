import tkinter as tk

root = tk.Tk()

# Criar o label e posicioná-lo na grade
P1_label = tk.Label(root, text="Caso o valor de pares de base seja ")
P1_label.grid(row=0, column=0)
C1_label = tk.Label(root, text=" ,então o alelo será: ")
C1_label.grid(row=0, column=6)
# Criar a Entry box e posicioná-la na grade
P1_recebido = tk.Entry(root)
P1_recebido.grid(row=0, column=2)
C1_recebido = tk.Entry(root)
C1_recebido.grid(row=0, column=7)
# Criar a OptionMenu e posicioná-la na grade
options = ["_","maior", "menor", "igual", "entre"]
variable1 = tk.StringVar(root)
variable1.set(options[0])
select_box = tk.OptionMenu(root, variable1, *options)
select_box.grid(row=0, column=1)

# Criar o label e posicioná-lo na grade
P2_label = tk.Label(root, text="Caso o valor de pares de base seja ")
P2_label.grid(row=2, column=0)
P2_label.place(x=3000, y=3000)
C2_label = tk.Label(root, text=" ,então o alelo será: ")
C2_label.grid(row=2, column=6)
# Criar a Entry box e posicioná-la na grade
P2_recebido = tk.Entry(root)
P2_recebido.grid(row=2, column=2)
C2_recebido = tk.Entry(root)
C2_recebido.grid(row=2, column=7)
# Criar a OptionMenu e posicioná-la na grade
options = ["_","maior", "menor", "igual", "entre"]
variable2 = tk.StringVar(root)
variable2.set(options[0])
select_box = tk.OptionMenu(root, variable2, *options)
select_box.grid(row=2, column=1)

# Criar o label e posicioná-lo na grade
P3_label = tk.Label(root, text="Caso o valor de pares de base seja ")
P3_label.grid(row=3, column=0)
C3_label = tk.Label(root, text=" ,então o alelo será: ")
C3_label.grid(row=3, column=6)
# Criar a Entry box e posicioná-la na grade
P3_recebido = tk.Entry(root)
P3_recebido.grid(row=3, column=2)
C3_recebido = tk.Entry(root)
C3_recebido.grid(row=3, column=7)
# Criar a OptionMenu e posicioná-la na grade
options = ["_","maior", "menor", "igual", "entre"]
variable3 = tk.StringVar(root)
variable3.set(options[0])
select_box = tk.OptionMenu(root, variable3, *options)
select_box.grid(row=3, column=1)

# Criar o label e posicioná-lo na grade
P4_label = tk.Label(root, text="Caso o valor de pares de base seja ")
P4_label.grid(row=4, column=0)
C4_label = tk.Label(root, text=" ,então o alelo será: ")
C4_label.grid(row=4, column=6)
# Criar a Entry box e posicioná-la na grade
P4_recebido = tk.Entry(root)
P4_recebido.grid(row=4, column=2)
C4_recebido = tk.Entry(root)
C4_recebido.grid(row=4, column=7)
# Criar a OptionMenu e posicioná-la na grade
options = ["_","maior", "menor", "igual", "entre"]
variable4 = tk.StringVar(root)
variable4.set(options[0])
select_box = tk.OptionMenu(root, variable4, *options)
select_box.grid(row=4, column=1)


#Criando um valor de teste
resultado_cont=6

# Função para aparecer os widgets
def mostrar():
    P2_label.grid(row=2)

# Função para imprimir os valores dos widgets
def testar():
    valor_selecionado1 = variable1.get()
    match valor_selecionado1:
        case "_":
            print ("")
        case "maior":
            P1=int(P1_recebido.get())
            C1=C1_recebido.get()
            if resultado_cont>P1:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C1)
                resultado_parametro.configure(state="disabled")
        case "menor":
            P1=int(P1_recebido.get())
            C1=C1_recebido.get()
            if resultado_cont<P1:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C1)
                resultado_parametro.configure(state="disabled")
        case "igual":
            P1=int(P1_recebido.get())
            C1=C1_recebido.get()
            if resultado_cont==P1:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C1)
                resultado_parametro.configure(state="disabled")
        case "entre":
            P1=int(P1_recebido.get())
            C1=C1_recebido.get()
            resultado_parametro.configure(state="normal")
            resultado_parametro.delete("1.0", "end")
            resultado_parametro.insert("end", C1)
            resultado_parametro.configure(state="disabled")
    valor_selecionado2 = variable2.get()
    match valor_selecionado2:
        case "_":
            print ("")
        case "maior":
            P2=int(P2_recebido.get())
            C2=C2_recebido.get()
            if resultado_cont>P2:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C2)
                resultado_parametro.configure(state="disabled")
        case "menor":
            P2=int(P2_recebido.get())
            C2=C2_recebido.get()
            if resultado_cont<P2:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C2)
                resultado_parametro.configure(state="disabled")
        case "igual":
            P2=int(P2_recebido.get())
            C2=C2_recebido.get()
            if resultado_cont==P2:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C2)
                resultado_parametro.configure(state="disabled")
        case "entre":
            P2=int(P2_recebido.get())
            C2=C2_recebido.get()
            valor_selecionado2 = variable2.get()
            resultado_parametro.configure(state="normal")
            resultado_parametro.delete("1.0", "end")
            resultado_parametro.insert("end", C2)
            resultado_parametro.configure(state="disabled")
    valor_selecionado3 = variable3.get()
    match valor_selecionado3:
        case "_":
            print ("")
        case "maior":
            P3=int(P3_recebido.get())
            C3=C3_recebido.get()
            if resultado_cont>P3:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C3)
                resultado_parametro.configure(state="disabled")
        case "menor":
            P3=int(P3_recebido.get())
            C3=C3_recebido.get()
            if resultado_cont<P3:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C3)
                resultado_parametro.configure(state="disabled")
        case "igual":
            P3=int(P3_recebido.get())
            C3=C3_recebido.get()            
            if resultado_cont==P3:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C3)
                resultado_parametro.configure(state="disabled")
        case "entre":
            P3=int(P3_recebido.get())
            C3=C3_recebido.get()
            resultado_parametro.configure(state="normal")
            resultado_parametro.delete("1.0", "end")
            resultado_parametro.insert("end", C3)
            resultado_parametro.configure(state="disabled")
    valor_selecionado4 = variable4.get()
    match valor_selecionado4:
        case "_":
            print ("")
        case "maior":
            P4=int(P4_recebido.get())
            C4=C4_recebido.get()
            if resultado_cont>P4:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C4)
                resultado_parametro.configure(state="disabled")
        case "menor":
            P4=int(P4_recebido.get())
            C4=C4_recebido.get()
            if resultado_cont<P4:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C4)
                resultado_parametro.configure(state="disabled")
        case "igual":
            P4=int(P4_recebido.get())
            C4=C4_recebido.get()            
            if resultado_cont==P4:
                resultado_parametro.configure(state="normal")
                resultado_parametro.delete("1.0", "end")
                resultado_parametro.insert("end", C4)
                resultado_parametro.configure(state="disabled")
        case "entre":
            P4=int(P4_recebido.get())
            C4=C4_recebido.get()
            resultado_parametro.configure(state="normal")
            resultado_parametro.delete("1.0", "end")
            resultado_parametro.insert("end", C4)
            resultado_parametro.configure(state="disabled")


# Criar o botão e posicioná-lo na grade
botao_buscar = tk.Button(root, text="Testar", command=testar)
botao_buscar.grid(row=7, column=0, columnspan=2)

# Criar o botão e posicioná-lo na grade mostrar
botao_buscar = tk.Button(root, text="Testar", command=mostrar)
botao_buscar.grid(row=10, column=0)


# Cria o widget para exibir o resultado da busca
resultado_parametro = tk.Text(root)
resultado_parametro.configure(state="disabled", height=1, width=15, font=("Helvetica", 10))
resultado_parametro.tag_configure("encontrado", foreground="red")
resultado_parametro.grid(row=8, column =0, columnspan=2)
resultado_parametro.pack

root.mainloop()

