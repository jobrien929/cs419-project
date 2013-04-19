import socket, ssl, pprint

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_verify_locations(cafile='crt/cert.pem')
context.verify_mode = ssl.CERT_REQUIRED

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_ssl = context.wrap_socket(sock)
sock_ssl.connect(('localhost', 4444))
print("Connected to server...")
try:
    pprint.pprint(sock_ssl.getpeercert())
finally:
    sock_ssl.close()
    
