char data;
int LED=D0;
void setup()
{
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
 // digitalWrite (LED, HIGH); //initially set to low
  Serial.println("This is my First Example.");
}
void loop()
{
while (Serial.available())
  {Serial.println(data);
    data = Serial.read();


   
  }
  if (data == '1')
  digitalWrite (LED, HIGH);


  else if (data == '0')
  digitalWrite (LED, LOW);
}
