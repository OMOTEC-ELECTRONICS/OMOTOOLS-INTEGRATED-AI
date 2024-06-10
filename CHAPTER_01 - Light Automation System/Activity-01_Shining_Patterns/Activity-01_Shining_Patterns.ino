int LED = D5;    // Pin connected to the LED

void setup() 
{
  pinMode(LED, OUTPUT);  // Set the LED pin as an output
}

void loop() 
{
  digitalWrite(LED,HIGH);  // Turn on the LED
  delay(1000);            // Wait for 1 second

  digitalWrite(LED, LOW);    // Turn off the LED
  delay(1000);                 // Wait for 1 second
}

