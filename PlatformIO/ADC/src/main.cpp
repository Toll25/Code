#include <Arduino.h>

#define ANALOG_INPUT_PIN 36

void setup() {
  Serial.begin(9600);
  pinMode( ANALOG_INPUT_PIN, ANALOG);
  analogReadResolution(6);
  ledcSetup(0,100,6);
  ledcAttachPin(22,0);
}

void loop() {
  
  int8_t strength = analogRead(ANALOG_INPUT_PIN);

  Serial.println(strength, DEC);

  ledcWrite(0, strength);

  delay(100);
  // put your main code here, to run repeatedly:
}