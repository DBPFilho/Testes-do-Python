import tkinter as tk

class Aplicacao(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("Minha Aplicação")
        
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        self.frames = {}  # Dicionário para armazenar os frames
        
        self.criar_frames()
        self.mostrar_frame("cabecalho")
    
    def criar_frames(self):
        # Crie uma classe para cada página/frame da sua aplicação
        
        class Cabecalho(tk.Frame):
            def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                self.controller = controller
                
                label = tk.Label(self, text="Cabeçalho")
                label.grid(row=0, column=0, pady=10, padx=10)
                
                nome_label = tk.Label(self, text="Qual o seu nome: ")
                nome_label.grid(row=1, column=0, pady=10, padx=10)
                nome_recebido = tk.Entry(self)
                nome_recebido.grid(row=1, column=1, pady=10, padx=10)

                nomepersonagem_label = tk.Label(self, text="Qual o nome do seu personagem: ")
                nomepersonagem_label.grid(row=2, column=0, pady=10, padx=10)
                nomepersonagem_recebido = tk.Entry(self)
                nomepersonagem_recebido.grid(row=2, column=1, pady=10, padx=10)

                global opcoes_subclasse
                opcoes_subclasse = ["_"]
                classe_label = tk.Label(self, text="Qual sua classe: ")
                classe_label.grid(row=3, column=0, pady=10, padx=10)
                classe_options = ["_","Bárbaro", "Bardo", "Bruxo", "Clérigo", "Druida", "Feiticeiro", "Guerreiro", "Ladino", "Mago", "Monge", "Paladino", "Patrulheiro"]
                classe = tk.StringVar(self)
                classe.set(classe_options[0])
                classe_box = tk.OptionMenu(self, classe, *classe_options)
                classe_box.grid(row=3, column=1)

                raca_label = tk.Label(self, text="Qual sua raça: ")
                raca_label.grid(row=4, column=0, pady=10, padx=10)
                raca_options = ["_","Anão", "Elfo", "Halfling", "Humano", "Draconato", "Gnomo", "Meio-elfo", "Meio-orc", "Tiefling"]
                raca = tk.StringVar(self)
                raca.set(raca_options[0])
                raca_box = tk.OptionMenu(self, raca, *raca_options)
                raca_box.grid(row=4, column=1)

                global nivel
                nivel_label = tk.Label(self, text="Qual seu nível: ")
                nivel_label.grid(row=5, column=0, pady=10, padx=10)
                nivel_options = ["1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
                nivel = tk.StringVar(self)
                nivel.set(nivel_options[0])
                nivel_box = tk.OptionMenu(self, nivel, *nivel_options)
                nivel_box.grid(row=5, column=1)

                antecedente_label = tk.Label(self, text="Qual seu antecedente: ")
                antecedente_label.grid(row=6, column=0, pady=10, padx=10)
                antecedente_options = ["falta pensar se é selectbox ou n","2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
                antecedente = tk.StringVar(self)
                antecedente.set(antecedente_options[0])
                antecedente_box = tk.OptionMenu(self, antecedente, *antecedente_options)
                antecedente_box.grid(row=6, column=1)

                alinhamento_label = tk.Label(self, text="Qual seu alinhamento: ")
                alinhamento_label.grid(row=7, column=0, pady=10, padx=10)
                alinhamento_recebido = tk.Entry(self)
                alinhamento_recebido.grid(row=7, column=1, pady=10, padx=10)

                tasha_var = tk.IntVar()
                xanathar_var = tk.IntVar()
                xanathar = tk.Checkbutton(self, text="Xanathar", variable=xanathar_var)
                xanathar.grid(row=3, column=3)
                tasha = tk.Checkbutton(self, text="Tasha", variable=tasha_var)
                tasha.grid(row=4, column=3)                

                def atualizar_selectbox():
                # Atualiza as opções da select box na página "subclasse" com base na opção selecionada na página "classe"
                    # Limpa as opções antigas
                    global opcao_selecionada                  
                    opcao_selecionada = classe.get()
                    if opcao_selecionada == "Bárbaro":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["Caminho do Furioso", "Caminho do Guerreiro Totem"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                    if opcao_selecionada == "Bardo":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["Colégio do Conhecimento", "Colégio da Bravura"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                    if opcao_selecionada == "Bruxo":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["Arquifeérico", "Demoníaco", "O Grande Antigo"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                    if opcao_selecionada == "Clérigo":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["Domínio do Conhecimento", "Vida", "Luz", "Natureza","Tormenta", "Trapaça", "Guerra"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                    if opcao_selecionada == "Druida":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["Circulo das Terras", "Circulo da Lua"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                    if opcao_selecionada == "Feiticeiro":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["Linhagem Draconica", "Magia Selvagem"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                    if opcao_selecionada == "Guerreiro":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["O Campeão", "O Mestre da Batalha", "O Cavaleiro Místico"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                    if opcao_selecionada == "Ladino":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["Ladrão", "Assassino", "Trapaceiro Arcano"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                    if opcao_selecionada == "Mago":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["Abjuração", "Conjuração", "Adivinhação", "Encantamento", "Evocação", "Ilusão", "Necromancia", "Transmutação"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                    if opcao_selecionada == "Monge":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["O Estilo da Mão Aberta", "O Estilo da Sombra", "O Estilo dos Quatro Elementos"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                    if opcao_selecionada == "Paladino":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["Juramento da Devoção", "Juramento dos Anciões", "Juramento da Vingança"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                    if opcao_selecionada == "Patrulheiro":
                        subclasse_box["menu"].delete(0, "end")
                        opcoes_subclasse = ["arquétipo do Caçador", "Mestre da Besta"]
                        if tasha_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["tasha"]
                        if xanathar_var.get() ==1:
                            opcoes_subclasse = opcoes_subclasse + ["xanathar"]
                        for opcao in opcoes_subclasse:
                            subclasse_box["menu"].add_command(label=opcao, command=tk._setit(subclasse, opcao))
                def controle_subclasse():
                    nivel_atual = int(nivel.get())
                    if nivel_atual<=2 and opcao_selecionada=="Guerreiro":
                        subclasse_box["menu"].delete(0, "end")
                botao = tk.Button(self, text="Subclasse", command = lambda: (atualizar_selectbox(), controller.mostrar_frame("subclasse"), controle_subclasse()))
                botao.grid(row=8, column=0, pady=10, padx=10)


        class Subclasse(tk.Frame):
            def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                self.controller = controller
                
                label = tk.Label(self, text="Subclasse")
                label.grid(row=0, column=0, pady=10, padx=10)

                # Select box correspondente na página "subclasse"
                global subclasse_box
                global subclasse
                subclasse_label = tk.Label(self, text="Qual sua subclasse: ")
                subclasse_label.grid(row=1, column=0, pady=10, padx=10)
                subclasse_options = [opcoes_subclasse]
                subclasse = tk.StringVar(self)
                subclasse.set(subclasse_options[0])
                subclasse_box = tk.OptionMenu(self, subclasse, *subclasse_options)
                subclasse_box.grid(row=1, column=1)

                
                def informacao_classe(*args):
                    subclasse_selecionada = subclasse.get()
                    nivel_atual = int(nivel.get())
                    if nivel_atual>=1 and opcao_selecionada=="Guerreiro":                        
                        texto_classe="Estilo de luta \n"
                        selecao_classe_label.config(text = texto_classe)
                        informacao_classe_label.config(text='{} nível {} tem:'.format(opcao_selecionada, nivel_atual))
                    if nivel_atual>=2 and opcao_selecionada=="Guerreiro":
                        texto_classe= texto_classe + "Surto de ação \n"
                        selecao_classe_label.config(text = texto_classe)
                    if nivel_atual>=3 and opcao_selecionada=="Guerreiro":
                        selecao_classe_label.config(text="Arquétipo marcial")
                    if nivel_atual>=4 and opcao_selecionada=="Guerreiro":
                        selecao_classe_label.config(text="Você é um guerreiro nível 4")
                    if nivel_atual>=1 and subclasse_selecionada=="O Campeão":
                        selecao_subclasse_label.config(text="Você ainda não tem acesso a subclasse, apenas no nível 3")
                    if nivel_atual>=2 and subclasse_selecionada=="O Campeão":
                        selecao_subclasse_label.config(text="Você ainda não tem acesso a subclasse, apenas no nível 3")
                    if nivel_atual>=3 and subclasse_selecionada=="O Campeão":
                        selecao_subclasse_label.config(text="Você é um O Campeão nível 3 e ganha blablabla")

                subclasse.trace("w", informacao_classe)
                botao = tk.Button(self, text="Voltar para o cabeçalho", command=lambda: (controller.mostrar_frame("cabecalho"), subclasse.set(subclasse_options[0]), selecao_classe_label.config(text = ""), informacao_classe_label.config(text="")))
                botao.grid(row=2, column=0, pady=10, padx=10)
                selecao_classe_label = tk.Label(self)
                selecao_classe_label.grid(row=3, column=3)
                selecao_subclasse_label = tk.Label(self)
                selecao_subclasse_label.grid(row=3, column=4)

                informacao_classe_label = tk.Label(self)
                informacao_classe_label.grid(row=1, column=3)
                

                
        # Adicione cada classe de página/frame ao dicionário de frames
        self.frames["cabecalho"] = Cabecalho(self.container, self)
        self.frames["subclasse"] = Subclasse(self.container, self)
        
        # Posicione cada frame na mesma localização dentro do container
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")
    
    def mostrar_frame(self, nome_frame):
        frame = self.frames[nome_frame]
        frame.tkraise()  # Exiba o frame desejado acima dos outros frames


# Crie uma instância da aplicação e execute-a
app = Aplicacao()
app.mainloop()
