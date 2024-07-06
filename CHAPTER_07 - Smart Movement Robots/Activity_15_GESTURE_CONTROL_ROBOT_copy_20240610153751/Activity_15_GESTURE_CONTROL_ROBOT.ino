// Define the pins for the motor control
const int motor1Pin1 = D1; // Motor 1 input 1 (GPIO5)
const int motor1Pin2 = D2; // Motor 1 input 2 (GPIO4)
const int motor2Pin1 = D5; // Motor 2 input 1 (GPIO14)
const int motor2Pin2 = D6; // Motor 2 input 2 (GPIO12)

void setup() {
  // Set the motor control pins as outputs
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);

  // Start serial communication
  Serial.begin(9600);
  Serial.println("Send commands to control the robot:");
  Serial.println("'w' to move forward");
  Serial.println("'s' to move backward");
  Serial.println("'a' to turn left");
  Serial.println("'d' to turn right");
  Serial.println("'x' to stop");
}

void loop() {
  // Check if data is available in the serial buffer
  if (Serial.available() > 0) {
    // Read the command from the serial buffer
    char command = Serial.read();

    // Execute the command based on the key received
    switch (command) {
      case 'w': // Move forward
        // Set both motors to move forward
        digitalWrite(motor1Pin1, HIGH);
        digitalWrite(motor1Pin2, LOW);
        digitalWrite(motor2Pin1, HIGH);
        digitalWrite(motor2Pin2, LOW);
        Serial.println("Moving forward");
        break;
      case 's': // Move backward
        // Set both motors to move backward
        digitalWrite(motor1Pin1, LOW);
        digitalWrite(motor1Pin2, HIGH);
        digitalWrite(motor2Pin1, LOW);
        digitalWrite(motor2Pin2, HIGH);
        Serial.println("Moving backward");
        break;
      case 'a': // Turn left
        // Set motor 1 to move backward and motor 2 to move forward
        digitalWrite(motor1Pin1, LOW);
        digitalWrite(motor1Pin2, HIGH);
        digitalWrite(motor2Pin1, HIGH);
        digitalWrite(motor2Pin2, LOW);
        Serial.println("Turning left");
        break;
      case 'd': // Turn right
        // Set motor 1 to move forward and motor 2 to move backward
        digitalWrite(motor1Pin1, HIGH);
        digitalWrite(motor1Pin2, LOW);
        digitalWrite(motor2Pin1, LOW);
        digitalWrite(motor2Pin2, HIGH);
        Serial.println("Turning right");
        break;
      case 'x': // Stop the motors
        // Stop both motors
        digitalWrite(motor1Pin1, LOW);
        digitalWrite(motor1Pin2, LOW);
        digitalWrite(motor2Pin1, LOW);
        digitalWrite(motor2Pin2, LOW);
        Serial.println("Stopping motors");
        break;
      default:
        Serial.println("Unknown command");
        break;
    }
  }
}
