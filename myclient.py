if __name__ == "__main__":
    import socket
    sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
    sock.connect('server_socket')
    print sock.recv(11)
    sock.close()
