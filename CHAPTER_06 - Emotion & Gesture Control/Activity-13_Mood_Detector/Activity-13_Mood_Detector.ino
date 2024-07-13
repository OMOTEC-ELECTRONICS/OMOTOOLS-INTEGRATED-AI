
int LedPin = D2; //Initialize the LED pin


void setup() {
  pinMode(LedPin, OUTPUT); //Set the mode of the LedPin as Output pin
 
  Serial.begin(9600); //Call serial monitor
}


void loop() {
  if (Serial.available() > 0) 
{
    char command = Serial.read(); //Create new variable to store the serial monitor reading
    if (command == '1')   
{
      digitalWrite(LedPin, HIGH);  // Turn LED on
         
    } 
else if (command == '0') 
{
      digitalWrite(LedPin, LOW);   // Turn LED off
    }
  }
}
