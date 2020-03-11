import socket

# send and receive data through sockets
# AF_NET = ipv4, SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
  clientsocket, address = s.accept()
  print(f'connection from {address} has been established')
  clientsocket.send(bytes('welcome to socket land', 'utf-8'))
  clientsocket.close()
