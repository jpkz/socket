import threading
from socket import socket,AF_INET,SOCK_STREAM
ADDR=('',1234)
BUFSIZ=1024
tcp_server_sock=socket()
tcp_server_sock.bind(ADDR)
tcp_server_sock.listen()
def handle(sock,addr):
	while True:
		data=socke.recv(BUFSIZ).decode()
		if not data:
			sock.close()
			break
		print('recevide message:{}'.format(data))
		sock.send('[{}{}'.format('hello kitty',data).encode())
	sock.close()
	print('{}closed'.format(addr))
def main():
	print('waiting for client to conn...')
	while True:
		try:
			tcp_extension_sock,addr=tcp_server_sock.accept()
		except KeyboardInterrupt:
			break
		t=threading.Thread(target=handle,args=(tcp_extension_sock,addr))
		t.start()
	print('\nExit')
	tcp_server_sock.close()
if __name__=='__main__':
	main()
