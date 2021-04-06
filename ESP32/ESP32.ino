/*
 *  This sketch sends random data over UDP on a ESP32 device
 *
 */
#include <WiFi.h>

#include <WiFiUdp.h>

// WiFi network name and password:
const char * networkName = "VM7528515";
const char * networkPswd = "Sg6phqthjnhc";

//IP address to send UDP data to:
// either use the ip address of the server or 
// a network broadcast address
const char * udpAddress = "192.168.0.19";
const int udpPort = 5005;

//Are we currently connected?
boolean connected = false;

WiFiUDP udp;

void setup() {
  // Initilize hardware serial:
  Serial.begin(115200);

  pinMode(32, INPUT); // Setup for leads off detection LO +
  pinMode(35, INPUT); // Setup for leads off detection LO -
  //Connect to the WiFi network
  connectToWiFi(networkName, networkPswd);
}

void loop() {




//only send data when connected
  if (connected) {
    //Send a packet

    if ((digitalRead(32) == 1) || (digitalRead(35) == 1)) {
      Serial.println('!');
    } else {

      udp.beginPacket(udpAddress, udpPort);
      udp.printf("%lu", analogRead(33));
      udp.endPacket();
    }
  }
  //Wait for 1 second
  delay(1);
}

void connectToWiFi(const char * ssid,
  const char * pwd) {
  Serial.println("Connecting to WiFi network: " + String(ssid));

  // delete old config
  WiFi.disconnect(true);
  //register event handler
  WiFi.onEvent(WiFiEvent);

  //Initiate connection
  WiFi.begin(ssid, pwd);

  Serial.println("Waiting for WIFI connection...");
}

//wifi event handler
void WiFiEvent(WiFiEvent_t event) {
  switch (event) {
  case SYSTEM_EVENT_STA_GOT_IP:
    //When connected set 
    Serial.print("WiFi connected! IP address: ");
    Serial.println(WiFi.localIP());
    //initializes the UDP state
    //This initializes the transfer buffer
    udp.begin(WiFi.localIP(), udpPort);
    connected = true;
    break;
  case SYSTEM_EVENT_STA_DISCONNECTED:
    Serial.println("WiFi lost connection");
    connected = false;
    break;
  default:
    break;
  }
}