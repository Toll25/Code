#include <Arduino.h>

#define INPUT_PIN_1 34
#define INPUT_PIN_2 35
#define INPUT_PIN_3 32
#define INPUT_PIN_4 33
#define INPUT_PIN_5 25
#define INPUT_PIN_6 26
#define LED_PIN_1 22

int inputPins[6] = {
  INPUT_PIN_1,
  INPUT_PIN_2,
  INPUT_PIN_3,
  INPUT_PIN_4,
  INPUT_PIN_5,
  INPUT_PIN_6
};

u_int8_t inputStatus = 0;

void setup() {
  Serial.begin(9600);
  ledcSetup(0,100,8);
  ledcAttachPin(LED_PIN_1,0);
  for (int i : inputPins){
    pinMode(i,INPUT_PULLUP);
  }
}

void loop() {
  inputStatus=0;
  for (int i = 0; i<sizeof(inputPins);i++) {
       int bitValue = digitalRead(inputPins[i]);  // Read the state of the input pin (0 or 1)
    inputStatus |= (bitValue << (i+2));  // Shift the bitValue to the correct position and OR it into inputStatus
  }
  Serial.print(inputStatus, DEC);
  Serial.print("\n");
  ledcWrite(0, inputStatus);
  delay(1000);
}

