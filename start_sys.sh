#!/bin/bash
# Bash script to start system.

echo Starting...
echo Embedded to ML. v0.1
echo "This script will set local system configurations to"
echo "gather ECG sample data sent by ESP32 over UDP and apply data processing" 


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

