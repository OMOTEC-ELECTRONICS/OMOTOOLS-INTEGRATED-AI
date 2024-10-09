// main.ino
#include <ESP8266WiFi.h>
#include "C:\Users\OMOLP085\Documents\Arduino\NAMEPICKER\code.h"
const char *ssid = "OMOTECH_2.4GHz"; //change it
const char *password = "Omotech@23";//change it

const int In1 = D1; //In1 pin of motor
const int In2 = D2; //In2 pin of motor

ESP8266WebServer server(80);

  void setup() {
  Serial.begin(9600);
  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);

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
  server.on("/motor", HTTP_GET, handlemotor);
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}
void handleRoot() {
  server.send(200, "text/html", htmlContent);
}

void handlemotor() {
  String state = server.arg("state");
  if (state == "on") 
  {
  digitalWrite(In1, HIGH);
  digitalWrite(In2, LOW);
  Serial.print("on");
  } 
else 
{
digitalWrite(In1, LOW);
digitalWrite(In2, LOW);
Serial.print("off");
}
server.send(200, "text/plain", "OK");
}