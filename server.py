import socket
import time

HEAD_SIZE = 10

# send and receive data through sockets
# AF_NET = ipv4, SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
  clientsocket, address = s.accept()
  print(f'connection from {address} has been established')
  msg = 'welcome to the server'
  msg = f'{len(msg):<{HEAD_SIZE}}' + msg
  clientsocket.send(bytes(msg, 'utf-8'))

  while True:
    time.sleep(3)
    msg = f'time: {time.time()}'
    msg = f'{len(msg):<{HEAD_SIZE}}' + msg
    clientsocket.send(bytes(msg, 'utf-8'))
