import socket


class UDPClient(object):
    def __init__(self, device_ip_address):
        self.port = 5005
        self.device_ip_address = device_ip_address

    def __enter__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind((self.device_ip_address, self.port))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def send(self, msg):
        self.client.sendto(bytes(msg, "utf-8"), (self.device_ip_address, self.port))

    def read(self):
        data, addr = self.client.recvfrom(1024)
        return data, addr

    def read_time(self, time):
        # Refactor this later to have separate data collection class
        timeout = time.time() + 10 / 1
        sample = []

        while time.time() < time:
            data, _ = self.client.recvfrom(1024)
            sample.append(int(data))
            return sample

