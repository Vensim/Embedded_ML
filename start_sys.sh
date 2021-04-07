#!/bin/bash
# Bash script to start system.

echo Starting...
echo Embedded to ML. v0.1
echo "This script will set local system configurations to"
echo "gather ECG sample data sent by ESP32 over UDP and apply data processing" 

echo Configuration...
echo "Setting for ESP32 network parameters: /n"
echo "ESSID: "
read ESSID
echo "Password: "
read PASSWORD

echo Setting UDP values
read -p "Do you want 'ipconfig' to run to find local ip? (y/n)" -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then

ifconfig

fi

echo "UDP Receiver Address(From ESP32) : (eg. 192.168.0.10)"
read ADDRESS

echo "UDP Sender Address(To ESP32) : (eg. 192.168.0.20)"
read ADDRESS_SEND
#Figure quotation on bash

echo Updating Arduino file.
sed -i 's/ESSID/'${ESSID}'/' ./ESP32/ESP32.ino
sed -i 's/PASSWORD/'${PASSWORD}'/' ./ESP32/ESP32.ino
sed -i 's/UDPAddress/'${ADDRESS}'/' ./ESP32/ESP32.ino
echo Updating Python files.
sed -i 's/UDPAddress/'${ADDRESS}'/' ./ECG_sampling_server.py
sed -i 's/UDPAddress/'${ADDRESS_SEND}'/' ./UDP_init_ML_mode.py
sed -i 's/UDPAddress/'${ADDRESS_SEND}'/' ./UDP_init_sample.mode.py
sed -i 's/UDPAddress/'${ADDRESS_SEND}'/' ./UDP_init_test_mode.py

echo END OF CONFIGURATION
echo "Open the ESP32.ino arduino file and compile the updated file."

read -p "Press any button to proceed..." -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then

echo Proceeding...

fi

echo "Open the sampling server, ECG_sampling_server.py, in a seperate terminal"
read -p "Press any button to proceed..." -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then

echo Proceeding...

fi


echo "Running feature extraction script : ECG_feature_extraction.py"
python ./ECG_feature_extraction.py

echo "Visualisation of feature extraction"
python ./Visualise_ECG_features.py

echo "Running machine learning module"
python ./model_gen.py
#sed -i 's/^networkName=.*/networkName="${ESSID}"/' ./file.txt
#sed -i 's/^networkPswd=.*/networkPswd="${PASSWORD}"/' ./file.txt


echo Quitting...

