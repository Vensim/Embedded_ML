#include <EloquentTinyML.h>
// sine_model.h contains the array you exported from the previous step
// withhttps://dl.espressif.com/dl/package_esp32_index.json, http://arduino.esp8266.com/stable/package_esp8266com_index.json either xxd or tinymlgen
#include "sine_model.h"

#define NUMBER_OF_INPUTS 1
#define NUMBER_OF_OUTPUTS 1
// in future projects you may need to tweak this value.
// it's a trial and error process
#define TENSOR_ARENA_SIZE 5*1024

Eloquent::TinyML::TfLite<NUMBER_OF_INPUTS, NUMBER_OF_OUTPUTS, TENSOR_ARENA_SIZE> ml;

void setup() {
    Serial.begin(115200);
    ml.begin(model_data);
}

void loop() {
    // pick up a random x and predict its sine
    float x = 3.14 * random(100) / 100;
    float y = sin(x);
    float input[1] = { x };
    float predicted = ml.predict(input);

    Serial.print("sin(");
    Serial.print(x);
    Serial.print(") = ");
    Serial.print(y);
    Serial.print("\t predicted: ");
    Serial.println(predicted);
    delay(1000);
}
