#!/bin/bash
# Bash script to initialise a generic ESP32 system

echo Starting...
echo Installing ESPTool...
pip3 install esptool
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
pip3 install --user adafruit-ampy
echo -en "\e[38;5;2m ampy installed \e[m \n"

echo installing custom boot.py
ampy put ./ESP32/boot.py
echo -en "\e[38;5;2m boot.py installed \e[m \n"

#Set .ampy config here
echo Quitting...
