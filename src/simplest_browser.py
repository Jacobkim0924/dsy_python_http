import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.nytimes.com', 80))
#cmd = 'GET https://www.nytimes.com/index.html  HTTP/1.0\r\n\r\n'.encode()
cmd = 'GET https://www.nytimes.com/2019/04/30/us/politics/trump-infrastructure-plan.html HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
