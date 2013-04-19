import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_cert_chain(certfile="crt/ctf-cert.pem", keyfile="crt/ctf-key.pem")

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("localhost", 4444))
listener.listen(5)
print("Waiting for connection...")
sock, peer = listener.accept()
ssl_sock = context.wrap_socket(sock, server_side=True)
print("connected via ssl to", peer)

data = 1
while data:
    data = ssl_sock.recv()
    
ssl_sock.close()

