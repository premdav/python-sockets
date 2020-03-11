import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full = ''
while True:
  msg = s.recv(8)
  if len(msg) <= 0:
    break
  full += msg.decode('utf-8')

if len(full) > 0: print(full)
