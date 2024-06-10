// main.ino
#include <ESP8266WiFi.h>
#include "code.h"

const char *ssid = "Omo_Backup"; //change it
const char *password = "Omotec#909";//change it

const int ledPin = D2;

ESP8266WebServer server(80);

void setup() {
Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
    WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
 Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.on("/", HTTP_GET, handleRoot);
  server.on("/led", HTTP_GET, handleLED);
 
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
   server.handleClient();
}

void handleRoot() {
  server.send(200, "text/html", htmlContent);
}

void handleLED() {
  String state = server.arg("state");
  if (state == "on") {
    digitalWrite(ledPin, HIGH);
    Serial.print("on");
  } else {
    digitalWrite(ledPin, LOW);
     Serial.print("off");
     
  }
  server.send(200, "text/plain", "OK");
}
