# Embedded_ML
Optional: 
Initialise virtual python env.
 
```bash
conda create -n EmbeddedML_env python=3.8.5
conda activate EmbeddedML_env
pip install requirements.txt
```

#TBD - Initialise system environment variables over a bash script.

Initialise data transmisison : 
```bash
ifconfig
```
Will output network interface configuration. Use the ip the python scripts will be run off.

![image](https://user-images.githubusercontent.com/39244927/113598037-75938500-9634-11eb-8b80-bf54e8dd47ee.png)

In this case, the UDP server going to be run off is 192.168.0.19


Using Arduino IDE, edit the right values of WifiUDPClient.ino to connect to wifi and input own IP.

![image](https://user-images.githubusercontent.com/39244927/113598676-66f99d80-9635-11eb-9ce7-0216922b556c.png)

Install ESP32 arduino program 


Apply same changes in ECG_sample_get.py

![image](https://user-images.githubusercontent.com/39244927/113598824-a1fbd100-9635-11eb-9b4a-c4c4651132dc.png)


Place ECG electrodes.
![ECG Placement](https://user-images.githubusercontent.com/39244927/113597321-71b33300-9633-11eb-9fbe-8872a5d8d0fa.png) Image from ConnectMed.com


Gather a sample of data with python script
```bash
python ECG_sample_get.py
```
Example output

![image](https://user-images.githubusercontent.com/39244927/113598996-e38c7c00-9635-11eb-93a2-0f7b86773d94.png)


To generate model : 
```bash
python model_gen.py
```
This script will produce 2 files, sine_model_quantized.tflite  and  sine_model.h.

sine_model.h to be used with Arduino IDE as header file. 

To compile using Arduino IDE
Library : EloquentTinyML


Example output. Predicting sine value with x input.

![image](https://user-images.githubusercontent.com/39244927/113181209-6d5cd380-9249-11eb-8cb8-d765fd49bd2b.png)




Heart sensor schematic.

![image](Datasheets/Schematic_Heartmonitor.png)

Current heart sample output

![img](ECG_sample_good.png)

Current feature extraction output

![img](ECG_feature_extraction_current.png)
