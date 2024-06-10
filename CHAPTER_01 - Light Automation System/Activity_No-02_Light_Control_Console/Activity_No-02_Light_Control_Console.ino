int ledPin = D2;

void setup() 
{
  // Initialize serial communication
  Serial.begin(9600);

  // Set LED pin as output
  pinMode(ledPin, OUTPUT);
}


void loop() {
  if (Serial.available()) 
{
    char command = Serial.read(); // Check the command received from Serial Monitor
    if (command == '1') 
  {
      digitalWrite(ledPin, HIGH);   // Turn on the LED
      Serial.println("LED ON");
   } 
else if (command == '0') {
      digitalWrite(ledPin, LOW);    // Turn off the LED
      Serial.println("LED OFF");
    }
  }
}

