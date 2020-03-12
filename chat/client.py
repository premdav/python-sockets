import socket
import select
import errno
import sys

HEAD_LEN = 10
IP = '127.0.0.1'
PORT = 1234
my_name = input('Username: ')

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((IP, PORT))
client_sock.setblocking(False)

username = my_name.encode('utf-8')
username_head = f"{len(username):<{HEAD_LEN}}".encode('utf-8')
client_sock.send(username_head + username)

while True:
  msg = input(f'{my_name} > ')
  if msg:
    msg = msg.encode('utf-8')
    msg_head = f'{len(msg):<{HEAD_LEN}}'.encode('utf-8')
    client_sock.send(msg_head + msg)
  
  try:
    while True:
      username_head = client_sock.recv(HEAD_LEN)
      if not len(username_head):
        print('connection closed by server')
        sys.exit()
      username_len = int(username_head.decode('utf-8').strip())
      username = client_sock.recv(username_len).decode('utf-8')

      msg_head = client_sock.recv(HEAD_LEN)
      msg_len = int(msg_head.decode('utf-8').strip())
      msg = client_sock.recv(msg_len).decode('utf-8')
      print(f'{username} > {msg}')

  except IOError as e:
    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
      print('reading error', str(e))
      sys.exit()
    continue

  except Exception as e:
    print('general err: ', str(e))
    sys.exit()
