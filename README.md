# Embedded_ML
Python requirements:

CMAKE version => 3.11
tensorflow
tinyML

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

