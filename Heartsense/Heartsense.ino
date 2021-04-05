// ECG Sensor test

void setup() {

  Serial.begin(9600);
  pinMode(32, INPUT); // Setup for leads off detection LO +
  pinMode(35, INPUT); // Setup for leads off detection LO -

}

void loop() {

  if ((digitalRead(32) == 1) || (digitalRead(35) == 1)) {
    Serial.println('!');
  } else {

    Serial.println(analogRead(33));

  }
}
