
import socket
import threading



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect(("8.8.8.8", 80))

serverRunning = True
host_name = socket.gethostname()
#ip = socket.gethostbyname(host_name)
port = 10001

#ip = str(s.getsockname()[0])
ip = "192.168.43.149"
#s.close()

#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


clients ={}
s.bind((ip,port))
s.listen(5)


print('server is ready..')
print('Ip address of the server::%s'%ip)
def handleClient(client,uname):
	clientConnected=True
	keys=clients.keys()
	help='There are four command in Messenger\n1::#chatlist=>Give the list of people online\n2::#help=>Tell about some of the commands\n3::#broadcast=>This command is used to send the message to all connected users\n4::#quit=>Used to logged out.'



	while clientConnected:
		try:
			msg=client.recv(1024).decode('ascii')
			response='Number of People online\n'
			found=False
			if '#chatlist' in msg:
				clientNo=0
				for name in keys:
					clientNo += 1
					response=response + str(clientNo) +'::' +name+'\n'
				client.send(response.encode('ascii'))
			elif '#help' in msg:
				client.send(help.encode('ascii'))
			elif '#broadcast' in msg:
				msg=msg.replace('#broadcast','')
				for k,v in clients.items():
					v.send(msg.encode('ascii'))
			elif '#quit' in msg:
				response='Stopping Session and exiting....'
				client.send(response.encode('ascii'))
				clients.pop(uname)
				print(uname + '  logged out')
				clientConnected=False
			else:
				temp = msg
				for name in keys:
					temp = temp.replace('#'+name, '')

				for name in keys:
					if('#'+name) in msg:
						clients.get(name).send(temp.encode('ascii'))
						found=True
				if(not found):
					client.send('Trying to send message to invalid person.'.encode('ascii'))

		except:
			clients.pop(uname)
			print(uname +' has been logged out')
			clientConnected=False



while serverRunning:
	client, address=s.accept()
	uname=client.recv(1024).decode('ascii')
	print('%s connected to the server'%str(uname))
	client.send('welcome to messenger.For help enter #help.'.encode('ascii'))



	if(client not in clients):
		clients[uname]=client
		threading.Thread(target=handleClient,args=(client,uname)).start()



