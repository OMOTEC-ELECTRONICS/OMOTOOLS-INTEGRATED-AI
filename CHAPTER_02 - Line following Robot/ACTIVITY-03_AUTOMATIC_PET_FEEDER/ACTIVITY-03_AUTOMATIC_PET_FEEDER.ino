#include <Servo.h>

#define SERVO_PIN D4  // Pin connected to servo motor
#define IR_PIN D7     // Pin connected to IR sensor
#define SERVO_OPEN_ANGLE 90  // Angle to open the servo
#define IR_THRESHOLD 800     // Threshold for detecting an object with IR sensor

Servo servoMotor;

void setup() {
  Serial.begin(9600);
  servoMotor.attach(SERVO_PIN);
  pinMode(IR_PIN, INPUT);
}
void loop() {
  if (isPetNear()) {
    Serial.println("Pet detected. Feeding...");
    servoMotor.write(SERVO_OPEN_ANGLE); // Open the feeder
  } else {
    Serial.println("No pet detected.");
    // You can optionally close the servo when the pet is not detected
    // servoMotor.write(SERVO_CLOSE_ANGLE);  }
  delay(100); // Delay between sensor checks
bool isPetNear() {
  int irValue = analogRead(IR_PIN);
  return irValue < IR_THRESHOLD; // Returns true if an object (pet) is near, false otherwise
}
