#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define ANALOG_INPUT_PIN 36

Adafruit_SSD1306 oled(128, 64,&Wire, -1);


void setup() {
  Serial.begin(9600);
  pinMode( ANALOG_INPUT_PIN, ANALOG);
  analogReadResolution(6);
  ledcSetup(0,100,6);
  ledcAttachPin(32,0);
  if(!oled.begin(SSD1306_SWITCHCAPVCC, 0x3C)){
    Serial.println("OLED FAILED");
  }
  oled.clearDisplay();
  oled.setTextColor(SSD1306_WHITE);
  oled.write("Starting Up");
  oled.display();
}

void loop() {
  
  int8_t strength = analogRead(ANALOG_INPUT_PIN);

  Serial.println(strength, DEC);

  ledcWrite(0, strength);

  oled.clearDisplay();
  oled.setCursor(0,0);
  oled.print((strength*100)/63);
  oled.display();

  delay(100);
}