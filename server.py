import socket
import select
import sys

HOST = ''
PORT = 5000
BUFFER_SIZE = 1024

def disconnect_all_clients(sock_list, server_sock):
    remaining_socks = [server_sock]
    for sock in sock_list:
        if sock != server_sock:
            try:
                sock.send("Server is shutting down. Goodbye!".encode())
                sock.close()
            except:
                pass
    return remaining_socks

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Chat server started on port {PORT}")
print("Waiting for client to connect...")

connected_clients = [server_socket]
running = True

while running:
    try:
        read_sockets, _, _ = select.select(connected_clients, [], [])

        for sock in read_sockets:
            if sock == server_socket:
                client_socket, addr = server_socket.accept()
                connected_clients.append(client_socket)
                print(f"Client connected from {addr}")
                
            else:
                try:
                    message = sock.recv(BUFFER_SIZE).decode()
                    if message:
                        if message.strip().lower() == 'bye':
                            print(f"Client is leaving the chat")
                            sock.close()
                            connected_clients.remove(sock)
                            if len(connected_clients) == 1:
                                print("Waiting for client to connect...")
                        else:
                            print(f"\nClient: {message}")
                            response = input("Server: ")
                            if response.lower() == 'bye':
                                sock.send("Server is shutting down. Goodbye!".encode())
                                sock.close()
                                connected_clients.remove(sock)
                                print("\nServer shutting down...")
                                running = False
                                break
                            else:
                                sock.send(response.encode())
                    else:
                        print("Client disconnected")
                        sock.close()
                        connected_clients.remove(sock)
                        if len(connected_clients) == 1:
                            print("Waiting for client to connect...")
                        
                except:
                    print("Client disconnected unexpectedly")
                    if sock in connected_clients:
                        sock.close()
                        connected_clients.remove(sock)
                    if len(connected_clients) == 1:
                        print("Waiting for client to connect...")
                    continue
    except KeyboardInterrupt:
        print("\nServer shutting down...")
        running = False
    except Exception as e:
        print(f"Error: {e}")
        running = False

for sock in connected_clients:
    if sock != server_socket:
        try:
            sock.close()
        except:
            pass
server_socket.close()
sys.exit()