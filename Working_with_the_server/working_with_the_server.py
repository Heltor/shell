import socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('HOST', PORT))
    while True:
        data = s.recv(4096)
        if not data:
            continue
        st = data.decode("ascii")
        # Here comes the task processing algorithm, the results of which should be in a variable result
        s.send(str(result)+'\n'.encode('utf-8'))
finally:
    s.close()
