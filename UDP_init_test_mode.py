import socket

UDP_IP_CLIENT = "UDPAddress"
UDP_PORT = 5005
MESSAGE = "t"
client = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


client.sendto(bytes(MESSAGE, "utf-8"),(UDP_IP_CLIENT, UDP_PORT))

