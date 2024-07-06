#include <Servo.h>

Servo servoMotor;

void setup() {
  servoMotor.attach(16); // Attach servo to pin D0
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      servoMotor.write(0); // Move servo clockwise
    } else if (command == '0') {
      servoMotor.write(180); // Move servo anticlockwise
    }
  }
}

