#!/bin/bash
# Bash script to initialise a generic ESP32 system with network and webrepl on bootloader.

echo Starting...
echo Nev\'s ESP32 initialisation script. v0.1
echo This script will erase your system\'s flash and upload new firmware and bootloader.

read -p "Do you want to proceed? (y/n) " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then


echo Installing PySerial...
pip install pyserial
echo -en "\e[38;5;2m ESPTOOL installed \e[m \n"


echo Installing ESPTool...
pip install esptool
echo -en "\e[38;5;2m ESPTOOL installed \e[m \n"


echo Flashing ESP32...
esptool.py --port /dev/ttyUSB0 erase_flash
echo -en "\e[38;5;2m ESP32 flashed \e[m \n" 

echo Getting micropython firmware... 
wget https://micropython.org/resources/firmware/esp32-idf4-20210202-v1.14.bin
echo -en "\e[38;5;2m Firmware aquired \e[m \n"

echo Flashing firmware into ESP32...
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-idf4-20210202-v1.14.bin
echo -en "\e[38;5;2m Firmware flashed! \e[m \n"

echo Installing ampy
pip install --user adafruit-ampy
echo -en "\e[38;5;2m ampy installed \e[m \n"

echo Initialising network parameters
echo "ESSID: \n"
read ESSID
echo "Password: \n"
read PASSWORD

sed -i 's/ESSID/'${ESSID}'/' ./ESP32/boot.py
sed -i 's/PASSWORD/'${PASSWORD}'/' ./ESP32/boot.py

echo installing custom boot.py
ampy put ./ESP32/boot.py
echo -en "\e[38;5;2m boot.py installed \e[m \n"

fi

rm ./esp32-idf4-20210202-v1.14.bin

#Set .ampy config here
echo Quitting...
