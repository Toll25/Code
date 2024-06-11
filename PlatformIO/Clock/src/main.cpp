#include <Arduino.h>
#include <Adafruit_SSD1306.h>

hw_timer_t *Timer0_Cfg = NULL;

Adafruit_SSD1306 oled(128, 64, &Wire, -1);

boolean countEnabled= true;

int timeStamp = 0;

const int interruptPin1 = 32; // Pin for interrupt 1
const int interruptPin2 = 33; // Pin for interrupt 2


void stopCount() {
  countEnabled = false; // Disable counting
}

void startCount() {
  countEnabled = true; // Disable counting
}

void resetCount() {
  timeStamp = 0; // Reset count
}

void IRAM_ATTR Timer0_ISR()
{
  if (countEnabled){
    timeStamp = timeStamp + 1;
  }
}

void setup()
{
  Serial.begin(9600);

  Timer0_Cfg = timerBegin(0, 80, true);
  timerAttachInterrupt(Timer0_Cfg, &Timer0_ISR, true);
  timerAlarmWrite(Timer0_Cfg, 10000, true);
  timerAlarmEnable(Timer0_Cfg);

  pinMode(interruptPin1, INPUT_PULLDOWN); // Set interrupt pin 1 as input with internal pull-up resistor
  pinMode(interruptPin2, INPUT_PULLDOWN); // Set interrupt pin 2 as input with internal pull-up resistor

  attachInterrupt(digitalPinToInterrupt(interruptPin1), stopCount, FALLING); // Attach interrupt on pin 32, falling edge
  attachInterrupt(digitalPinToInterrupt(interruptPin1), startCount, RISING);
  attachInterrupt(digitalPinToInterrupt(interruptPin2), resetCount, FALLING); // Attach interrupt on pin 33, falling edge


  if (!oled.begin(SSD1306_SWITCHCAPVCC, 0x3C))
  {
    Serial.println("OLED FAILED");
  }
  oled.clearDisplay();
  oled.setTextColor(SSD1306_WHITE);
  oled.write("Starting Up");
  oled.display();
}

void loop()
{
  // Assuming timeStamp is an integer representing hundredths of a second
int totalSeconds = timeStamp / 100;
int hours = totalSeconds / 3600;
int minutes = (totalSeconds % 3600) / 60;
int seconds = totalSeconds % 60;
int hundredths = timeStamp % 100;

// Format the time as HH:MM:SS:SS
char formattedTime[12]; // 11 characters for HH:MM:SS:SS and 1 for the null terminator
sprintf(formattedTime, "%02d:%02d:%02d:%02d", hours, minutes, seconds, hundredths);

oled.clearDisplay();
oled.setCursor(0, 0);
oled.print(formattedTime);
oled.display();
}
