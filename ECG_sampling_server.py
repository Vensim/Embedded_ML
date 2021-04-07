import socket
import csv
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

UDP_IP = "UDPAddress"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

timeout = time.time() + 10/1
sample = []

test = 0
while True:

	if test >= 5000: # or time.time() > timeout:
		break
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print("received message: %s" % data)
	sample.append(int(data))
	print(data)
	test += 1
	print(test)




with open('AD8232_data.csv', mode='w') as data_file:
		writer = csv.writer(data_file, delimiter=',')
		writer.writerow(sample)
		data_file.close()
		
#Plotting sample data
t = np.arange(0.0, 5000.0, 1.0)

sample_array = np.array(sample)
print(sample_array)
print(t)
fig, ECG = plt.subplots()
ECG.plot(t, sample_array)

ECG.set(xlabel='samples (s)', ylabel='Analog',
       title='Analog data over samples')

ECG.grid()

fig.savefig("ECG_sample.png")
plt.show()

