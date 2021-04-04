import socket
import csv
import time


UDP_IP = "192.168.0.19"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

timeout = time.time() + 10/1
sample = []


while True:
	test = 0
	if test == 5 or time.time() > timeout:
		break
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print("received message: %s" % data)
	sample.append(int(data))
	time.sleep(0.02)
	print(data)


with open('AD8232_data.csv', mode='w') as data_file:
		writer = csv.writer(data_file, delimiter=',')
		writer.writerow(sample)
		data_file.close()
		
