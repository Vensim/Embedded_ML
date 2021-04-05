# Embedded_ML
Optional: 
Initialise virtual python env.
 
```bash
conda create -n EmbeddedML_env python=3.8.5
conda activate EmbeddedML_env
pip install requirements.txt
```


Initialise esp32. Downloads esptool, micropython firmware and flashes. 
```bash
python esp32_init.sh
```


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




Heart sensor schematic. ![image](Datasheets/Schematic_Heartmonitor.png)

Current heart sample output
![img](ECG_sample_good.png)
