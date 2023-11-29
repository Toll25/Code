#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 oled(128, 64,&Wire, -1);
int i = 0;

void setup() {
  Serial.begin(9600);
  if(!oled.begin(SSD1306_SWITCHCAPVCC, 0x3C)){
    Serial.println("OLED FAILED");
  }
  oled.clearDisplay();
  oled.setTextColor(SSD1306_WHITE);
  oled.write("Starting Up");
  oled.display();
}
void loop() {
  Serial.print("Updating");
  delay(1000);
  i++;
  oled.clearDisplay();
  oled.setCursor(0,0);
  oled.print(i);
  oled.display();
}
