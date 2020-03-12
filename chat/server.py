import socket
import select

HEAD_LEN = 10
IP = '127.0.0.1'
PORT = 1234

serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serve_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serve_socket.bind((IP, PORT))

serve_socket.listen()

s_list = [serve_socket]

clients = {}

def receive_msg(client_sock):
  try:
    msg_head = client_sock.recv(HEAD_LEN)
    if not len(msg_head): return False
    msg_len = int(msg_head.decode('utf-8').strip())
    return { 'header': msg_head, 'data': client_sock.recv(msg_len) }
  except:
    return False

while True:
  read_sock, _, except_sock = select.select(s_list, [], s_list)
  
  for noti_sock in read_sock:
    if noti_sock == serve_socket:
      c_sock, c_addr = serve_socket.accept()

      user = receive_msg(c_sock)
      if user is False:
        continue
      s_list.append(c_sock)
      clients[c_sock] = user
      print(f"accepted new connection from {c_addr[0]}:{c_addr[1]}, username: {user['data'].decode('utf-8')}")
    else:
      msg = receive_msg(noti_sock)
      if msg is False:
        print(f"Closed connection from {clients[noti_sock]['data'].decode('utf-8')}")
        s_list.remove(noti_sock)
        del clients[noti_sock]
        continue
      user = clients[noti_sock]
      print(f"Received message from {user['data'].decode('utf-8')}: {msg['data'].decode('utf-8')}")

      for cl_so in clients:
        if cl_so != noti_sock:
          cl_so.send(user['header'] + user['data'] + msg['header'] + msg['data'])
  
  for noti_sock in except_sock:
    s_list.remove(noti_sock)
    del clients[noti_sock]
