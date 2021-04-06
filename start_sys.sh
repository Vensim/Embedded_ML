#!/bin/bash
# Bash script to start system.

echo Starting...
echo Embedded to ML. v0.1
echo "This script will set local system configurations,"
echo "gather ECG sample data sent by ESP32 over UDP and apply data processing " 

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

echo "UDP Address : (eg. 192.168.0.10)"
read ADDRESS

#Figure quotation on bash

echo Updating Arduino file.
sed -i 's/ESSID/'${ESSID}'/' ./ESP32/ESP32.ino
sed -i 's/PASSWORD/'${PASSWORD}'/' ./ESP32/ESP32.ino
sed -i 's/UDPAddress/'${ADDRESS}'/' ./ESP32/ESP32.ino
echo Updating Python files.
sed -i 's/UDPAddress/'${ADDRESS}'/' ./ESP32-ECG_w_UDP_sample_get.py

echo "Open the ESP32.ino arduino file and compile the updated file."
read -p "Press Y when you are ready to proceed (y/n)" -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then

echo Proceeding...

fi

echo "Running sampling script: ESP32-ECG_w_UDP_sample_get.py"
python ./ESP32-ECG_w_UDP_sample_get.py

echo "Running feature extraction script : ECG_feature_extraction.py"
python ./ECG_feature_extraction.py

echo "Visualisation of feature extraction"
python ./Visualise_ECG_features.py

echo "Running machine learning module"
python ./model_gen.py
echo -e "2 files should be generated on output: /n sine /n sine2"
#sed -i 's/^networkName=.*/networkName="${ESSID}"/' ./file.txt
#sed -i 's/^networkPswd=.*/networkPswd="${PASSWORD}"/' ./file.txt

echo Quitting...

