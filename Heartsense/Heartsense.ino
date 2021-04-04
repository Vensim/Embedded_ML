

#define LED 2
  int val = 0;
void setup() {
  // put your setup code here, to run once:
  
Serial.begin(9600);
  pinMode(LED, OUTPUT); // GPIO 2 led
  pinMode(32, INPUT); // Setup for leads off detection LO +
  pinMode(35, INPUT); // Setup for leads off detection LO -

}

void loop() {

  digitalWrite(LED, HIGH);
  delay(1000);
  digitalWrite(LED, LOW);

  while(Serial.available()) {

    

  if((digitalRead(32) == 1)||(digitalRead(35) == 1)){
    Serial.println('!');
  }
  else{
    // send the value of analog input 0:
    val = analogRead(33);
      Serial.print(val);
    }
  }
}
