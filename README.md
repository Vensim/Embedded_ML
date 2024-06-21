# Embedded ML for ECG applications
[![pipeline status](https://gitlab.com/Sesven/Embedded_ML/badges/main/pipeline.svg)](https://gitlab.com/Sesven/Embedded_ML/-/commits/main)
## Introduction

> Objective of this repository is to acquire experience in developing products and to get familiar with new technologies. Secondary objective is to create a framework of sensor to machine learning starting with raw electrocardiogram data with the intent of quantize how deviated the heart wave is from sample data and in addition to predict future heart states with different activities. In the future different sensors could be applied such as electromyography sensors.

Server-runner added.


![ECG Features](ECG_feature_extraction_current.png)

![Fourier](Fourier_output.png)

![ML Prediction](https://user-images.githubusercontent.com/39244927/113791372-60554e00-973b-11eb-96e5-5e616ea720b7.png)



<img src="https://user-images.githubusercontent.com/39244927/113945275-edf97200-97fd-11eb-8a9f-ba0aee1ba3b5.png" width="300" height="400">


## Current progress

Goal | Progress
------------ | -------------
ECG to ESP data aquisition | Y
ESP UDP control | Y
ESP UDP data transmission | Y
Feature extraction | Basic
Machine Learning model | In progress
ESP Prediction | In progress

Analog input produces 50~ Hertz noise, research into implementing Low-pass filter

Implement windowing to individual heart pulses for additional feature extraction

Find way to change Machine Learning model, the hex array, without recompiling whole program. 


## Installation

Optional: 
Initialise virtual python env.
 
```bash
conda create -n EmbeddedML_env python=3.8.5
conda activate EmbeddedML_env
pip install requirements.txt
```


Initialise system variables with bash script. This will give prompt for ESSID, Password and UDP IP configurations.
```bash
chmod +x env_init.sh
./env_init.sh
```
Or edit the script files and the ESP32.ino file manually.

Will output network interface configuration. Use the ip the python scripts will be run off.


Install the ESP32 arduino program with new initialised values. 


Place ECG electrodes.

Image from ConnectMed.com
<img src="https://user-images.githubusercontent.com/39244927/113597321-71b33300-9633-11eb-9fbe-8872a5d8d0fa.png" width="500" height="500">


Test the output of the ECG sensor in a serial monitor.
```bash
python UDP_init_test_mode.py
```

Gather sample data. Enable sampling server then initialise sampling.
```bash
python ECG_sampling_server.py
python UDP_init_sample_mode.py
```
Example output

![img](ECG_sample_good.png)



With sampled data, perform feature extraction
```bash
python ECG_feature_extraction.py
python Visualise_ECG_features.py # Optional, to visualise the output.
```

Feature extraction example output.

![img](ECG_feature_extraction_current.png)



To generate model with featured data 
```bash
python ECG_ML_Modelgen.py
```
This script will produce 2 files, ECG_model_quantized.tflite  and  ECG_ML_Model.h.

ECG_ML_Model.h to be used with Arduino IDE as header file.

Recompile the ESP32 with the new header file and activate Machine Learning mode
```bash
python UDP_init_ML_mode.py
```
Expected output
![image](https://user-images.githubusercontent.com/39244927/113791372-60554e00-973b-11eb-96e5-5e616ea720b7.png)



Heart sensor schematic.

![image](Datasheets/Schematic_Heartmonitor.png)


