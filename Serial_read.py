#https://techtutorialsx.com/2017/12/02/esp32-esp8266-arduino-serial-communication-with-python/
#https://pyserial.readthedocs.io/en/latest/shortintro.html
import serial
import io
import struct

ser = serial.Serial("/dev/ttyUSB0",
                    baudrate=9600,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_ODD,
                    timeout = 1
)


def Initialize():
	global ser
	try:
		ser.write(b's')
		ser.flush()
		ser.isOpen()
		print("\n Serial is open")
	except: 
	        print ("Error: serial Not Open")

def Reader():
	global ser
	if (ser.isOpen()):
		try:
			x = ser.read(4)
#			print(type(x))
#			x = x.decode()
			return x
		except:
			return "unable to print"
		else:
			return "cannot open serial port"


Initialize()
while True:
	print(Reader())
