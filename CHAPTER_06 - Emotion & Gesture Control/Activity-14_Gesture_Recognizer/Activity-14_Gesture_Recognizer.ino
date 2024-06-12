Int LED = D2;
void setup() {
  Serial.begin(9600); // Initialize serial communication
pinMode (LED, OUTPUT);
}

void loop() {

  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the command from serial
    if (command == 'H') {
      // Perform action for "Hi" gesture
      Serial.println("Received command: Hi");
   digitalWrite (LED, HIGH);
    } else if (command == 'N') {
      // Perform action for "Namaste" gesture
      Serial.println("Received command: Namaste");
  digitalWrite (LED, HIGH);
    } else {
      // Unknown command
      Serial.println("Unknown command received");
  digitalWrite (LED, LOW);
    }
  }
}
