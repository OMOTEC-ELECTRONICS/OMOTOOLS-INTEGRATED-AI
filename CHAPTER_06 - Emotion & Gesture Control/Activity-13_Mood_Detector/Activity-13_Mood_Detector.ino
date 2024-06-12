int greenLedPin = 2;


void setup() {
  pinMode(greenLedPin, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(greenLedPin, HIGH);  // Turn green LED on
          
    } else if (command == '0') {
      digitalWrite(greenLedPin, LOW);   // Turn green LED off
       
    }
  }
}
