/*
 *  This sketch sends random data over udp on a ESP32 device
 *
 */
#include <WiFi.h>

#include <WiFiUdp.h>

// WiFi network name and password:
const char * networkName = "VM7528515";
const char * networkPswd = "Sg6phqthjnhc";

//IP address to send udp data to:
// either use the ip address of the server or 
// a network broadcast address
const char * udpAddress = "192.168.0.19";
const int udpPort = 5005;

//Are we currently connected?
boolean connected = false;

char packetBuffer[255]; //buffer to hold incoming packet
char ReplyBuffer[] = "acknowledged"; // a string to send back

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

    // if there's data available, read a packet

    int packetSize = udp.parsePacket();

    if (packetSize) {

        Serial.print("Received packet of size ");
        Serial.println(packetSize);
        Serial.print("From ");
        IPAddress remoteIp = udp.remoteIP();
        Serial.print(remoteIp);
        Serial.print(", port ");
        Serial.println(udp.remotePort());

        // read the packet into packetBufffer
        int len = udp.read(packetBuffer, 255);
        if (len > 0) {
            packetBuffer[len] = 0;

        }

        Serial.println("Contents:");
        Serial.println(packetBuffer);

        // send a reply, to the IP address and port that sent us the packet we received

        udp.beginPacket(udp.remoteIP(), udp.remotePort());
        udp.printf("%lu", ReplyBuffer);
        udp.endPacket();

        char Setting = * packetBuffer;

        switch (Setting) {

        case 't': //Test mode, serial mode

            for (int i = 0; i < 1000; i++) {

                if ((digitalRead(32) == 1) || (digitalRead(35) == 1)) {
                    Serial.println('!');
                } else {

                    Serial.println(analogRead(33));
                    delay(1);
                }
            }
            break;

        case 's': //Sample mode, sends over UDP. Stores. 
            Serial.println("Sample mode");
            if (connected) {
                //Send a packet
            for (int i = 0; i < 5500; i++) {
                if ((digitalRead(32) == 1) || (digitalRead(35) == 1)) {
                    Serial.println('!');
                } else {

                    udp.beginPacket(udpAddress, udpPort);
                    udp.printf("%lu", analogRead(33));
                    udp.endPacket();
                    delay(1);
                }

            }
            //Wait for 1 second
            
        }

        break;

        case 'm': //Machine Learning mode
        Serial.println("ML Mode");
        udp.beginPacket(udp.remoteIP(), udp.remotePort());
        udp.printf("ML Mode");
        udp.endPacket();
        break;
    }

}
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
        //initializes the udp state
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
