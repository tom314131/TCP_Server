import socket, threading, os

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)						# create TCP ipv4 socket
server_ip='0.0.0.0'																# set ip
server_port=12345																# set port
server.bind((server_ip,server_port))											# bind socket with params
server.listen(5)																# start listening - can take care of 5 client at the same time

while True:
	client_socket,client_address=server.accept()								# accept connection tries
	print 'Connection from:',client_address
	data=client_socket.recv(1024)												# receive data from client
	commandReady = False
	while not data =="ended":													
		if not commandReady:
			fullpath=""
			if "\n" in data:
				commandReady = True												#the request is finished by \n and we are ready to carry it out
				path = data.split(" ")[1]										#take rellevant part of request which is the message
				if path == "/":
					path="/index.html"
				fullpath="files"+path											#add directory files to the path in order to access the file
				if path == "/redirect":											
					client_socket.send("HTTP/1.1 301 Moved Permanently\n")
					client_socket.send("Connection: close\n")
					client_socket.send("Location: /result.html\n\n")
					
				if os.path.isfile(fullpath):
					client_socket.send("HTTP/1.1 200 OK\n")
					client_socket.send("Connection: close\n\n")
					
					ending=path.split(".")[1]
					file=""
					
					if ending == "jpg" or ending=="ico":
						file = open(fullpath,'rb')	
					else:
						file = open(fullpath,'r')	
						
					buffer=file.read(1024)
					while(buffer):
						client_socket.send(buffer)
						buffer=file.read(1024)
				else:
					client_socket.send("HTTP/1.1 404 Not Found\n")
					client_socket.send("Connection: close\n\n")

				print data[0:data.find('\n')]

		if "\r\n\r\n" in data:													#if the client finished with his request
			commandReady=False													#we do not carry out anithing anymore
			data=""
			print 'Client disconnected'
			client_socket.close()												#close the socket
			data="ended"
			
		else:
			data += client_socket.recv(1024)
