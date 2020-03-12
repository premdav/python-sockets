import socket
import time
import pickle

HEAD_SIZE = 10

# send and receive data through sockets
# AF_NET = ipv4, SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
  clientsocket, address = s.accept()
  print(f'connection from {address} has been established')
  thing = { 1: 'Hey', 2: 'There', 3: 'Person' }
  msg = pickle.dumps(thing)
  msg = bytes(f'{len(msg):<{HEAD_SIZE}}', 'utf-8') + msg
  clientsocket.send(msg)

  while True:
    time.sleep(3)
    p = { "msg": "hello there fine person, it is", "time": time.time() }
    msg = pickle.dumps(p)
    msg = bytes(f'{len(msg):<{HEAD_SIZE}}', 'utf-8') + msg
    clientsocket.send(msg)
