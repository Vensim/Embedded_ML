import socket

UDP_IP_CLIENT = "192.168.0.26"
UPD_IP_SERVER = "192.168.0.19"
UDP_PORT = 5005
MESSAGE = "m"
client = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
server = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

client.sendto(bytes(MESSAGE, "utf-8"),(UDP_IP_CLIENT, UDP_PORT))
sock.bind((UDP_IP, UDP_PORT))

Test = 0

while True:
	Test = 0
	
	if test >= 1: # or time.time() > timeout:
		break
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print("received message: %s" % data)
	test += 1
