import socket
import sounddevice as sd

HOST = "192.168.1.2"# O servidor escutará em todas as interfaces disponíveis
PORT = 12345     # Porta de comunicação

# Inicializa o dispositivo de áudio
def audio_callback(indata, frames, time, status):
    stream_server.sendall(indata.tobytes())

# Configura o servidor socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Aguardando conexão do celular...")

# Aceita a conexão do celular
client_socket, address = server_socket.accept()
print("Conexão estabelecida com:", address)

# Inicializa o dispositivo de áudio para receber o áudio do celular
stream_server = sd.InputStream(callback=audio_callback)
with stream_server:
    while True:
        pass
