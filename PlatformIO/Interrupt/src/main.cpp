#include <Arduino.h>

const int PIN_TO_INTERRUPT = 33;
const int LED_PIN = 16;
long now = millis();
long lastTrigger = 0;
int counter = 0;
boolean startTimer = false;
long debounceTime = 25;

void IRAM_ATTR lightLED()
{
  counter++;
  digitalWrite(LED_PIN, HIGH);
  startTimer = true;
  lastTrigger = millis();
}

void setup()
{
  Serial.begin(9600);
  Serial.println("setting up");

  pinMode(PIN_TO_INTERRUPT, PULLUP);

  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  attachInterrupt(digitalPinToInterrupt(PIN_TO_INTERRUPT), lightLED, RISING);
}

void loop()
{
  now = millis();

  if (startTimer && (now - lastTrigger > debounceTime))
  {
    Serial.println("no rising flank");
    digitalWrite(LED_PIN, LOW);
    startTimer = false;
    Serial.println(counter);
  }
}