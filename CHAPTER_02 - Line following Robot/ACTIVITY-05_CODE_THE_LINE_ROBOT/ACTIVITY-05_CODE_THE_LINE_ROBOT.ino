// Pin configuration for light-tracking robot
int Left_IR = D8; // GPIO pin for left light sensor
int Right_IR = D7; // GPIO pin for right light sensor

// Motor control pins
int M1 = D1; // Left motor control pin 1 D1
int M2 = D2; // Left motor control pin 2 D2
int M3 = D3; // Right motor control pin 1 D3
int M4 = D4; // Right motor control pin 2 D4

void setup(){
  // Configure light sensor pins as inputs
  pinMode(Left_IR, INPUT);
  pinMode(Right_IR, INPUT);
  // Configure motor pins as outputs
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
  pinMode(M3, OUTPUT);
  pinMode(M4, OUTPUT);
  // Initialize serial communication for debugging
  Serial.begin(9600);
}
void loop() 
{
  // Read the values from the light sensors
  int left = digitalRead(Left_IR);
  int right = digitalRead(Right_IR);

  // Print the sensor values to the serial monitor
  Serial.print("Left Sensor: ");
  Serial.print(left);
  Serial.print(" | Right Sensor: ");
  Serial.println(right);
  // Compare sensor values
  if (left == 1 && right == 1) 
{
    // Both sensors line detected, move forward
    digitalWrite(M1, HIGH);
    digitalWrite(M2, LOW);
    digitalWrite(M3, HIGH);
    digitalWrite(M4, LOW);
  } 

else if (left == 1 && right == 0) 
{
    // Left sensor sees line , turn right
    digitalWrite(M1, LOW);
    digitalWrite(M2, HIGH);
    digitalWrite(M3, HIGH);
    digitalWrite(M4, LOW);
  } 
else if (left == 0 && right == 1) 
{
    // Right sensor sees line, turn left
    digitalWrite(M1, HIGH);
    digitalWrite(M2, LOW);
    digitalWrite(M3, LOW);
    digitalWrite(M4, HIGH);
  } 
else 
{
    // Both sensors see white colors, stop
    digitalWrite(M1, LOW);
    digitalWrite(M2, LOW);
    digitalWrite(M3, LOW);
    digitalWrite(M4, LOW);
  }
  delay(200);
}
