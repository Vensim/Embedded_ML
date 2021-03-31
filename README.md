# Embedded_ML
Optional: 
Initialise virtual python env.
 
```bash
conda create -n EmbeddedML_env python=3.8.5
conda activate EmbeddedML_env
pip install requirements.txt
```

Bash requirements:

xxd - to create hexdump of ml model.

To generate model : 
```bash
python model_gen.py
```
Conversion to hex file
```bash
xxd -i sine_model_quantized.tflite > sine_model.cc
```

To compile using Arduino IDE
Library : EloquentTinyML


Example output. Predicting sine value with x input.
![image](https://user-images.githubusercontent.com/39244927/113181209-6d5cd380-9249-11eb-8cb8-d765fd49bd2b.png)
