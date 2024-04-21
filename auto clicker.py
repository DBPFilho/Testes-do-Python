import time
import random
import pyautogui
import tkinter as tk
import threading
import pydirectinput

# Cria a janela
janela = tk.Tk()
janela.title("Auto Clicker DANEL")
janela.geometry("400x400")

# Cria labels para definir o tempo
labe_tmin = tk.Label(janela, text="Tempo mínimo: ")
labe_tmin.grid(row=0, column=0)
labe_tmin_entrada = tk.Entry(janela)
labe_tmin_entrada.grid(row=0, column=1)

labe_tmax = tk.Label(janela, text="Tempo máximo: ")
labe_tmax.grid(row=1, column=0)
labe_tmax_entrada = tk.Entry(janela)
labe_tmax_entrada.grid(row=1, column=1)

# Define uma thread para o autoclicker
class AutoClickerThread(threading.Thread):
    def __init__(self, intervalo_minimo, intervalo_maximo):
        threading.Thread.__init__(self)
        self.intervalo_minimo = intervalo_minimo
        self.intervalo_maximo = intervalo_maximo
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            tempo_espera = random.uniform(self.intervalo_minimo, self.intervalo_maximo)
            print(tempo_espera)
            time.sleep(tempo_espera)
            pyautogui.click()

    def stop(self):
        self._stop_event.set()

auto_clicker_thread = None

# Define a função para iniciar o autoclicker
def iniciar_autoclicker():
    global auto_clicker_thread
    if auto_clicker_thread is None:
        intervalo_minimo = float("{:.2f}".format(float(labe_tmin_entrada.get())))
        intervalo_maximo = float("{:.2f}".format(float(labe_tmax_entrada.get())))
        auto_clicker_thread = AutoClickerThread(intervalo_minimo, intervalo_maximo)
        auto_clicker_thread.start()

# Cria o botão para chamar a função
botao_clic = tk.Button(janela, text="Clicar", command=iniciar_autoclicker)
botao_clic.grid(row=3, column=0)

# Define a função para interromper o autoclicker
def interromper_autoclicker():
    global auto_clicker_thread
    if auto_clicker_thread is not None:
        auto_clicker_thread.stop()
        auto_clicker_thread = None

# Cria o botão para interromper o autoclicker
botao_interromper = tk.Button(janela, text="Interromper", command=interromper_autoclicker)
botao_interromper.grid(row=3, column=1)

#Função para obter a posição
def obter_posicao_clicar():
    global posicao_clicar
    posicao_clicar = pyautogui.position()
    print (posicao_clicar)

# Cria o botão para obter a posição do clique
botao_posicao = tk.Button(janela, text="Obter posição", command=obter_posicao_clicar)
botao_posicao.grid(row=3, column=3)
janela.bind('<KeyPress-F1>', lambda event: obter_posicao_clicar())

# Mantém a janela aberta
janela.mainloop()
