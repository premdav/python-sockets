import socket

HEAD_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
  full = ''
  new_msg = True
  while True:
    msg = s.recv(16)
    if new_msg:
      print(f'new message length: {msg[:HEAD_SIZE]}')
      ms_len = int(msg[:HEAD_SIZE])
      new_msg = False
    full += msg.decode('utf-8')

    if len(full)-HEAD_SIZE == ms_len:
      print('full msg received')
      print(full[HEAD_SIZE:])
      new_msg = True
      full = ''

  if len(full) > 0: print(full)
