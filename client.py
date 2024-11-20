import socket
import sys
import threading
import os

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

def clear_line():
    if os.name == 'nt':
        sys.stdout.write('\r' + ' ' * 50 + '\r')
    else:
        sys.stdout.write('\033[2K\r')
    sys.stdout.flush()

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(BUFFER_SIZE).decode()
            if message:
                clear_line()
                print(f"Server: {message}")
                print("You: ", end='', flush=True)
                if "shutting down" in message:
                    sys.exit()
            else:
                print("\nServer disconnected")
                sys.exit()
        except:
            print("\nLost connection to server")
            sys.exit()

def send_messages(sock):
    print("You: ", end='', flush=True)
    while True:
        try:
            message = input()
            if message:
                sock.send(message.encode())
                if message.lower() == 'bye':
                    sys.exit()
                print("You: ", end='', flush=True)
        except:
            sys.exit()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Connected to chat server")
print("Type 'bye' to exit")

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
send_thread = threading.Thread(target=send_messages, args=(client_socket,))

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()

client_socket.close()