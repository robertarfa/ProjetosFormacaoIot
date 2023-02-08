#define pinTemp A0
#define fan 3
#define buzzer 7

void setup()
{
  Serial.begin(9600);
  pinMode(buzzer, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  float temp = analogRead(pinTemp);
  temp = temp * 0.48828125;

  if (temp >= 30)
  {
    digitalWrite(fan, HIGH);
  }

  if (temp >= 50)
  {
    digitalWrite(LED_BUILTIN, HIGH);
    tone(buzzer, 261);
  }
}