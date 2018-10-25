import socket
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=9999


uname=input('enter the username:')
ip=input('enter the ip address::')
s.connect((ip,port))
s.send(uname.encode('ascii'))
def receiveMsg(sock):
	while True:
		msg=sock.recv(1024).decode('ascii')
		print(msg)


threading.Thread(target=receiveMsg,args=(s,)).start()


while True:
	tempMsg=input()
	msg=uname+'>>'+tempMsg
	s.send(msg.encode('ascii'))