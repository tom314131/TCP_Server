import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# create TCP ipv4 socket
dest_ip = '192.168.1.48'								# set ip
dest_port = 12345										# set port
s.connect((dest_ip, dest_port))							# connect to params with socket

msg = raw_input("Message to send: ")
while not msg == 'quit':								# if msg is not quit
	s.send(msg)											# send message
	data = s.recv(4096)									# receive data
	print "Server sent: ", data
	msg = raw_input("Message to send: ")
s.close()
